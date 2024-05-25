import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Somikoron | Recommendation Engine",
    layout="wide",
    initial_sidebar_state="auto",
)

# # Logo image URL
# logo_url = "https://i.postimg.cc/26jFTyb0/logo.jpg"

# # Header content
# header_html = f"""
# <div style="display: flex; align-items: center;">
#     <img src="{logo_url}" alt="Logo" style="width: 50px; height: 50px; margin-right: 10px;">
# </div>
# """
# # Render the header using the markdown method
# st.markdown(header_html, unsafe_allow_html=True)



def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css("styles.css")


# header
st.markdown('<div id="head"><h1 class="head_h1">SOMIKORON\'S Recommendation Engine</h1></div>', unsafe_allow_html=True)

# subhead
subhead_html="""
<div id="subhead">
    We are here to make your next read effortless and help you embark on a literary journey tailored to your taste
</div>
"""
st.markdown(subhead_html, unsafe_allow_html=True)


# Display search results (if any)
search_bar_html = """
<div class="search-container">
    <input type="text" id="search-input" class="search-input" placeholder="Search Book or Author name in Bangla...">
    <button onclick="submitSearch()" class="search-button">Search</button>
</div>

"""
# Render the HTML in Streamlit
st.markdown(search_bar_html, unsafe_allow_html=True)

name_html="""
<div id="name"><h4>Books Similar to "আমার ছেলেবেলা"</h4></div>
"""
st.markdown(name_html,unsafe_allow_html=True)

cards_html = """
<div class="card-container">
    <div class="card">
        <img src="https://i.postimg.cc/445jJHQx/amar-chelebela.jpg" alt="Book image">
        <div class="card-content">
            <div class="card-author">হুমায়ূন আহমেদ</div>
            <div class="card-title">আমার ছেলেবেলা</div>
        </div>
    </div>
    <div class="card">
        <img src="https://i.postimg.cc/zvVwZQkW/image.jpg" alt="Book image">
        <div class="card-content">
            <div class="card-author">হুমায়ূন আহমেদ</div>
            <div class="card-title">আপনারে আমি খুঁজিয়া বেড়াই</div>
        </div>
    </div>
    <div class="card">
        <img src=https://i.postimg.cc/qqSskGmF/image.jpg" alt="Book image">
        <div class="card-content">
            <div class="card-author">হুমায়ূন আহমেদ</div>
            <div class="card-title">আমার আপন আঁধার </div>
        </div>
    </div>
    <div class="card">
        <img src="https://i.postimg.cc/h45bbSS0/image.jpg" alt="Book image">
        <div class="card-content">
            <div class="card-author">হুমায়ূন আহমেদ</div>
            <div class="card-title">অনন্ত অম্বরে</div>
        </div>
    </div>
    <div class="card">
        <img src="https://i.postimg.cc/GmkFCGvM/image.jpg" alt="Book image">
        <div class="card-content">
            <div class="card-author">তসলিমা নাসরিন</div>
            <div class="card-title">নেই, কিছু নেই </div>
        </div>
    </div>
</div>
"""

# Render the HTML in Streamlit
st.markdown(cards_html, unsafe_allow_html=True)


marque_html = """
<marquee class = "marquee" behavior="scroll" direction="left">
Our recommendation engine is currently focused only on research and development, not for commercial book sales.</marquee>
"""
st.markdown(marque_html, unsafe_allow_html=True)


# footer
st.markdown('<footer><address id="footer">Developed by <i>MD MONJURUL ISLAM RIFAT</i></address></footer>', unsafe_allow_html=True) # type: ignore