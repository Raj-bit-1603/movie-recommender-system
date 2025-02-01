import pandas as pd
import streamlit as st
import pickle
import requests  #hit the api by posture

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=ab2b88d532b399134d1136c7589e7789&%20language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommanded(movie):  #this function show a similar movie name.
  movie_index = movies[movies['title'] == movie].index[0] #they will show a index of similar movie
  distances = cousine_similarity[movie_index] # then it will check a distance of the movie.
  movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6] #sort the movie in reverse order

  recommanded_movie =  []
  recommanded_movie_poster = []
  for i in movies_list:
    movie_id = movies.iloc[i[0]].id   #fetch the posture by id of movie API.

    recommanded_movie.append(movies.iloc[i[0]].title)
    recommanded_movie_poster.append(fetch_poster(movie_id))
  return  recommanded_movie,recommanded_movie_poster


movies_dict = pickle.load(open('movie_dict.pkl','rb'))  #rb = read binary mode
movies = pd.DataFrame(movies_dict)

cousine_similarity = pickle.load(open('similarity.pkl','rb'))
st.title("Movie Recommander System")  #title of the website

selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    (movies['title'].values)
)

st.button("Recommend") #button
name,postures = recommanded(selected_movie_name) #created a function name recomanded.
col1,col2,col3, col4,col5 = st.columns(5)
with col1:
    st.text(name[0])
    st.image(postures[0])
with col2:
    st.text(name[1])
    st.image(postures[1])
with col3:
    st.text(name[2])
    st.image(postures[2])
with col4:
    st.text(name[3])
    st.image(postures[3])
with col5:
    st.text(name[4])
    st.image(postures[4])