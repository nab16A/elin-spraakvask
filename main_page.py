import streamlit as st
import bg_image
from streamlit_option_menu import option_menu
import nynorsk_functions
import bokmaal_functions

st.set_page_config(
    page_title="Språkvask og Korrektur",
    page_icon=":book:",
    layout="centered",
    initial_sidebar_state="expanded",
)
style = {"container": {"padding": "5!important", "background-color": "  #5dade2  "},
         "icon": {"color": "#273746", "font-size": "25px"},
         "nav-link": {"font-size": "20px", "text-align": "left", "margin": "0px",
                      "--hover-color": " #d5d8dc ", "font-family": "Times New Roman", },
         "nav-link-selected": {"background-color": "#a9cce3",
                               "font-family": "Times New Roman", "font-size": "20px", "color": "#273746"},
         }

# setting footer
st.markdown("""
  <style>
      MainMenu, header, footer {visibility: hidden}
      footer::after {
        content: 'Developed with ❤️ by ©CMN - 2022';
        #content: url(images/logo_edc_2.jpg);
        visibility: visible;
        display: block;
        #position: fixed;
        #background-color: #1c2833;
        padding-bottom: 1px;
        top: 0px;
        text-align: center;
        font-size: 16px;
        color:  #273746;
        width: 100%;
        font-family: "Times New Roman", Times, serif;
      }
  </style>
  """, unsafe_allow_html=True)

selected_nynorsk = ''
selected_bokmaal = ''

# Use a background image
bg_image.set_png_as_page_bg('images/bg_2.png')


# change the color and the dimension of sidebar
def change_sidebar():
    return st.markdown("""
            <style>
                [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
                    width: 250px;
                    background-image: linear-gradient( #5dade2 ,#2e7bcf);
                }
                [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
                    width: 250px;
                    margin-left: -500px;
                }
            </style>
            """, unsafe_allow_html=True)


def ny_norsk_page():
    global selected_nynorsk
    with st.sidebar:
        nynorsk = option_menu("Hovudmeny", ['Hovudside', 'Om meg', 'Kontakt'], key='1',
                              icons=['house', 'person lines fill', 'person-bounding-box'], menu_icon="app-indicator",
                              default_index=0,
                              styles=style,
                              )
        selected_nynorsk = nynorsk


def bokmaal_page():
    global selected_bokmaal
    with st.sidebar:
        bokmaal = option_menu("Hovedmeny", ['Hovedside', 'Om meg', 'Kontakt'], key='2',
                              icons=['house', 'person lines fill', 'person-bounding-box'], menu_icon="app-indicator",
                              default_index=0,
                              styles=style,
                              )
        selected_bokmaal = bokmaal


def main():
    page = st.sidebar.radio("vel/velg språk:", tuple(PAGES.keys()), format_func=str.capitalize)
    st.markdown("""
                <style>
                    div.row-widget.stRadio > div{
                    flex-direction:row;
                    #justify-content: center;
                    display:flex;
                    #margin-left: 35px;
                    #margin-right: 35px;
                    #background:  #e8daef ;
                    #background-color: green;
                    #font: italic 30px Times New Roman;
                    padding-bottom: 20px;
                    }
                    div.row-widget.stRadio > label{
                    #margin-left: 0px;
                    #margin-right: 10px;
                    #background:  #e8daef ;
                    #background-color: green;
                    font: 22px Times New Roman;
                    padding: 5px;
                    padding-bottom: 15px;
                    padding-left: 0px;
                    color: #2f89bf;
                    }
                    section.main> div:first-child {
                    padding-top: 0px;
                    padding-bottom: 50px;
                    }
                    section:not(.main)>div:first-child {
                    #padding-top: 50px;
                    }
                </style>""",
                unsafe_allow_html=True)
    PAGES[page]()
    if page == 'nynorsk':
        if selected_nynorsk == 'Hovudside':
            nynorsk_functions.main_method()
        elif selected_nynorsk == 'Om meg':
            nynorsk_functions.method_ommeg()
        else:
            nynorsk_functions.kontakt()
    else:
        if selected_bokmaal == 'Hovedside':
            bokmaal_functions.main_method()
        elif selected_bokmaal == 'Om meg':
            bokmaal_functions.method_ommeg()
        else:
            bokmaal_functions.kontakt()


PAGES = {
    "nynorsk": ny_norsk_page,
    "bokmål": bokmaal_page,
}

if __name__ == "__main__":
    # change_sidebar()
    main()
