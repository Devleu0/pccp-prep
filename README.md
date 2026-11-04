# PCCP 대비 저장소 (pccp-prep)

프로그래머스 **PCCP(코딩전문역량인증, Programmers Certified Coding Professional)** 시험 정보 조사 결과와
목표 등급별 대비 전략, 학습 로드맵, 시험 당일 플레이북, 암기용 알고리즘 템플릿, 진도 추적 도구를 모아 둔 저장소입니다.

> 시험 정보 검증일: **2026-11-04** (공식 사이트 `certi.programmers.co.kr` 기준).
> 응시료·언어 등은 바뀔 수 있으니 접수 전에 [공식 안내](https://certi.programmers.co.kr/about/pccp)를 꼭 다시 확인하세요.

## 한눈에 보기

| 항목 | 내용 |
| --- | --- |
| 문항 / 시간 | 코드 작성 **4문항 / 120분** |
| 언어(택1) | Python, Java, JavaScript, C, C++, C# |
| 응시료 | 50,000원 |
| 합격 | 1000점 만점 중 **400점 이상**, 등급 Lv.1 ~ Lv.5 |
| 유효기간 | 2년 |
| 방식 | 비대면 IBT(모니토), 웹캠과 스마트폰 카메라로 감독, **외부 IDE 사용 금지** |

## 저장소 구조

```text
pccp-prep/
├── docs/                      # 조사 결과와 전략 문서 (한 주제에 한 파일)
│   ├── 01-exam-overview.md    # 시험 개요, 규정, 출처
│   ├── 02-scope-and-grading.md# 출제 범위, 등급, 채점 특성
│   ├── 03-strategy.md         # 목표 등급별 전략, 점수 모델
│   ├── 04-roadmap-8weeks.md   # 8주 학습 로드맵
│   ├── 05-exam-day-playbook.md# 시험 당일 시간 배분과 체크리스트
│   └── 06-problem-bank.md     # 기출과 유형별 추천 문제
├── templates/python/          # IDE 없이 손으로 칠 알고리즘 템플릿 (모듈 하나에 주제 하나)
├── tools/progress_report.py   # 풀이 기록(CSV)을 유형별 진도 리포트로 요약
├── tracker/problems.csv       # 풀이 기록 (한 줄에 문제 하나)
├── tests/                     # 템플릿과 도구 단위 테스트 (pytest)
└── .github/                   # CI, PR/이슈 템플릿
```

## 사용법

```bash
# 1) 템플릿 동작 확인
pip install pytest
pytest -q

# 2) 문제를 풀 때마다 tracker/problems.csv 에 한 줄 추가 후 리포트 보기
python tools/progress_report.py tracker/problems.csv
```

## 읽는 순서

1. [시험 개요](docs/01-exam-overview.md) → 2. [출제 범위·채점](docs/02-scope-and-grading.md)
3. [전략](docs/03-strategy.md) → 4. [로드맵](docs/04-roadmap-8weeks.md)
5. [당일 플레이북](docs/05-exam-day-playbook.md) → 6. [문제 은행](docs/06-problem-bank.md)

협업 규칙은 [CONTRIBUTING.md](CONTRIBUTING.md)를 참고하세요.
