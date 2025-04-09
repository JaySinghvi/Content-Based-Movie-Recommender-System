# 🎬 Personalized Movie Recommender

A content-based movie recommendation system that suggests similar movies based on film metadata using machine learning and NLP techniques.

## 🚀 Overview

This project analyzes movie metadata (like genres, keywords, overview, etc.) to generate personalized movie recommendations. It uses TF-IDF vectorization and cosine similarity to match user-selected movies with similar ones. The frontend is powered by Streamlit, and real-time movie posters are fetched using the TMDB API.

👉 [View the complete project on GitHub](https://github.com/JaySinghvi/Content-Based-Movie-Recommender-System)

## 🧠 Methodology

- **Data Preprocessing**: Cleaned and merged metadata fields such as genres, keywords, and movie overviews.
- **Text Vectorization**: Applied TF-IDF using `scikit-learn` and performed NLP preprocessing with `NLTK`.
- **Similarity Matching**: Computed cosine similarity scores to recommend movies based on content features.
- **Streamlit App**: Developed an interactive Streamlit application for users to explore movie suggestions effortlessly.
- **API Integration**: Fetched real-time movie posters from the TMDB API for a dynamic user experience.

## 🛠️ Tech Stack

- Python  
- scikit-learn  
- NLTK  
- Pandas & NumPy  
- Streamlit  
- TMDB API

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/JaySinghvi/Content-Based-Movie-Recommender-System.git
   cd Content-Based-Movie-Recommender-System

