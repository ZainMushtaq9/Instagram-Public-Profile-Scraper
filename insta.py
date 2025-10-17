import streamlit as st
import instaloader
import pandas as pd
from datetime import datetime
import time
import requests
import random

# --- App Configuration ---
st.set_page_config(
    page_title="Instagram Scraper",
    page_icon="📸",
    layout="wide",
)

# --- Caching & Instaloader Logic ---

@st.cache_resource
def get_instaloader_instance():
    """
    Creates and returns a single instance of Instaloader.
    Tries to load a session from a file to avoid repeated logins.
    """
    L = instaloader.Instaloader(
        download_pictures=False,
        download_videos=False,
        download_video_thumbnails=False,
        download_geotags=False,
        download_comments=False,
        save_metadata=False,
        compress_json=False,
    )
    
    try:
        # --- IMPORTANT ---
        # Replace 'your_instagram_username' with the username for your session file.
        session_username = "your_instagram_username" 
        L.load_session_from_file(session_username)
        st.success(f"✅ Logged in with session: {session_username}")
    except FileNotFoundError:
        st.warning(
            "⚠️ Session file not found. "
            "Scraping will be done anonymously and is likely to fail."
        )
    except Exception as e:
        st.error(f"Could not load session: {e}")
        
    return L

@st.cache_data(ttl=3600, show_spinner="Fetching profile data...")
def get_profile_data(_L, username):
    """Fetches Instagram profile data for a given username."""
    try:
        profile = instaloader.Profile.from_username(_L.context, username)
        return profile
    except instaloader.exceptions.ProfileNotExistsException:
        st.error(f"Profile '{username}' does not exist.")
    except instaloader.exceptions.LoginRequiredException:
        st.error("Login required to view this profile. Please create a session file.")
    except instaloader.exceptions.PrivateProfileNotFollowedException:
        st.error("This profile is private and you do not follow it.")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
    return None

# --- Main App UI ---
st.title("📸 Instagram Public Profile Scraper")
st.markdown("Enter an Instagram username to fetch public profile data. **Note:** A logged-in session is required for reliable results.")

L_instance = get_instaloader_instance()

col1, col2 = st.columns([3, 1])
with col1:
    username_input = st.text_input(
        "Enter Instagram Username", 
        placeholder="e.g., nasa", 
        label_visibility="collapsed"
    )
with col2:
    scrape_button = st.button("Scrape Profile", type="primary", use_container_width=True)

# --- Main Content Area for Displaying Results ---
if scrape_button and username_input:
    profile = get_profile_data(L_instance, username_input)

    if profile:
        st.header(f"@{profile.username}")

        # --- Profile Header ---
        c1, c2 = st.columns([1, 3])
        with c1:
            try:
                session = L_instance.context._session
                response = session.get(profile.profile_pic_url, stream=True)
                response.raise_for_status()
                st.image(response.content, width=150, caption="Profile Picture")
            except Exception as e:
                st.error(f"Could not load profile picture.")

        with c2:
            st.subheader(f"{profile.full_name}")
            st.markdown(f"**Bio:** {profile.biography}")
            if profile.external_url:
                st.markdown(f"**Website:** [{profile.external_url}]({profile.external_url})")
        
        # --- Key Metrics ---
        st.markdown("---")
        metric1, metric2, metric3, metric4 = st.columns(4)
        metric1.metric("Total Posts", f"{profile.mediacount:,}")
        metric2.metric("Followers", f"{profile.followers:,}")
        metric3.metric("Following", f"{profile.followees:,}")
        
        account_type = "Public ✅"
        if profile.is_business_account: account_type = "Business 🏢"
        if profile.is_private: account_type = "Private 🔒"
        metric4.metric("Account Type", account_type)

        # --- Data Tabs ---
        st.markdown("---")
        # tab1, tab2, tab3 = st.tabs(["📊 Recent Posts", "👥 Followers", "👤 Following"])
        
        # # --- TAB 1: RECENT POSTS ---
        # with tab1:
        #     st.subheader("Recent Posts (Latest 12)")
        #     with st.spinner("Loading posts..."):
        #         try:
        #             posts = profile.get_posts()
        #             post_count = 0
        #             cols = st.columns(4)
        #             session = L_instance.context._session

        #             for post in posts:
        #                 if post_count >= 12:
        #                     break
        #                 with cols[post_count % 4]:
        #                     try:
        #                         response = session.get(post.url, stream=True)
        #                         response.raise_for_status()
        #                         st.image(response.content, caption=f"❤️ {post.likes:,} | 💬 {post.comments:,}")
        #                     except Exception:
        #                         st.warning("Image failed to load.")
        #                 post_count += 1
                        
        #             if post_count == 0:
        #                 st.warning("This user has no public posts.")
        #         except Exception as e:
        #             st.error(f"Could not retrieve posts. Often due to rate-limiting. Error: {e}")

        # # --- TAB 2: FOLLOWERS ---
        # with tab2:
        #     st.subheader("Followers Preview (First 50)")
        #     with st.spinner("Loading followers list..."):
        #         try:
        #             followers_list = []
        #             # Fetch only the first 50 to avoid rate limits and long waits
        #             for i, f in enumerate(profile.get_followers()):
        #                 if i >= 50:
        #                     break
        #                 followers_list.append(f.username)
                    
        #             df_followers = pd.DataFrame(followers_list, columns=["Username"])
        #             st.dataframe(df_followers, use_container_width=True)
        #         except Exception as e:
        #             st.error(f"Could not retrieve followers. This is often a rate-limit issue. Error: {e}")
        
        # # --- TAB 3: FOLLOWING ---
        # with tab3:
        #     st.subheader("Following Preview (First 50)")
        #     with st.spinner("Loading 'following' list..."):
        #         try:
        #             followees_list = []
        #             # Fetch only the first 50
        #             for i, f in enumerate(profile.get_followees()):
        #                 if i >= 50:
        #                     break
        #                 followees_list.append(f.username)

        #             df_followees = pd.DataFrame(followees_list, columns=["Username"])
        #             st.dataframe(df_followees, use_container_width=True)
        #         except Exception as e:
        #             st.error(f"Could not retrieve 'following' list. Error: {e}")

elif scrape_button and not username_input:
    st.warning("Please enter a username to search for.")