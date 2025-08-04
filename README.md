# 🎬 Movie Recommender System

A beautiful, responsive, and interactive **Movie Recommender Web App** built using **Streamlit**, powered by **content-based filtering** using movie similarity.

![App Screenshot] <!-- Replace with actual poster or screenshot -->
<img width="1418" height="822" alt="Screenshot 2025-08-04 at 11 41 11 PM" src="https://github.com/user-attachments/assets/7220b11b-9e18-4521-ae76-941ccc18fdf7" />

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
```

## 🧑‍💻 Setup Instructions

### ✅ 1. Clone the Repository


git clone https://github.com/your-username/movie-recommender-system.git
cd movie-recommender-system

### ✅ 2. Create a Virtual Environment

python -m venv venv
source venv/bin/activate        # macOS/Linux
 OR
venv\Scripts\activate           # Windows

### ✅ 3. Install Dependencies

pip install -r requirements.txt

### ✅ 4. Add Your TMDb API Key

Create a .env file in the root directory with the following content:
TMDB_API_KEY=your_tmdb_api_key_here
🔐 Important: Keep your .env file private and don’t push it to GitHub.

### ✅ 5. Run the App

streamlit run Main.py



