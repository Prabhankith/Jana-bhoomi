# 🌿 Janabhoomi – Telugu Public Diary

Janabhoomi is a **Streamlit-based diary application** where users can:
- ✍️ Write daily diary entries in **Telugu** (typed or via voice input).
- 🔒 Save entries **privately** or share them **publicly**.
- 🤖 Chat with an **AI-powered Chatbot** (Dify integration).
- 📚 Collect public diary data for building a **Telugu corpus**.

---

## 🚀 Features
- 🗣️ **Speech-to-Text (ASR)**: Convert spoken Telugu into text.
- 📝 **Diary System**: Save diary entries securely.
- 💬 **AI Chatbot Tab**: Ask questions and interact with a Dify-powered chatbot.
- 🌐 **Corpus Logger**: Collect public entries for research.
- 🗄️ **Database Handlers**: Manage saved entries.

---

## 📂 Project Structure
janabhoomi_project/
│── app.py # Main Streamlit app
│── requirements.txt # Python dependencies
│── .gitignore # Ignore secrets, env, cache
│── corpus/ # Stores diary entries (corpus)
│── prompts/ # Daily prompts for diaries
│── handlers/ # Handlers for ASR, DB, Chatbot, etc.
│ ├── asr_handler.py
│ ├── db_handler.py
│ └── chatbot_handler.py


---

## ⚙️ Installation & Setup

### 1. Clone the repo
```bash
git clone https://github.com/YOUR-USERNAME/janabhoomi_project.git
cd janabhoomi_project
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
streamlit run app.py
👥 Contributing

Pull requests are welcome!
For major changes, please open an issue first to discuss what you’d like to change.

📜 License

This project is licensed under the AGPLv3 License.
