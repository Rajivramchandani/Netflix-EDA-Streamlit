import streamlit as st 
import homepage
import recommendation
import distribution_of_content
import evolution_of_content
import unique_stratergies


import streamlit as st
PAGES = {
    "Home": homepage,
    "Distribution of Content": distribution_of_content,
    "Evolution of Content": evolution_of_content,
    "Unique Stratergies":unique_stratergies,
    "Recommendation": recommendation
}


def main():
    st.sidebar.title("Navigate yourself...")
    menu_selection = st.sidebar.radio("Choice your option...", list(PAGES.keys()))

    menu = PAGES[menu_selection]

    with st.spinner(f"Loading ..."):
        menu.app()


    st.sidebar.info("Rajiv Ramchandani (17070122053) and  Riya Chaudhary (17070122056)" )

if __name__ == "__main__":
    main()


# st.sidebar.title('Navigation')
# selection = st.sidebar.radio("Go to", list(PAGES.keys()))
# page = PAGES[selection]
# page.app()

# df = pd.read_csv('archive/netflix_titles.csv' )

# st.dataframe(df)

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
#                   font_size=18)
# st.plotly_chart(fig)