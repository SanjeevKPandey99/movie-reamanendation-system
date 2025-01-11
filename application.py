import streamlit as st
import pickle 


movie = pickle.load(open("movies_list.pkl","rb"))
similarity = pickle.load(open("similarity.pkl","rb"))

def recommanded_movies(movies):
    index = movie[movie["title"] == movies].index[0]

    distances = sorted(list(enumerate(similarity[index])), reverse = True, key = lambda x : x[1])
    movies_l = []
    for i in distances[1 : 6]:
        print(movie.loc[i[0]]["title"])
        movies_l.append(movie.loc[i[0]]["title"])
    return movies_l



st.title("Movies Recommandation System")

movie_titles = movie["title"].values
selected_movies =st.selectbox(
    "Select a movie to get recommandation",
    movie_titles
)

if st.button("Get Recommandation"):
    recom_movie = recommanded_movies(selected_movies)
    # st.write(selected_movies)
    for i in recom_movie:
        st.write(i)