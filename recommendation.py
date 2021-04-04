import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords  
stop_words= stopwords.words('english')


def app():
    st.title("Recommendation model using Cosine Similarity")

    df = pd.read_csv('archive/netflix_titles.csv')

    df['cast']=df['cast'].fillna('Unknown')
    df['director']=df['director'].fillna('Unknown')
    #combining all fields which will be used for recomendation
    df['CombinedField']=df['cast']+' '+df['director']+' '+df['listed_in']+' '+df['description']
    modifiedCOrpus=[]


    #tokenizing all words.
    corpus = df['CombinedField'].apply(lambda x:word_tokenize(x))
    listcorpus = list(corpus)
    modifiedCOrpus = []
    #pre processing words, by lowering it, removing symbolls and removing stop words
    for desc in listcorpus:
        stmt = []
        for i in desc:
            if i.lower() not in  stop_words:
                if i.lower() not in ['.',',','â€',':','""']:
                    stmt.append(i.lower())
        modifiedCOrpus.append(' '.join(stmt))
        
    tfdifVect = TfidfVectorizer(stop_words='english',lowercase=True)
    corpus = modifiedCOrpus
    tfdifCorpus = tfdifVect.fit_transform(corpus)

    cossineSim = cosine_similarity(tfdifCorpus,tfdifCorpus)
    def get_recommendations(title):
        indices = pd.Series(df.index, index=df['title']).drop_duplicates()
        try:
            idx = indices[title]
            # Get the pairwsie similarity scores of all movies with that movie
            sim_scores = list(enumerate(cossineSim[idx]))
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            # Get the scores of the 10 most similar movies
            sim_scores = sim_scores[1:11]
            movie_indices = [i[0] for i in sim_scores]
            st.write(df.loc[movie_indices])
        except:
            st.write('No such movie found')
        
    user_input = st.text_input("label goes here",)
    st.write("Recommendations: ")
    if (user_input):
     get_recommendations(user_input)