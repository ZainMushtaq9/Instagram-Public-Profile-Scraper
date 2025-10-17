# 📸 insta_scrape — Instagram Public Profile Scraper

A small Streamlit app that fetches public Instagram profile information using **Instaloader**. This README contains everything you need to run it locally or view the live demo.

---

## 🖼️ Screenshot

![](instagram-demo.jpg)

> The screenshot file `instagram-demo.jpg` is located in the main folder.

---

## 🚀 Quick Start — Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/ZainMushtaq9/Instagram-Public-Profile-Scraper.git
cd Instagram-Public-Profile-Scraper
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

You can view and use the **live deployed version** here:

👉 **[Open Live Demo on Streamlit Cloud](https://instagram-scrape.streamlit.app/)**

---

## ⚙️ Deploy on Streamlit Cloud

1. Push your code to GitHub: [ZainMushtaq9/Instagram-Public-Profile-Scraper](https://github.com/ZainMushtaq9/Instagram-Public-Profile-Scraper.git)
2. Go to [Streamlit Cloud](https://share.streamlit.io/).
3. Click **New app** → Select your repo → Choose branch (e.g., `main`) → Set file path to `app.py`.
4. Click **Deploy**.

Your app will build and run automatically. You’ll get a URL similar to:

```
https://instagram-scrape.streamlit.app/
```

---

## 🧠 Notes

* **Session file:** The app uses `Instaloader` to scrape Instagram profiles. To avoid frequent login issues, use an existing session file or configure Streamlit Secrets for credentials.
* **Caching:** The app uses `@st.cache_data` and `@st.cache_resource` to minimize redundant network calls.
* **Limitations:** Private or restricted accounts require authentication.

---

## 🪪 License

Released under the MIT License. Feel free to fork, improve, and share.

---

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://instagram-scrape.streamlit.app/)
