<h1 align="left">🤖 Gemini-Powered Chatbot (LangChain + Streamlit)</h1>

###

<h3 align="left">
🧠 A basic AI chatbot built using <strong>LangChain</strong> and <strong>Google Gemini</strong><br>
⚡ Features real-time streaming responses and session-based memory<br>
🧩 Clean separation between UI and LLM logic
</h3>

###

<br clear="both">

<div align="center">
  <img height="200" src="https://media.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif" />
</div>

---

## 📁 Project Structure

```

.
├── app.py                  # Streamlit UI
├── chatbot_stremlit.py     # LangChain + Gemini logic
├── requirements.txt
├── .gitignore
├── README.md
└── .env                    # API keys (created by user)

````

---

## 🌟 Key Features

- 🧠 **Session-based Conversational Memory**  
  Maintains chat history using `st.session_state`

- ⚡ **Streaming Responses**  
  Uses LangChain `.stream()` for live output

- 🧩 **Clean Architecture**
  - `chatbot_stremlit.py` → AI logic  
  - `app.py` → UI and interaction  

- 🔐 **Secure API Management**  
  Uses `.env` file with `python-dotenv`

---

<div align="center">
  <img height="200" src="https://media.giphy.com/media/jBOOXxSJfG8kqMxT11/giphy.gif" />
</div>

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **LLM:** Google Gemini (`gemini-2.5-flash-lite`)
- **Frameworks:** LangChain (LCEL), Streamlit
- **Utilities:** python-dotenv

---

## 🚀 Complete Setup Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
````

---

### 2️⃣ (Optional) Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Create `.env` File

Create a file named **`.env`** in the root directory.

```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

⚠️ Never commit `.env` to GitHub.

---

### 5️⃣ Run the App

```bash
streamlit run app.py
```

The chatbot will open in your browser.

---

## 🧠 How It Works (High-Level)

```
User → Streamlit UI → LangChain Prompt
     → Gemini Model → Streamed Response
```

* Chat history is injected using `MessagesPlaceholder`
* Responses stream live using `st.write_stream`
* Memory persists within the session

---

## 📦 requirements.txt (Example)

```txt
streamlit
langchain
langchain-google-genai
python-dotenv
```

---

## 🧠 What I Learned

* Using **LangChain Expression Language (LCEL)**
* Handling Streamlit reruns via **Session State**
* Implementing **real-time LLM streaming**
* Structuring AI apps cleanly and scalably

---

## 👨‍💻 Author

**Dev Doshi**
B.Tech | AI / ML | LangChain | Streamlit | Generative AI

---

## 🔗 Let’s Connect

<div align="left">
  <a href="https://www.linkedin.com/in/dev-doshi-8360a727b" target="_blank">
    <img src="https://raw.githubusercontent.com/maurodesouza/profile-readme-generator/master/src/assets/icons/social/linkedin/default.svg" width="52" height="40" />
  </a>
</div>

---

⭐ If you found this useful, consider starring the repository.

```
Thank you for reading
```
