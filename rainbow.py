import streamlit as st
import random

st.set_page_config(page_title="Birthday Wishes", page_icon="🎂", layout="wide")

background_image_url = "https://images.unsplash.com/photo-1504196606672-aef5c9cefc92?auto=format&fit=crop&w=1650&q=80"

# Inject CSS for background and animation
st.markdown(
    f"""
    <style>
    body {{
        background-image: url('{background_image_url}');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        overflow-x: hidden;
    }}

    @keyframes floatZigZag {{
        0% {{
            transform: translate(0, 0) scale(1);
            opacity: 1;
        }}
        25% {{
            transform: translate(-30px, -25vh) scale(1.1);
        }}
        50% {{
            transform: translate(30px, -50vh) scale(1.2);
        }}
        75% {{
            transform: translate(-15px, -75vh) scale(1.3);
        }}
        100% {{
            transform: translate(15px, -100vh) scale(1.5);
            opacity: 0;
        }}
    }}

    .heart {{
        color: red;
        position: fixed;
        bottom: -60px;
        animation-name: floatZigZag;
        animation-iteration-count: infinite;
        animation-timing-function: ease-in;
        opacity: 0.9;
        z-index: 1000;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Happy Birthday Girl ❤️🎉")
st.markdown(
    """ 
    ### 💌 Wishing you endless love and happiness on your special day!

    Click the button below to send a *magical heart shower*! ❤️
    """
)

# Generate multiple hearts with random size, duration, position, and delay
if st.button("Send Magical Heart Shower 💖"):
    hearts_html = ""
    for i in range(20):
        left = random.randint(5, 95)  # percent
        size = random.randint(30, 80)  # px
        duration = round(random.uniform(3, 7), 2)  # seconds
        delay = round(random.uniform(0, 3), 2)  # seconds
        hearts_html += f"""
        <div class="heart" style="
            left: {left}%;
            font-size: {size}px;
            animation-duration: {duration}s;
            animation-delay: {delay}s;">
            ❤️
        </div>
        """
    st.markdown(hearts_html, unsafe_allow_html=True)

