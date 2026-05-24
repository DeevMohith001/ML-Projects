import streamlit as st
import pickle

movies_list = pickle.load(open('"C:/Users/lenovo/Machine Learning Projects/Movie Recommender System/movies.pkl"', 'rb'))
movies_list = movies_list['title'].values
st.title('Movie Recommendation System')

option = st.selectbox(
    'How would you like  to contacted?',
    movies_list
)