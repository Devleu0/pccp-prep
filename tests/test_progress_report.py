import pytest

from tools.progress_report import format_report, load_records, main, summarize, weak_categories

HEADER = "id,title,category,level,status,minutes,date,note\n"


def write_csv(tmp_path, body):
    path = tmp_path / "p.csv"
    path.write_text(HEADER + body, encoding="utf-8")
    return path


def test_summarize_and_weak_categories(tmp_path):
    path = write_csv(
        tmp_path,
        "1,a,bfs_dfs,2,solved,20,2026-11-04,\n"
        "2,b,bfs_dfs,2,hint,40,2026-11-04,경계 조건\n"
        "3,c,dp,3,failed,60,2026-11-05,\n"
        "4,d,hash,1,solved,10,2026-11-05,\n"
        "5,e,dp,3,todo,,,\n",
    )
    stats = summarize(load_records(path))
    assert stats["bfs_dfs"].attempted == 2
    assert stats["bfs_dfs"].success_rate == 0.5
    assert stats["dp"].attempted == 1  # todo는 시도에서 제외
    assert weak_categories(stats) == ["dp", "bfs_dfs"]
    report = format_report(stats)
    assert "다음 주 우선 학습: dp, bfs_dfs" in report


def test_invalid_status_raises(tmp_path):
    path = write_csv(tmp_path, "1,a,dp,1,done,10,,\n")
    with pytest.raises(ValueError, match="status"):
        load_records(path)


def test_main_returns_error_code_for_missing_file(tmp_path, capsys):
    assert main([str(tmp_path / "none.csv")]) == 1
    assert "오류" in capsys.readouterr().err


def test_bundled_tracker_is_valid():
    assert load_records("tracker/problems.csv")
