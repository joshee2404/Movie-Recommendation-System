import streamlit as st
import pandas as pd
from Recommend import recommend, movies  # Import movies DataFrame

st.set_page_config(page_title="Movie Recommendation", page_icon="🎬")

st.title("🎬 Movie Recommendation System")
st.write("Select a movie you like and get similar movie suggestions!")


movie_list = movies['title'].tolist()
selected_movie = st.selectbox("Select a movie:", movie_list)


if st.button("Recommend"):
    recommended_movies = recommend(selected_movie)
    st.write("### Recommended Movies:")
    for i, movie in enumerate(recommended_movies, 1):
        st.write(f"{i}. {movie}")
