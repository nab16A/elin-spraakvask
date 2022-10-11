import streamlit as st
import streamlit.components.v1 as components


# Background color and text color of a header/subheader
def subheader(url):
    # background-color:#a8def7;
    st.markdown(f'<p style="color:#2c3e50;font-size:24px;font-family:Times New Roman '
                f';border-radius:2%;font-weight:bold;width:40%;">{url}</p>',
                unsafe_allow_html=True)


def site_title(name):
    components.html(f"""<div style='font-size:40px;text-align:right;color:#273746'>
                            <b>{name}</b>
                            </div>
    """)


def change_header_kontakt(url):
    st.markdown(f'<p style="font-family:Times New Roman;font-size:40px;color: #273746;border-radius:2%;">{url}</p>',
                unsafe_allow_html=True)
