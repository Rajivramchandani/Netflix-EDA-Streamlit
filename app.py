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
    st.sidebar.title("Netflix EDA")
    menu_selection = st.sidebar.radio("Browse Topics:", list(PAGES.keys()))

    menu = PAGES[menu_selection]

    with st.spinner(f"Loading ..."):
        menu.app()


    st.sidebar.info("Made by :" )
    st.sidebar.info("Rajiv Ramchandani" )
    st.sidebar.info("Riya Chaudhary" )



if __name__ == "__main__":
    main()
