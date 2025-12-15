# 🌏 한-중-일 동시 마스터 (East Asia Language Tutor)

**DeepSeek V3 & Qwen 2.5 LLM을 활용한 한자 문화권 언어 동시 학습 플랫폼**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red)
![AI Model](https://img.shields.io/badge/Model-DeepSeek%20%7C%20Qwen-green)

## 📖 프로젝트 소개 (Introduction)
한국어 화자가 일본어와 중국어를 따로 배우는 비효율을 해결하기 위해 개발된 **AI 기반 언어 학습 튜터**입니다.

기존 번역기와 달리, **LLM(거대언어모델)**의 추론 능력을 활용하여 입력된 문장을 3개 국어로 동시에 보여주고, 특히 **한자(Hanja/Kanji/Hanzi)의 표기법 차이**와 **어순의 문법적 차이**를 실시간으로 비교 분석해줍니다.

## ✨ 주요 기능 (Key Features)
* **3개 국어 동시 학습:** 한국어 입력 시 중국어(간체)와 일본어 번역 결과를 한 화면에서 제공
* **AI 언어학 튜터:** 단순 번역을 넘어 문법적 차이, 뉘앙스, 어순을 상세히 설명
* **한자 비교 분석:** 같은 단어가 한국(Hanja), 중국(Hanzi), 일본(Kanji)에서 어떻게 다르게 표기되는지 시각적으로 정리
* **멀티 모델 지원:**
    * **DeepSeek-V3:** 뛰어난 가성비와 논리적 추론 능력
    * **Qwen 2.5 (via Together AI):** 아시아 언어(CJK) 및 문학적 표현에 특화된 모델

## 🛠 기술 스택 (Tech Stack)
* **Frontend & Backend:** Python, Streamlit
* **LLM Serving:** OpenAI Compatible API (DeepSeek, Together AI)
* **Environment:** Python venv
* **Version Control:** Git, GitHub

## 🚀 실행 방법 (How to Run)

이 프로젝트를 로컬 환경에서 실행하려면 아래 단계를 따라주세요.

**1. 레포지토리 클론 (Clone)**
```bash
git clone [`https://github.com/aboutexo04/dual-lang-ai.git`](https://github.com/aboutexo04/dual-lang-ai.git)
cd max1-lang-tutor
```

**2. 가상환경 생성 및 필수 라이브러리 설치**
```bash
# Mac/Linux
python -m venv venv
source venv/bin/activate

# 필수 패키지 설치
pip install -r requirements.txt
```

**3. API 키 설정**
* 앱 실행 후 왼쪽 사이드바(Sidebar)에 API Key를 직접 입력하여 사용할 수 있습니다.
* 또는 `.streamlit/secrets.toml` 파일을 생성하여 키를 저장할 수 있습니다.

**4. 앱 실행**
```bash
streamlit run app.py
```

## 📂 프로젝트 구조 (Project Structure)
```
📦 max1-lang-tutor
 ┣ 📂 .streamlit       # Streamlit 설정 (secrets.toml 등)
 ┣ 📜 app.py           # 메인 애플리케이션 코드
 ┣ 📜 requirements.txt # 의존성 라이브러리 목록
 ┣ 📜 .gitignore       # Git 제외 파일 목록
 ┗ 📜 README.md        # 프로젝트 설명서
```

## 📝 개발자 (Author)
* **Name:** Seo Yeon Moon
* **Contact:** aboutexo04@gmail.com
* **Role:** AI Application Engineer

---
*Created for AI Engineering Portfolio Project.*
