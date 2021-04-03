import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import itertools
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from plotly.offline import init_notebook_mode, iplot, plot
import streamlit as st


def app():
    df =  pd.read_csv('archive/netflix_titles.csv')
    df['date_added'] = df['date_added'].fillna('No data')
    df['month_added'] = df['date_added'].apply(lambda x: x.split(' ')[0])

    content_by_month = df.query('month_added != "No" & month_added != ""')\
    .groupby('month_added').agg({'type': 'count'}).reset_index()\
    .rename(columns = {'type': 'content'}).sort_values('content', ascending = False)

    
    fig = px.pie(names = content_by_month['month_added'],values=content_by_month['content'],color_discrete_sequence=px.colors.sequential.deep_r)

    st.plotly_chart(fig)
    
    
    df['country'].fillna('Other',inplace = True)

    df['main_country'] = df['country'].apply(lambda x: x.split(',')[0])

       
    country_order = df['main_country'].value_counts()[:11].index
    data_q2q3 = df[['type', 'main_country']].groupby('main_country')['type'].value_counts().unstack().loc[country_order]
    data_q2q3['sum'] = data_q2q3.sum(axis=1)
    data_q2q3_ratio = (data_q2q3.T / data_q2q3['sum']).T[['Movie', 'TV Show']].sort_values(by='Movie',ascending=False)[::-1]

    fig, ax = plt.subplots(1,1,figsize=(10, 7),)

    ax.barh(data_q2q3_ratio.index, data_q2q3_ratio['Movie'], 
            color='#ff002aff', alpha=0.8, label='Movie')
    ax.barh(data_q2q3_ratio.index, data_q2q3_ratio['TV Show'], left=data_q2q3_ratio['Movie'], 
            color='#1ee3e0', alpha=0.8, label='TV Show')
    plt.legend(loc="upper left")
    st.pyplot(fig)
    st.write("Interestingly, Netflix in India is made up nearly entirely of Movies. ")

    st.write("Bollywood is big business, and perhaps the main focus of this industry is Moviesand not TV Shows.")
    st.write("South Korean Netflix on the other hand is almost entirely TV Shows.")

    st.write("The underlying resons for the difference in content must be due to market research conducted by Netflix.")
    
    
    data_movie = df[df['type']== 'Movie']
    fig = go.Figure()
    fig.add_box(
        y = data_movie.duration,
        name = "Duration of Movies",
        marker_color='Red' )
    fig.update_layout(xaxis_showgrid=False, yaxis_showgrid=False) 
    fig.update_layout(xaxis_showgrid=False, yaxis_showgrid=False) 
    st.plotly_chart(fig)
