# 기여 가이드

스터디원 여러 명이 함께 쓰는 것을 전제로 한 규칙입니다.

## 브랜치 / 커밋

- `main`은 보호 브랜치입니다. 모든 변경은 PR로 올립니다.
- 브랜치 이름: `docs/<주제>`, `template/<알고리즘>`, `solve/<문제ID>-<닉네임>`, `tool/<기능>`
- 커밋 메시지: `docs: ...`, `feat(template): ...`, `solve(250136): ...`, `fix: ...`, `test: ...`

## 어디에 무엇을 두나

| 변경 | 위치 | 규칙 |
| --- | --- | --- |
| 시험 정보 갱신 | `docs/01-exam-overview.md` | **출처 URL과 검증일**을 함께 갱신. 공식/2차 출처를 ✅/⚠️로 구분 |
| 전략, 로드맵 | `docs/03~05` | 한 문서에 한 주제. 다른 문서 내용은 복사하지 말고 링크 |
| 문제 추가 | `docs/06-problem-bank.md` | 기존 **분류 키**를 사용. 새 키가 필요하면 PR에서 따로 논의 |
| 템플릿 | `templates/<언어>/<주제>.py` | 표준 라이브러리만 사용, docstring에 복잡도와 사용 예 적기, **테스트 필수** |
| 풀이 기록 | `tracker/problems.csv` | 개인 기록은 `tracker/<닉네임>.csv`로 따로 만들어도 됩니다 |

## 다른 언어 템플릿 추가

`templates/cpp/`, `templates/java/`처럼 언어별 폴더를 만들고 Python 템플릿과 같은 파일 이름을 씁니다.
예를 들어 `graph_search.cpp`를 만들어 언어 사이에 대응이 보이게 합니다.

## PR 전 확인

```bash
pytest -q
python tools/progress_report.py tracker/problems.csv
```
