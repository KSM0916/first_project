import streamlit as st
import random

# 🎉 타이틀과 설명
st.set_page_config(page_title="가위✌️ 바위✊ 보✋ 게임", page_icon="🎮", layout="centered")
st.title("🎮 가위✌️ 바위✊ 보✋ 게임")
st.markdown("### 운을 시험해보세요! 컴퓨터와 가위바위보 대결! 🧠💥")
st.markdown("---")

# 🖼️ 이모지 매핑
emoji_map = {
    "가위": "✌️",
    "바위": "✊",
    "보": "✋"
}

# 🧑 사용자 선택
user_choice = st.selectbox("👉 당신의 선택은?", ["가위", "바위", "보"], index=0, format_func=lambda x: f"{emoji_map[x]} {x}")

# 🤖 컴퓨터 선택
if st.button("🎲 게임 시작!"):
    comp_choice = random.choice(["가위", "바위", "보"])

    st.markdown("## ⚔️ 대결 결과 ⚔️")
    st.markdown(f"**당신**: {emoji_map[user_choice]} {user_choice}")
    st.markdown(f"**컴퓨터**: {emoji_map[comp_choice]} {comp_choice}")

    # 🧠 승패 판단
    if user_choice == comp_choice:
        result = "😮 비겼습니다!"
    elif (user_choice == "가위" and comp_choice == "보") or \
         (user_choice == "바위" and comp_choice == "가위") or \
         (user_choice == "보" and comp_choice == "바위"):
        result = "🎉 당신이 이겼어요!"
    else:
        result = "😢 컴퓨터가 이겼어요..."

    st.markdown(f"### 🏁 결과: {result}")
    st.balloons() if "이겼어요" in result else None

# 📌 푸터
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit & Python")

