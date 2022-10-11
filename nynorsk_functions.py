import streamlit as st
from PIL import Image
import common_functions

logo = Image.open(r'images\logo_edc.png')
picture = Image.open(r'images\elin.png')


def main_method():
    col1, col2 = st.columns([0.8, 1.5])
    with col1:
        st.image(logo, width=250)
    with col2:
        common_functions.site_title("Språkvask og Korrektur")
    st.markdown('<hr style="height:2px;width:100%;border-width:10;color:blue;background-color:#1c2833">',
                unsafe_allow_html=True)
    st.write('#')

    common_functions.subheader('Norsk – begge målformer 📖')
    st.markdown(
        '<p class="font"style="font-family:Times New Roman;font-size:20px;color: #273746">Eg tek oppdrag både på '
        'bokmål og nynorsk.</p>',
        unsafe_allow_html=True)

    st.write('#')

    common_functions.subheader("Teksttypar 📚")

    st.markdown("""
        <style
            type="text/css">
            li { color: #273746;}
            ul { list-style-type: '✽ '; }
        </style>
        <ul>
            <li><p class="font"style="font-family:Times New Roman;font-size:20px;color: #273746">Artiklar (alle lengder) – 
                    både vitskaplege og anna</p></li>
            <li><p class="font"style="font-family:Times New Roman;font-size:20px;color: '
                    '#273746">Masteroppgåver</p></li>
            <li><p class="font"style="font-family:Times New Roman;font-size:20px;color: '
                    '#273746">Doktorgradsavhandlingar</p></li>
            <li><p class="font"style="font-family:Times New Roman;font-size:20px;color: #273746">Bøker</p></li>
            <li><p class="font"style="font-family:Times New Roman;font-size:20px;color: #273746">Andre tekstar</p></li>
        </ul>

    """, unsafe_allow_html=True)


def method_ommeg():
    col1, col2 = st.columns([0.8, 0.4])
    with col1:  # To display the header text using css style
        st.markdown(""" <style> .font {
                font-size:30px ; font-family: 'Times New Roman'; color: #2c3e50;} 
                </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font"style="font-family:Times New Roman;">Elin D. Chelighem</p>', unsafe_allow_html=True)
        st.write('#')
        with col2:  # To display brand log
            st.image(picture, width=250)
        st.markdown('<p style="font-family:Times New Roman;font-size:20px;color: #273746">Norsklærar med lidenskap '
                    'for godt, tydeleg og korrekt språk.</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family:Times New Roman;font-size:20px;color: #273746">Har språkvaska akademiske '
                    'tekstar frå 2005.</p>',
                    unsafe_allow_html=True)


def kontakt():
    st.write('#')
    st.markdown('<p style="font-family:Times New Roman;font-size:22px;color: #273746">'
                'Treng du språkvask eller korrektur?</p>', unsafe_allow_html=True)

    st.markdown('<p style="font-family:Times New Roman;font-size:22px;color: #273746">'
                'Send ein e-post, så sender eg eit kostnadsoverslag.</p>', unsafe_allow_html=True)

    st.markdown('<hr style="height:2px;width:100%;border-width:10;color:blue;background-color:#1c2833">',
                unsafe_allow_html=True)

    common_functions.change_header_kontakt("Kontakt meg! 👉 📬 ")
    st.write('#')

    contact_form = """
                <form action="https://formsubmit.co/0d93a5cadb13d41eabbc7206e0136813" method="POST">
                        <input type="hidden" name="_captcha" value="false">
                        <input type="text" name="name" style="font-family:'Times New Roman';font-size:20px;" placeholder="Ditt navn" required>
                        <input type="email" name="email" style="font-family:'Times New Roman';font-size:20px;" placeholder="Din epost" required>
                        <textarea name="message" style="font-family:'Times New Roman';font-size:20px;" placeholder="Din melding her" required></textarea>
                        <button type="submit" value="Submit" style="font-family:'Times New Roman';font-size:20px;" id = "sendButton">Send</button>
                </form>    
                """
    st.markdown(contact_form, unsafe_allow_html=True)

    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("style/style_nn.css")
