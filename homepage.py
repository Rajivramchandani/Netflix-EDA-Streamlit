import pandas as pd
import streamlit as st 
import plotly.graph_objects as go

import streamlit as st
def app():
    st.title('Lets look at the dataset:')    
    df = pd.read_csv('archive/netflix_titles.csv' )

    st.dataframe(df)

    # t1 = df.type.value_counts()

    # fig = go.Figure()
    # fig.add_pie(name='', 
    #             values=t1.values, 
    #             labels=t1.index, 
    #             text=t1.index,
    #             )
    # fig.update_layout(title={
    #                         'text':'Movie vs TV Show: Pie Chart',
    #                         },
    #                 font_size=18)
    # st.plotly_chart(fig)