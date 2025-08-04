import requests
import streamlit as st
import pickle
from dotenv import load_dotenv
import os

load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

# --- API Call ---
def fetch_Poster(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}'
    )
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# --- Recommender Function ---
def recommend(movie):
    movieIndex = movies_list[movies_list['title'] == movie].index[0]
    distance = similarity[movieIndex]
    movieList = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:16]

    recommended_movies = []
    recommended_movies_poster = []
    recommended_movies_ids = []
    for i in movieList:
        movie_id = movies_list.iloc[i[0]]['id']
        recommended_movies.append(movies_list.iloc[i[0]]['title'])
        recommended_movies_poster.append(fetch_Poster(movie_id))
        recommended_movies_ids.append(movie_id)  # Collect IDs

    return recommended_movies, recommended_movies_poster, recommended_movies_ids

# --- Load Data ---
movies_list = pickle.load(open('movies.pkl', 'rb'))
movies_titles = movies_list['title'].values
similarity = pickle.load(open('similarity.pkl', 'rb'))

# --- Page Config ---
st.set_page_config(page_title="Movie Recommender", layout="wide")

# --- Custom CSS for styling ---
st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
    }
    .main-title {
        font-size: 48px;
        font-weight: 900;
        text-align: center;
        margin-bottom: 30px;
        color: #e63946;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .section-header {
        font-size: 28px;
        margin-top: 40px;
        margin-bottom: 20px;
        color: #f0f2f5;
        font-weight: 700;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-align: center;
    }
    .movie-title {
        font-weight: 700;
        font-size: 20px;
        text-align: center;
        margin-top: 12px;
        color: #f0f2f5;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    img {
        border-radius: 12px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        max-width: 100%;
        height: auto;
        cursor: pointer;
    }
    img:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }
    .selected-movie-container {
        background: white;
        max-width: 600px;
        margin: 0 auto 40px auto;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
    }
    .recommendations-container {
        padding: 0 40px 60px 40px;
        max-width: 1200px;
        margin: 0 auto;
    }
    .recommendation-row {
        margin-bottom: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# --- App Title ---
st.markdown('<div class="main-title">🎬 Movie Recommender System</div>', unsafe_allow_html=True)

# --- Movie Selection ---
st.markdown('<div class="section-header">Select a Movie</div>', unsafe_allow_html=True)

selected_movie_name = st.selectbox("", movies_titles)

selected_movie_id = movies_list[movies_list['title'] == selected_movie_name].iloc[0]['id']
selected_movie_poster = fetch_Poster(selected_movie_id)

# Selected Movie Display
st.markdown('<div class="section-header">You Selected:</div>', unsafe_allow_html=True)
with st.container():
    # st.markdown('<div class="selected-movie-container">', unsafe_allow_html=True)
    st.markdown(
        f"""
        <div style="text-align: center;">
        <a href="./movie_details?movie_id={selected_movie_id}" target="_self">
            <img src="{selected_movie_poster}" style="width: 50%; border-radius: 12px; margin-bottom: 15px;" />
        </a>
        <p style="font-weight: 700; font-size: 22px; margin-top: 0; color:#f0f2f5;">{selected_movie_name}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

# Recommend Button and Output
st.markdown('<div class="section-header">Recommended Movies</div>', unsafe_allow_html=True)

if st.button("🎯 Recommend Similar Movies"):
    names, posters, ids = recommend(selected_movie_name)

    # Container for recommendations with padding
    with st.container():
        # First row
        cols1 = st.columns(5)
        for i in range(5):
            with cols1[i]:
                st.markdown(f"""
                <a href="./movie_details?movie_id={ids[i]}" target="_self">
                    <img src="{posters[i]}" style="width: 100%; border-radius: 10px;" />
                </a>
                """,
                    unsafe_allow_html=True
                )

                st.markdown(f'<div class="movie-title">{names[i]}</div>', unsafe_allow_html=True)

        st.markdown('<div style="margin-bottom: 50px;"></div>', unsafe_allow_html=True)  # spacer between rows

        # Second row
        cols2 = st.columns(5)
        for i in range(5, 10):
            with cols2[i - 5]:
                st.markdown(f"""
                <a href="./movie_details?movie_id={ids[i]}" target="_self">
                    <img src="{posters[i]}" style="width: 100%; border-radius: 10px;" />
                </a>
                """,
                    unsafe_allow_html=True
                )
                st.markdown(f'<div class="movie-title">{names[i]}</div>', unsafe_allow_html=True)

        st.markdown('<div style="margin-bottom: 50px;"></div>', unsafe_allow_html=True)  # spacer between rows

        # Third row
        cols3 = st.columns(5)
        for i in range(10, 15):
            with cols3[i - 10]:
                st.markdown(f"""
                <a href="./movie_details?movie_id={ids[i]}" target="_self">
                    <img src="{posters[i]}" style="width: 100%; border-radius: 10px;" />
                </a>
                """,
                    unsafe_allow_html=True
                )
                st.markdown(f'<div class="movie-title">{names[i]}</div>', unsafe_allow_html=True)

