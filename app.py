import streamlit as st
from openai import OpenAI

# 페이지 기본 설정
st.set_page_config(page_title="한중일 AI 튜터", layout="wide")

st.title("🌏 한-중-일 동시 마스터")
st.markdown("한국어 문장을 입력하면 **중국어**와 **일본어**로 번역하고, **한자 차이**까지 알려줍니다.")

# --- 사이드바: 설정 영역 ---
st.sidebar.header("설정 (Settings)")

# 1. API 서비스 선택 (DeepSeek vs Together AI)
service_option = st.sidebar.selectbox(
    "사용할 모델 선택",
    ["DeepSeek (가성비)", "Qwen 2.5 (Together AI)"]
)

api_key = st.sidebar.text_input("API Key 입력", type="password")

# 선택에 따른 URL과 모델명 자동 설정
if service_option == "DeepSeek (가성비)":
    BASE_URL = "https://api.deepseek.com"
    MODEL_NAME = "deepseek-chat"
else:
    # Together AI (Qwen 사용 시)
    BASE_URL = "https://api.together.xyz/v1"
    MODEL_NAME = "Qwen/Qwen2.5-72B-Instruct-Turbo"

# --- 메인 기능 영역 ---
user_input = st.text_input("공부할 한국어 문장을 입력하세요:", "학생들이 도서관에서 공부하고 있다.")

if st.button("AI 선생님에게 물어보기 🚀"):
    if not api_key:
        st.error("좌측 사이드바에 API 키를 먼저 입력해주세요! 😅")
    else:
        # OpenAI 클라이언트 설정 (호환 모드)
        client = OpenAI(base_url=BASE_URL, api_key=api_key)
        
        # 시스템 프롬프트 (AI에게 역할을 부여)
        system_prompt = """
        너는 한국어, 중국어, 일본어 언어학 전문가야.
        입력된 한국어를 [중국어]와 [일본어]로 번역해줘.
        
        그리고 가장 중요한 것:
        1. 한자(Hanja/Kanji/Hanzi)의 표기법 차이를 비교해서 설명해줘. (간체자 vs 약자 vs 번체자)
        2. 어순이나 문법적 특징이 다르면 짚어줘.
        3. 출력은 마크다운 표(Table)나 글머리 기호를 써서 가독성 있게 보여줘.
        """

        with st.spinner(f"{service_option} 모델이 분석 중입니다..."):
            try:
                response = client.chat.completions.create(
                    model=MODEL_NAME,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": f"분석할 문장: {user_input}"},
                    ],
                    stream=False
                )
                
                # 결과 출력
                st.success("분석 완료!")
                st.markdown("### 📝 AI 분석 리포트")
                st.markdown(response.choices[0].message.content)
                
            except Exception as e:
                st.error(f"에러가 났어요: {e}")
