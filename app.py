import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=1a468fd0d6d83734121feb32692e6d79&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies_df[movies_df["title"] == movie].index[0]  # fetching the index of the movie
    distances = similarity[movie_index]  # similarity score
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]  # here we use enumerate becuase we also need to hold the index position so enumerate gives index position and score
    recommended_movie = []
    recommended_movie_posters =[]
    for i in movies_list:
        movie_id = movies_df.iloc[i[0]].id
        recommended_movie.append(movies_df.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id)) #fetching posters from TMDB API
        #fetching poster for each movie using TMDB API
    return recommended_movie, recommended_movie_posters
movies_list = pickle.load(open("movies_dict.pkl", "rb"))
movies_df = pd.DataFrame(movies_list)

similarity = pickle.load(open("similarity.pkl", "rb"))
#code to give title and a drop box to view and select/search for movies
st.title("Movie Recommender System")
selected_movies = st.selectbox(
    "Watch movies similiar to the ones you like!", movies_df["title"].values)

#to add a button
if st.button("Recommend"):
    name, posters = recommend(selected_movies)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(name[0])
        st.image(posters[0])
    with col2:
        st.text(name[1])
        st.image(posters[1])
    with col3:
        st.text(name[2])
        st.image(posters[2])
    with col4:
        st.text(name[3])
        st.image(posters[3])
    with col5:
        st.text(name[4])
        st.image(posters[4])