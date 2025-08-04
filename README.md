# 🎬 Movie Recommender System

A beautiful, responsive, and interactive **Movie Recommender Web App** built using **Streamlit**, powered by **content-based filtering** using movie similarity.

![App Screenshot](https://image.tmdb.org/t/p/w500/your_example_poster_path.jpg) <!-- Replace with actual poster or screenshot -->

---

## 🚀 Features

- 🔍 Search and select a movie to get 15 similar recommendations.
- 🖼️ Each recommendation is clickable and links to a **detailed movie info page**.
- 🎞️ Movie details include: poster, overview, director, rating, release date, genre, and runtime.
- 🎯 Built using **TMDb API** and **precomputed cosine similarity**.
- 💡 Clean, responsive UI with animated hover effects.

---

## 🛠️ Tech Stack

| Component | Tech |
|----------|------|
| Web Framework | [Streamlit](https://streamlit.io) |
| Backend | Python |
| Data Source | [TMDb API](https://www.themoviedb.org/documentation/api) |
| Styling | HTML + CSS (within Streamlit) |
| Environment | `python-dotenv` for API key security |
| Model | Precomputed similarity matrix (cosine similarity) |

---

## 📁 Project Structure

```bash
Movie_recommender_system/
│
├── .env                     # TMDB_API_KEY stored securely
├── Main.py                 # Main app interface (movie recommender UI)
├── pages/
│   └── movie_details.py    # Dynamic movie details page
├── similarity.pkl          # Precomputed similarity matrix (content-based filtering)
├── movies.pkl              # Movie dataset with title and ID
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
