import pandas as pd
import streamlit as st 
import plotly.graph_objects as go

import streamlit as st
def app():
    st.image('Netflix_Logo_RGB.png')

    st.write("Netflix is an application that keeps growing bigger and faster with its popularity, shows and content. in this project we will explore the following:")
    st.write("1. What is the Distribution of content (Type, Genre, Age group and Geographically).")
    st.write("2. How has the content evolved throughout the years and a closer look at the trend of content in the USA and India.")
    st.write("3. What unique stratergies Netflix has implemented by doing market research and experimentation on their platform. ")
    st.write("4. A recommendation model using Cosine Similarity to give a list of recommendation using a given title's cast, director, genre and description")



   
    st.markdown('## Lets look at the dataset:')    

    st.write("The dataset consists of about 7000 entries of meta details about the movies and tv shows such as the title, director, and cast of the shows / movies. Details such as the release year, the rating, duration etc. ")
    df = pd.read_csv('archive/netflix_titles.csv' )
    st.dataframe(df)
