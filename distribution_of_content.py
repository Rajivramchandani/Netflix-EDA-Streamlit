import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import itertools
from collections import Counter
from plotly.offline import  iplot
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from streamlit.proto.Markdown_pb2 import Markdown
# plt.style.use('dark_background')

def app():
    st.title("Distribution of the content on Netflix")

    df = pd.read_csv('archive/netflix_titles.csv' )

    t1 = df.type.value_counts()

    fig = go.Figure()
    fig.add_pie(name='', 
                values=t1.values, 
                labels=t1.index, 
                text=t1.index,
                )
    fig.update_layout(title={'text':'Movie vs TV Shows',},
                    font_size=18)
    st.plotly_chart(fig)
    
    st.write("From the graph, it can be inferred that movies dominate over TV shows at around seventy percent of content on Netflix. One of the reasons for this disparity is the fact that it takes a longer time (multiple seasons) for TV shows to be deemed profitable which is substantially more than 1.5-2.5 hours of a movie. Many movies make far more in their first weekend than a TV series makes over several years, and pay off their production costs overnight. Hence, investing in licensing deals for movies vs TV shows differ greatly ")
  
  
    t2 = df.groupby(pd.to_datetime(df['date_added']).map(lambda x:x.year))['type'].agg('describe')
    t2['movies'] = t2.freq
    t2.drop(columns=['top', 'freq', 'unique'], inplace=True)
    t2['tv_shows'] = t2['count'] - t2.movies



    fig = go.Figure()
    fig.add_scatter(x=t2.index, 
                    y=t2.tv_shows, 
                    fill='tonexty',
                    name='TV Shows',
                    line_color='rgb(25,25,255)'
                )
    fig.add_scatter(x=t2.index, 
                    y=t2.movies, 
                    fill='tonexty',
                    name='Movies',
                    line_color='rgb(77,195,255)'
                )
    fig.add_scatter(x=t2.index, 
                    y=t2['count'], 
                    line_color='black', 
                    line_dash='dash',
                    opacity=.5,
                    name='Total',
                )
    fig.update_traces(mode='lines')
    fig.update_layout(title_text='New Content added over time',
                    title_font_size=24,
                    xaxis_title='Year',
                    yaxis_title='New Content added',
                    hovermode="x unified",xaxis_showgrid=False, 
                    yaxis_showgrid=False)
    st.plotly_chart(fig)
    st.write("The growth of Netflix can be contributed to two main factors-personalized movie recommendation system and shifting to streaming service. Netflix started with a basic rating system, based on Big Data and completely based on how good or bad a particular movie or show had been rated. These ratings were based on number of views, customer feedback, if videos were watched until the end and even IMDB ratings. They evolved their algorithm to an open source initiative because they understood that with more data and the technological knowledge of more people, the Netflix experience would become much better. Already in September 2009, a prize of $1M (called The Netflix Prize) was awarded to team ‘BellKor’s Pragmatic Chaos’ for improving Netflix’s recommendation model.")
    st.write("In the earlies of 2000, Netflix did effective modifications in monetizing process. Putting an end to the single rental structure, Netflix came up with a rising business model that included unlimited rentals for a flat fee with no due dates, no shipping fees, and handling fees. The subscribers here can rent a certain number of movies based on the package. If they want to access new movies they had to return the old ones. In 2013, Netflix started to develop their own production and shows, based on the analysis of their own customers’ data and produced a massively successful show called 'House of Cards'.")
    st.write("There is a sharp increase in the number of movies and TV shows added from 2015. This was the time when Netflix started to produce high quality original content which cut licensing costs and attracted big personalities like Barack Obama, Indian directors like Zoya Akhtar, Karan Johar to produce work in various genres. At the same time, they had expanded to over 190 countries by 2018 by producing regional content and lauching local talent. ")
    st.write("The growth of Netflix can be contributed to two main factors-personalized movie recommendation system and shifting to streaming service. Netflix started with a basic rating system, based on Big Data and completely based on how good or bad a particular movie or show had been rated. These ratings were based on number of views, customer feedback, if videos were watched until the end and even IMDB ratings. They evolved their algorithm to an open source initiative because they understood that with more data and the technological knowledge of more people, the Netflix experience would become much better. Already in September 2009, a prize of $1M (called The Netflix Prize) was awarded to team ‘BellKor’s Pragmatic Chaos’ for improving Netflix’s recommendation model.")
    st.write("In the earlies of 2000, Netflix did effective modifications in monetizing process. Putting an end to the single rental structure, Netflix came up with a rising business model that included unlimited rentals for a flat fee with no due dates, no shipping fees, and handling fees. The subscribers here can rent a certain number of movies based on the package. If they want to access new movies they had to return the old ones. In 2013, Netflix started to develop their own production and shows, based on the analysis of their own customers’ data and produced a massively successful show called 'House of Cards'.")
    st.write("There is a sharp increase in the number of movies and TV shows added from 2015. This was the time when Netflix started to produce high quality original content which cut licensing costs and attracted big personalities like Barack Obama, Indian directors like Zoya Akhtar, Karan Johar to produce work in various genres. At the same time, they had expanded to over 190 countries by 2018 by producing regional content and lauching local talent. ")
    
    
    list_cats = df.listed_in.str.split(', ').tolist()
    flatten = itertools.chain.from_iterable(list_cats)
    cats_counter = dict(Counter(flatten))
    cats_counter = {k:v for k,v in sorted(cats_counter.items(), key=lambda e:e[1], reverse=True)}
    cat_list = list(cats_counter.keys())[:10][::-1]
    num_list = list(cats_counter.values())[:10][::-1]


    fig = go.Figure()
    fig.add_bar(x=num_list,
                y=cat_list,
                orientation='h',
                hovertemplate='Category: %{y}<br>Total: %{x}',
                name='')
    fig.update_layout(title_text='Top 10 Categories',
                    title_font_size=24,
                    xaxis_title_text='Total')
    st.plotly_chart(fig)

    films_genres = pd.DataFrame(columns = ['genre', 'count'], index = range(7))
    films_genres.iloc[0, 0] = 'Dramas'
    films_genres.iloc[0, 1] = df.listed_in.str.contains('Dramas').sum()
    films_genres.iloc[1, 0] = 'Comedies'
    films_genres.iloc[1, 1] = df.listed_in.str.contains('Comedies').sum()
    films_genres.iloc[2, 0] = 'Action & Adventure'
    films_genres.iloc[2, 1] =  df.listed_in.str.contains('Action & Adventure').sum()
    films_genres.iloc[3, 0] = 'Documentaries'
    films_genres.iloc[3, 1] =  df.listed_in.str.contains('Documentaries').sum()
    films_genres.iloc[4, 0] = 'Thrillers'
    films_genres.iloc[4, 1] = df.listed_in.str.contains('Thrillers').sum()
    films_genres.iloc[5, 0] = 'Horror Movies'
    films_genres.iloc[5, 1] =  df.listed_in.str.contains('Horror Movies').sum()
    films_genres.iloc[6, 0] = 'Sci-Fi & Fantasy'
    films_genres.iloc[6, 1] =  df.listed_in.str.contains('Sci-Fi & Fantasy').sum()

    fig = px.pie(labels = films_genres['genre'], values = films_genres['count'], names = films_genres['genre'])
    fig.update_traces(textposition = 'inside', 
                    textinfo = 'percent + label',)

    fig.update_layout(annotations = [dict(text = 'Distribution of genres', 
                                        x = 0.5, y = 1.15, font_size = 24, showarrow = False, 
                    
                                        )],
                    showlegend = False)
                    
    st.plotly_chart(fig)
    st.write("The above trend of the most popular genre topped by drama, followed by comedy can be explained by the audience Netflix actively seeks which are the adults and young adults age group. Drama encompasses a variety of mediums from TV shows to anime and can be an mentally immersive experience with disparate themes, riveting storytelling and cultural exposure. ")
    st.write("The second spot is taken by comedy at around 26% which can serve as a cleansing thought freshner and a departure from the harsh realities of life. Another good reason for its popularity is that this genre can be enjoyed by a large variety of audience from all age groups.")
    st.write("Both of these genres can be curated to celebrate a specific season, holiday or even person. Adventure and action and documentaries are next on the list and require more dedication both financially and manually to prepare and usually target a more compact audience. ")
    st.write("Lastly, thrillers, horror movies and fantasy shows are season specific and need a longer time to estalish a connect with its intended audiences. Most of the projects in these categories are an attempt to remake past movies and shows and enjoy a lesser appreciation than its former counterparts. ")
    

    
    fig = plt.figure(figsize=(15,7))
    sns.countplot(y='rating', data=df, order=df.rating.value_counts().index.to_list(), color='Blue')
    plt.title('Overall Distribution of Ratings', fontsize=24);
    st.pyplot(fig)
    

    
    df['age_group'] = df['rating']
    MR_age = {'TV-MA': 'Adults',
            'R': 'Adults',
            'PG-13': 'Teens',
            'TV-14': 'Young Adults',
            'TV-PG': 'Older Kids',
            'NR': 'Adults',
            'TV-G': 'Kids',
            'TV-Y': 'Kids',
            'TV-Y7': 'Older Kids',
            'PG': 'Older Kids',
            'G': 'Kids',
            'NC-17': 'Adults',
            'TV-Y7-FV': 'Older Kids',
            'UR': 'Adults'}
    df['age_group'] = df['age_group'].map(MR_age)

    val = df['age_group'].value_counts().index
    cnt = df['age_group'].value_counts().values

    fig = go.Figure([go.Bar(x=val, y=cnt, marker_color='blue')])
    fig.update_layout(title_text='Age Group Distribution', title_x=0.5)
    st.plotly_chart(fig)
    st.markdown(" The graph illustrates the age demographic that consumes Netflix content and adults make up about 46 percent of all users followed by young adults at 24 percent. This result is also in accordance with the popularity and production trend in content on Netflix with the likes of mature, outlandish and bold projects that were traditionally avoided and looked down upon.")

    df['country'] = df['country'].fillna('Other')
    df['country'].isna().sum()
    df['main_country'] = df['country'].apply(lambda x: x.split(',')[0])
    df.drop('country',axis=1, inplace=True)


    count = df.groupby(['main_country']).count()
    most_country = count['type'].to_frame().reset_index().sort_values(by='type', ascending=False)[:10]

    fig = plt.figure(figsize=(15,7))
    sns.barplot(x='main_country', y='type', data=most_country,palette='Set1')
    plt.ylabel('TV and Movies')
    plt.xlabel('Country')
    plt.title("Country wise count of Shows and Movies production (top 10)",fontsize = 24)
    st.pyplot(fig)
    st.write("USA is home to Netflix and has the largest content library. From its initial start as a movie rental company that eliminated various restrictions on users like late fees and physical pickups, it picked up pace in 2007 when it began online streaming, garnering more customers every day. ")
    st.write("In India, Netflix competes with the likes of Disney, Amazon, Hotstar and over 30 additional services. Thanks to Reliance Jio and its cheap data plans, India went from being one of the world’s most expensive data regimes to the most inexpensive in just four years. Unlike Americans and Europeans, a large chunk of Indians consume content on mobile devices. To reach these consumers, Netflix launched a mobile-only subscription plan at ₹199 a month, far cheaper than its standard plan, in 2019. On the back end, it had to adjust the bit rate of videos based on factors such as the speed of the Internet connection and the device to ensure a seamless experience. Netflix uped its game by creating regional content with local talent producing Emmy winner Delhi Crime andd crowd pleasing Sacred Games. Furthermore, Netflix has also forged strategic partnerships with telecom major Reliance Jio, Internet service providers such as Hathway and ACT Fibernet, and device brands like Samsung, OnePlus, and Mi to reach the almost 500 million smartphone users.")
    st.write("The United Kingdom was Netflix’s second international market launch in 2012 following Canada in 2010. Netflix added a record 37 million new subscribers in UK as lockdown prompted viewers to alleviate housebound cabin fever with fare including The Crown, Bridgerton and The Queen’s Gambit.")
    st.image('county_distribution.png')
    st.write("Netflix has 73.94 million paying subscribers based in the US & Canada. Netflix’s user base in the US & Canada accounts for a 36.3% share of global Netflix subscribers.")
    st.write("Netflix has 66.7 million paying subscribers based in Europe, the Middle East, and Africa. 32.75% of worldwide Netflix paying members are based in the EMEA region.")
    st.write("In Asia, 25.49 million digital streaming subscribers pay for a Netflix membership. 12.52% of Netflix global subscribers are based in the Asia-Pacific region.")
    st.write("For globalization, Netflix faced several challenges. Netflix must secure content deals region by region, and sometimes country by country. It also must face a diverse set of national regulatory restrictions, such as those that limit what content can be made available in local markets. International subscribers, many of whom are not fluent in English, often prefer local-language programming. And many potential subscribers, accustomed to free content, remain hesitant to pay for streaming services at all. Furthermore, strong competition in streaming already exists in many countries.")
    st.write("Netflix’s success can be attributed to two strategic moves — a three-stage expansion process into new markets and the ways it worked with those markets — which other companies looking to expand globally can use too.")
    st.write("Netflix did not try to enter all markets at once. Rather, it carefully selected its initial adjacent markets in terms of geography and psychic distance, or perceived differences between markets. For example, its earliest international expansion, in 2010, was to Canada, which is geographically close to and shares many similarities with the United States. Netflix was thus able to develop its internationalization capabilities in locations where the challenges of “foreignness” were less acute. In doing so, the company learned how to expand and enhance its core capabilities beyond its home market.")
    st.write("The next phase involved expanding into more-distant markets, it was supported by investments in content geared toward the preferences of those geographies, as well as technological investments in big data and analytics.")
    st.write("In the final phase, Netflix focused on adding more languages (including for subtitles), optimizing its personalization algorithms for a global library of content, and expanding its support for a range of device, operation, and payment partnerships.Netflix also began placing a greater emphasis on improving its mobile experience, including sign-ups, credentials and authentication, the user interface, and streaming efficiency for cellular networks. ")
    st.write("To address the protracted process of signing content deals with major studios on a regional or local basis, it has increasingly pursued global licensing deals so that it can provide content across all of its markets at once. Netflix has also begun to source regionally produced content, providing a win-win for these producers, whose local content can find a global audience.")
    st.markdown("**In this way, Netflix has been able to expand its reach to around 190 country in a small period of time.**")
 