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
    st.title("Unique Stratergies Netflix uses")
    df =  pd.read_csv('archive/netflix_titles.csv')
    df['date_added'] = df['date_added'].fillna('No data')
    df['month_added'] = df['date_added'].apply(lambda x: x.split(' ')[0])

    content_by_month = df.query('month_added != "No" & month_added != ""')\
    .groupby('month_added').agg({'type': 'count'}).reset_index()\
    .rename(columns = {'type': 'content'}).sort_values('content', ascending = False)

    
    fig = px.pie(names = content_by_month['month_added'],values=content_by_month['content'],color_discrete_sequence=px.colors.sequential.deep_r)
    fig.update_layout(title={'text':'Distribution of content added across a year',},
                    font_size=18)
    st.plotly_chart(fig)
    st.write("Instead of releasing new shows and new seasons of shows randomly, Netflix does it strategically.")
    st.write("For instance, there is a surge of TV shows and movies released in October as halloween approaches. Look at the release of Stranger Things 2. In the U.S., the streaming service dropped all episodes on October 27, which happened to fall on a Friday. For the show’s creepy, ‘80s-monster-movie-adventure vibe, the weekend before Halloween was a perfect launch date. Plus, to make things more perfect, the show’s action in season 2 took place around Halloween.")
    st.write("November and December are full of festivities around the world with Thankgiving, Christmas and New years falling one after the other leading to a long vacation with ample of time to consume entertainment content. This can also be seen in the fact that the genre and style of the projects released in the last months of the year are specific to the season, less bold and holiday centric. January is also a month when people are willing to experiment with new things and most often these new obssessions fail, the artisitc medium is the only source of escapism and comfort.")
    st.write("New content is most often added in the early winter, and least often added in the summer.")

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
    plt.title("Split of Movies to TV Shows across countries",fontsize = 18)

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
        marker_color='#1ee3e0' )
    fig.update_layout(xaxis_showgrid=False, yaxis_showgrid=False) 
    fig.update_layout(xaxis_showgrid=False, yaxis_showgrid=False) 
    fig.update_layout(title={'text':'Box plot of frequency of duration of movies',},
                    font_size=18)
    st.plotly_chart(fig)
    

    fig = plt.figure(figsize= (10,7))
    tv_show = df[df['type']== 'TV Show']
    sns.countplot(y = 'duration',data = tv_show,color='#1ee3e0', order = tv_show['duration'].value_counts().index,orient='vertical')
    plt.xticks(rotation = 90)
    plt.xlabel("Seasons",fontsize = 12)
    plt.ylabel("Total count",fontsize = 12)
    plt.title("Total Tv Show Season wise",fontsize = 18)
    st.pyplot(fig)

    st.write("The trend seen here can be explained by the fact that the average attention span of the youth today has shrunken considerably and due to the fast paced nature of today, people are less willing to invest ")