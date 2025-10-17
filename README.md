# 📸 insta_scrape — Instagram Public Profile Scraper

A small Streamlit app that fetches public Instagram profile information using **Instaloader**. This README contains everything you need to copy & paste to deploy the app to **Streamlit Cloud (share.streamlit.io)** — including a screenshot placeholder, requirements, and step‑by‑step deploy instructions.

---

## Demo screenshot

> Replace `assets/screenshot.png` with your actual screenshot file in the repo. The screenshot below is a placeholder — add your own image file to the `assets/` folder and commit.

![](assets/screenshot.png)

---

## Repository structure (recommended)

```
insta_scrape/
├─ app.py                  # your Streamlit app (the file you pasted)
├─ requirements.txt        # Python deps
├─ README.md               # this file
├─ assets/
│  └─ screenshot.png       # screenshot to show in README
```

> ✅ **Tip:** Name your main file `app.py` or `streamlit_app.py` — Streamlit Cloud will need the file path when connecting your repo.

---

## requirements.txt (copy & paste)

```
streamlit>=1.20.0
instaloader>=4.12
pandas
requests
```

Add any other packages your app uses.

---

## Important security note about Instagram sessions

Instaloader can use a saved session file to avoid repeated logins. **Do not commit sensitive credentials** (passwords/session cookies) to a public repository.

Two safe approaches:

1. **Use Streamlit Secrets to store credentials** (recommended): store `INSTAGRAM_USERNAME` and `INSTAGRAM_PASSWORD` in Streamlit Cloud Secrets and modify the app to programmatically log in on startup (see *Optional: automatic login snippet* below).

2. **Generate a session file locally and upload privately**: this is less recommended because session cookies are sensitive. If you must, keep the repo private.

---

## Optional: automatic login snippet (use with Streamlit Secrets)

If you want the app to log in on Streamlit Cloud using secrets, add this small snippet to your `app.py` (place before `L.load_session_from_file(...)` attempt):

```python
import os
from instaloader import Instaloader

USERNAME = st.secrets.get("INSTAGRAM_USERNAME")
PASSWORD = st.secrets.get("INSTAGRAM_PASSWORD")

if USERNAME and PASSWORD:
    try:
        L.context.log("Logging in with provided secrets...")
        L.login(USERNAME, PASSWORD)
        # Save session to temporary file so subsequent runs in the same container reuse it
        L.save_session_to_file(f"{USERNAME}.session")
        st.success("Logged in to Instagram (session created).")
    except Exception as e:
        st.error(f"Auto-login failed: {e}")
```

**Streamlit Cloud note:** container filesystem is ephemeral — sessions saved to disk survive for the life of the container, but may be lost when the container is restarted. Using secrets + login at startup is more robust than committing session files.

---

## Deploy to Streamlit Cloud — step by step (copy & paste)

1. Create a new GitHub repository called `insta_scrape` and push the repo structure above.

2. Ensure `app.py` is in the repo root (or note its path if different).

3. Add `requirements.txt` (copy the block above).

4. Add the screenshot `assets/screenshot.png` (optional but useful).

5. Commit and push all changes to GitHub.

6. Go to: [https://share.streamlit.io](https://share.streamlit.io) and sign in with your GitHub account.

7. Click **New app** → select the repository `your-user/insta_scrape` → choose the branch (e.g., `main`) and enter the file path (`app.py`). Click **Deploy**.

8. (Optional) Add Streamlit secrets for safe Instagram login:

   * In the deployed app settings click **Advanced settings** → **Secrets** and add keys: `INSTAGRAM_USERNAME` and `INSTAGRAM_PASSWORD`.
   * Or add them from GitHub Actions or environment depending on your workflow.

9. After deploy completes, Streamlit will provide a URL in the form:

```
https://share.streamlit.io/<github-username>/insta_scrape/<branch>/app.py
```

Example:

```
https://share.streamlit.io/malik123/insta_scrape/main/app.py
```

Share that URL with others.

---

## Troubleshooting & tips

* **LoginRequiredException / Private profiles:** Use a logged-in session (see *Optional: automatic login snippet*). Many profile fields require authentication.
* **Rate limits / errors fetching posts:** Instaloader may be rate-limited — avoid rapidly calling `get_posts()` in loops and consider caching results with `st.cache_data` (you already do in parts of the app).
* **Profile picture & images failing to load:** Streamlit Cloud restricts some cross-origin requests. Your code uses `requests` to fetch images — that usually works, but wrap in try/except and fallback to a placeholder image.
* **Session file persistence:** Streamlit Cloud containers can be restarted; don't rely on a file stored on disk for long-term persistence. Use secrets to perform logins on startup instead.

---

## Example README README snippet to paste on GitHub front page

Use the contents of this file as your repo `README.md`. If you want a short badge to link to the live app, add this badge markdown (replace URL with your app URL):

```md
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/<your-user>/insta_scrape/main/app.py)
```

---

## License

This project is released under the MIT License. Replace as needed.

---

## Final notes

* Paste the exact `requirements.txt`, `app.py`, and `README.md` into your repo. After connecting the repo on Streamlit Cloud the app should deploy.
* If you'd like, I can also:

  * produce a `requirements.txt` file content (already above),
  * give you a small code patch to make saving/loading sessions safer on Streamlit Cloud, or
  * generate a ready-to-copy `streamlit_app.py` that includes automatic login using `st.secrets`.

Happy deploying — once you push the repo and deploy, the Streamlit Cloud URL will be ready to share.
