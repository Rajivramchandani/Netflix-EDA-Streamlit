import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
plt.style.use('dark_background')


def app():
    df = pd.read_csv('archive/netflix_titles.csv')
    df_temp = df[(df['type'] == 'Movie') & (df['release_year'] > 2008) ]
    movie_rating = df_temp.groupby(['release_year','rating']).size().reset_index(name = 'Total')

    fig = plt.figure(figsize = (15,7))
    # sns.set_style('darkgrid')
    sns.barplot(data = movie_rating,x = 'release_year', y = 'Total',hue = 'rating',palette = 'Set1')
    plt.title('Overall Movies released ratings',fontsize = 15)
    plt.xlabel('Year',fontsize = 15)
    plt.ylabel('No.of Shows',fontsize = 15)
    plt.legend(loc="upper left")
    st.pyplot(fig)
    
    

    df_temp = df[(df['type'] == 'TV Show') & (df['release_year'] > 2008) ]
    tv_rating = df_temp.groupby(['release_year','rating']).size().reset_index(name = 'Total')

    fig = plt.figure(figsize = (15,7))
    sns.barplot(data = tv_rating,x = 'release_year', y = 'Total',hue = 'rating',palette = 'Set1')
    plt.title('Overall TV Shows released ratings',fontsize = 15)
    plt.xlabel('Year',fontsize = 15)
    plt.ylabel('No.of Shows',fontsize = 15)
    plt.legend(loc="upper left")
    st.pyplot(fig)
    
    st.write("It comes as no shock to anyone with a Netflix subscription that much of the content featured on the video streaming service is decidedly not family friendly by any means. Well, the graphs above descibe the trend of the content on Netflix and we can see that a majority of shows and movies have a TV-MA (mature content) rating, followed by shows and movies with a TV-14 rating. Shockingly, a mere fraction of the content enjoys a G (general audience) rating.")
    st.write("Over 56 million Americans subscribe to Netflix, so these ratings are a good barometer of the kind of perverse content popular today for viewing. ")



    df_temp = df[(df['type'] == 'TV Show') & (df['country'] == 'India') ]
    india_tv = df_temp.groupby(['release_year','rating']).size().reset_index(name = 'Total')

    fig = plt.figure(figsize = (15,7))
    sns.barplot(data = india_tv,x = 'release_year', y = 'Total',hue = 'rating',palette = 'Set1')
    plt.title('TV shows released in India by ratings',fontsize = 15)
    plt.xlabel('Year',fontsize = 15)
    plt.ylabel('No.of Shows',fontsize = 15)
    plt.legend(loc="upper left")
    st.pyplot(fig)
    
    

    df_temp = df[(df['type'] == 'Movie') & (df['country'] == 'India') & (df['release_year'] > 2008)]
    india_movie = df_temp.groupby(['release_year','rating']).size().reset_index(name = 'Total')

    fig = plt.figure(figsize = (15,7))
    sns.barplot(data = india_movie,x = 'release_year', y = 'Total',hue = 'rating',palette = 'Set1')
    plt.title('Movies released in India by ratings',fontsize = 15)
    plt.xlabel('Year',fontsize = 15)
    plt.ylabel('No.of Shows',fontsize = 15)
    plt.legend(loc="upper left")
    st.pyplot(fig)
    
        
    df_temp = df[(df['type'] == 'TV Show') & (df['country'] == 'United States') & (df['release_year'] > 2008) ]
    usa_tv = df_temp.groupby(['release_year','rating']).size().reset_index(name = 'Total')

    fig = plt.figure(figsize = (15,7))
    sns.barplot(data = usa_tv,x = 'release_year', y = 'Total',hue = 'rating',palette = 'Set1')
    plt.title('TV shows released in the United States by ratings',fontsize = 15)
    plt.xlabel('Year',fontsize = 15)
    plt.ylabel('No.of Shows',fontsize = 15)
    plt.legend(loc="upper left")
    st.pyplot(fig)


        
    df_temp = df[(df['type'] == 'Movie') & (df['country'] == 'United States') & (df['release_year'] > 2008) ]
    usa_movie = df_temp.groupby(['release_year','rating']).size().reset_index(name = 'Total')

    fig = plt.figure(figsize = (15,7))
    sns.barplot(data = usa_movie,x = 'release_year', y = 'Total',hue = 'rating',palette = 'Set1')
    plt.title('Movies released in the United States by ratings',fontsize = 15)
    plt.xlabel('Year',fontsize = 15)
    plt.ylabel('No.of Shows',fontsize = 15)
    plt.legend(loc="upper left")
    st.pyplot(fig)
    
    
    fig = plt.figure(figsize = (15,7))
    df['date_added_year']=df['date_added'].str.split(', ', n = 1, expand = True)[1]
    df['date_added_year'].fillna(0,inplace=True)
    df['date_added_year'] = df['date_added_year'].astype('int64')
    df['release_year'] = df['release_year'].astype('int64')
    df['Original_Licence'] = df['release_year'] == df['date_added_year']
    d = {True :'Original', False:'Licence'}
    df['Original_Licence'] =df['Original_Licence'].map(d)

    #2008 is choose as release year filter, as first netflix show was release in 2009.
    pivot = df[df['release_year'] >2008].pivot_table('show_id',index='release_year',columns='Original_Licence',aggfunc='count',fill_value=0)
    fig = pivot.plot(kind='bar',figsize=(10, 5),color=['#1ee3e0','#ff002aff'])
    plt.grid(False)
    st.pyplot(fig.figure)
    st.write("From the graph, it can be inferred that from 2013 onwards Netflix started producing more original content and over time reduced the licensed and purchased counterpart. The number of original productions almost equals in 2018 and overtakes in the following year. ")
    st.write ("This move has come from the fact that despite nostalgic shows like 'The Office' and 'Friends' help in customer retention and avoids churn, these are contract based agreement over gargantuan prices and final negotiation rights over the makers of the show. Hence, it makes business sense to shift to home production and get unlimited access over the quality and extent of demographic reach as most of the licensed content is restricted certain region and time. ")
    st.write ("Also, 2013 was the year when the beloved show 'House of Cards' established the audiences evolving taste and departure from traditional storytelling techniques and medium. 2020 presented a great opportunity to the OTT platforms to expand their user base and Netflix was able to produce multiple shows and movies as well as acquire several rights over movies that would have released in theatres. ")


