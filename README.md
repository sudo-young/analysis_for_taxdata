
# 💼 세무 데이터 분석 프로젝트

실제 세무 데이터를 기반으로 납세 리스크 탐지, 패턴 분석, 자동화 시나리오를 구현한 프로젝트입니다. 세무 지식과 데이터 분석 기술의 융합 역량을 강조합니다.

---

## 📊 프로젝트 개요

- **목적**: 전자세금계산서 및 부가세 관련 데이터를 활용한 납세 리스크 분석 및 자동화 사례 구현
- **도구**: Python (pandas, scikit-learn), Matplotlib/Seaborn, UiPath/RPA, Excel
- **대상 데이터**: 가상 세무 데이터셋 (세금계산서, 부가세 신고서 등)

---

## 📁 프로젝트 구성

### 1. 부가세 납부 패턴 분석
- 업종/지역/시기별 부가세 납부 트렌드 시각화
- 납부액 급증/급감 여부 탐지 (시계열 분석)
- 이상치 거래 분포 시각화

→ 📂 `vat-pattern-analysis/`

---

### 2. 납세 리스크 점수화
- 전자세금계산서 기반 리스크 스코어 모델링
- 주요 지표:
  - 거래 불균형
  - 반복 거래 상대방
  - 거래량 급변
- 간단한 이상치 탐지 알고리즘 (Isolation Forest 등) 활용

→ 📂 `tax-risk-scoring/`

---

### 3. 세무 자동화 (RPA)
- Python으로 Excel 신고서 자동 생성
- UiPath를 활용한 PDF 발행 & 파일 전송 자동화 예제
- 예시 시나리오:
  1. Excel → PDF 자동 변환
  2. 이메일 자동 첨부 전송

→ 📂 `tax-automation/`

---

## 📌 주요 성과

- 반복 세무 분석/신고 프로세스의 자동화 가능성 검증
- 거래 구조 기반의 간단한 납세 위험 진단 지표 개발
- 실무 기반의 데이터 핸들링 + 시각화 + RPA 통합 프로젝트

---

## 📷 결과 예시

| 프로젝트 | 결과 이미지 |
|----------|-------------|
| 납부 패턴 분석 | ![VAT 트렌드](images/vat_trend.png) |
| 리스크 점수 | ![Risk Graph](images/risk_score.png) |
| 자동화 시연 | ![RPA Demo](images/rpa_gif.gif) |

---
<!--
## 🚀 실행 방법

```bash
git clone https://github.com/sudo-young/[레포이름].git
cd [레포이름]
# 각 폴더별 README.md 참고
```

- 💼 LinkedIn: [https://linkedin.com/in/your-name]
--!>
---

## 📮 문의

- 📧 Contact: [corporatetax.sy@gmail.com]

