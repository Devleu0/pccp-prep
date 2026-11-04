"""풀이 기록 CSV를 읽어 유형별 진도와 약점을 요약한다.

사용법:
    python tools/progress_report.py tracker/problems.csv [--threshold 0.6]

CSV 열: id,title,category,level,status,minutes,date,note
    status: solved(혼자 해결) | hint(해설 참고) | failed(미해결) | todo
"""
import argparse
import csv
import sys
from collections import defaultdict
from dataclasses import dataclass, field

VALID_STATUS = ("solved", "hint", "failed", "todo")
REQUIRED_COLUMNS = ("id", "title", "category", "level", "status", "minutes", "date", "note")


@dataclass
class CategoryStat:
    attempted: int = 0
    solved: int = 0
    minutes: list = field(default_factory=list)

    @property
    def success_rate(self):
        return self.solved / self.attempted if self.attempted else 0.0

    @property
    def avg_minutes(self):
        return sum(self.minutes) / len(self.minutes) if self.minutes else 0.0


def load_records(path):
    """CSV를 읽고 형식을 검증한다. 잘못된 행이 있으면 ValueError."""
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        missing = [c for c in REQUIRED_COLUMNS if c not in (reader.fieldnames or [])]
        if missing:
            raise ValueError(f"CSV에 필요한 열이 없습니다: {missing}")
        records = []
        for line_no, row in enumerate(reader, start=2):
            status = row["status"].strip()
            if status not in VALID_STATUS:
                raise ValueError(f"{line_no}행: status '{status}'는 {VALID_STATUS} 중 하나여야 합니다")
            records.append(row)
    return records


def summarize(records):
    """category → CategoryStat. todo 상태는 시도 횟수에서 뺀다."""
    stats = defaultdict(CategoryStat)
    for row in records:
        status = row["status"].strip()
        if status == "todo":
            continue
        stat = stats[row["category"].strip()]
        stat.attempted += 1
        if status == "solved":
            stat.solved += 1
        minutes = row["minutes"].strip()
        if minutes:
            stat.minutes.append(float(minutes))
    return dict(stats)


def weak_categories(stats, threshold=0.6):
    """혼자 해결한 비율이 threshold 미만인 유형을 성공률 오름차순으로 반환."""
    weak = [(name, s.success_rate) for name, s in stats.items() if s.success_rate < threshold]
    return [name for name, _ in sorted(weak, key=lambda x: (x[1], x[0]))]


def format_report(stats, threshold=0.6):
    lines = [f"{'유형':<16}{'시도':>6}{'해결':>6}{'성공률':>8}{'평균(분)':>10}"]
    for name in sorted(stats):
        s = stats[name]
        lines.append(f"{name:<16}{s.attempted:>6}{s.solved:>6}{s.success_rate:>8.0%}{s.avg_minutes:>10.1f}")
    weak = weak_categories(stats, threshold)
    lines.append("")
    lines.append("다음 주 우선 학습: " + (", ".join(weak) if weak else "없음 (모든 유형이 기준 이상)"))
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description="PCCP 풀이 진도 리포트")
    parser.add_argument("csv_path")
    parser.add_argument("--threshold", type=float, default=0.6, help="약점 판정 성공률 기준 (기본 0.6)")
    args = parser.parse_args(argv)
    try:
        records = load_records(args.csv_path)
    except (OSError, ValueError) as e:
        print(f"오류: {e}", file=sys.stderr)
        return 1
    print(format_report(summarize(records), args.threshold))
    return 0


if __name__ == "__main__":
    sys.exit(main())
