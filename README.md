# 📸 insta_scrape — Instagram Public Profile Scraper

A small Streamlit app that fetches public Instagram profile information using **Instaloader**. This README contains everything you need to run it locally or deploy to **Streamlit Cloud (share.streamlit.io)**.

---

## 🖼️ Screenshot

![](assets/screenshot.png)

> Add your actual app screenshot in the `assets/` folder and name it `screenshot.png`.

---

## 🚀 Quick Start — Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/insta_scrape.git
cd insta_scrape
```

### 2️⃣ Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit app

```bash
streamlit run app.py
```

The app will open automatically in your browser at:

```
http://localhost:8501
```

---

## 📦 requirements.txt

```
streamlit>=1.20.0
instaloader>=4.12
pandas
requests
```

---

## 🌐 Live Demo (Streamlit Cloud)

You can view and use the live demo here:

👉 **[Open Live Demo on Streamlit Cloud](https://share.streamlit.io/your-username/insta_scrape/main/app.py)**

> Replace `your-username` with your GitHub username once deployed.

---

## ⚙️ Deploy on Streamlit Cloud

1. Push your code to GitHub.
2. Go to [Streamlit Cloud](https://share.streamlit.io/).
3. Click **New app** → Select your repo → Choose branch (e.g., `main`) → Set file path to `app.py`.
4. Click **Deploy**.

Your app will build and run automatically. You’ll get a URL similar to:

```
https://share.streamlit.io/<your-username>/insta_scrape/main/app.py
```

Add that link in this README under the **Live Demo** section.

---

## 🧠 Notes

* **Session file:** The app uses `Instaloader` to scrape Instagram profiles. To avoid frequent login issues, use an existing session file or configure Streamlit Secrets for credentials.
* **Caching:** The app uses `@st.cache_data` and `@st.cache_resource` to minimize redundant network calls.
* **Limitations:** Private or restricted accounts require authentication.

---

## 🪪 License

Released under the MIT License. Feel free to fork, improve, and share.

---

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/your-username/insta_scrape/main/app.py)
