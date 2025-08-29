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

yaml
Copy code

---

## ⚙️ Installation & Setup

### 1. Clone the repo
```bash
git clone https://github.com/YOUR-USERNAME/janabhoomi_project.git
cd janabhoomi_project
2. Create a virtual environment
bash
Copy code
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
4. Configure environment variables
Create a file named .env in the project root:

ini
Copy code
DIFY_API_KEY=your-dify-api-key-here
⚠️ Never commit .env to GitHub!
(It’s already ignored via .gitignore.)

If deploying to Streamlit Cloud, instead use:

Go to Secrets Manager in Streamlit Cloud

Add:

toml
Copy code
DIFY_API_KEY="your-dify-api-key-here"
▶️ Running the App Locally
bash
Copy code
streamlit run app.py
The app will open in your browser at http://localhost:8501.

🌍 Deployment (Streamlit Cloud)
Push this repo to GitHub.

Go to Streamlit Cloud → Deploy App.

Connect your repo.

Add your DIFY_API_KEY inside Secrets Manager.

Done ✅

👥 Contributing
Pull requests are welcome!
For major changes, please open an issue first to discuss what you’d like to change.

📜 License
This project is licensed under the AGPLv3 License.

