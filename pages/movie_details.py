import streamlit as st
import requests
from dotenv import load_dotenv
import os


load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

def fetch_MovieDetails(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&append_to_response=credits"
    resp = requests.get(url)
    if resp.status_code != 200:
        return {}
    data = resp.json()
    directors = [p['name'] for p in data.get('credits', {}).get('crew', []) if p['job'] == 'Director']
    data['directors'] = directors
    return data

# Retrieve movie_id from query parameters
params = st.query_params
movie_id = params.get("movie_id", None) 

if movie_id is None:
    st.error("No movie ID provided.")
else:
    details = fetch_MovieDetails(movie_id)
    if not details:
        st.error("Failed to fetch movie details.")
    else:
        st.title(details.get('title', 'N/A'))
        poster_url = "https://image.tmdb.org/t/p/w500/" + details.get('poster_path', '') if details.get('poster_path') else None
        if poster_url:
            st.image(poster_url, use_container_width=True)
        st.write(f"**Director(s):** {', '.join(details.get('directors', ['N/A']))}")
        st.write(f"**Release Date:** {details.get('release_date', 'N/A')}")
        st.write(f"**Rating:** {details.get('vote_average', 'N/A')} / 10")
        st.write(f"**Runtime:** {details.get('runtime', 'N/A')} minutes")
        genres = details.get('genres', [])
        st.write(f"**Genres:** {', '.join([g['name'] for g in genres]) if genres else 'N/A'}")      
        st.write("**Overview:**")
        st.write(details.get('overview', 'No overview available.'))

    if st.button("🔙 Back to Recommender"):
        st.switch_page("Main.py")  # Only works in newer Streamlit versions

