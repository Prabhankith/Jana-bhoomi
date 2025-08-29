import streamlit as st
from prompts.prompt_generator import get_daily_prompt
from handlers.db_handler import save_entry, get_entries
from corpus.corpus_logger import log_to_corpus
from handlers.chatbot_handler import ask_dify, get_dify_api_key  # ✅ import key check

st.set_page_config(page_title="Janabhoomi", layout="centered")
st.title("📔 జనభూమి - Telugu Public Diary")

# Create two tabs
tab1, tab2 = st.tabs(["📖 Diary", "🤖 Mitrudu Chatbot"])

# ---------------- Tab 1: Diary ----------------
with tab1:
    prompt = get_daily_prompt()
    st.markdown(f"🗒️ **ఈరోజు ప్రేరణ:** *{prompt}*")

    entry = st.text_area("మీ భావాలను తెలుగులో రాయండి", height=200)

    if entry:
        privacy = st.radio("ప్రైవసీ ఎంపిక:", ["ప్రైవేట్", "పబ్లిక్"])
        if st.button("సేవ్ చేయండి"):
            save_entry(entry, privacy)
            log_to_corpus(entry, privacy)
            st.success("ఎంట్రీ సేవ్ అయ్యింది!")

    st.subheader("🔓 పబ్లిక్ డైరీ ఎంట్రీలు")
    for item in get_entries(public_only=True):
        st.markdown(f"📝 *{item['text']}*")

# ---------------- Tab 2: Chatbot ----------------
with tab2:
    st.subheader("🤖 మీ వ్యక్తిగత చాట్‌బాట్‌")

    if not get_dify_api_key():
        st.warning("⚠️ Chatbot unavailable. Please configure your DIFY_API_KEY in `.env` or Streamlit Secrets.")
    else:
        user_msg = st.text_input("మీ ప్రశ్న రాయండి...")

        if st.button("Ask Chatbot"):
            if user_msg.strip():
                response = ask_dify(user_msg)
                st.markdown(f"**Bot:** {response}")
            else:
                st.warning("⚠️ Please enter a question.")
