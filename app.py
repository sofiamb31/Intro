import streamlit as st
from PIL import Image

st.title(" Mi Primera App Sofi")

st.header("Bingo")
st.write("Yo soy Bingo, Bingo soy yo")
image = Image.open('bingo.jpg')

st.image(image, caption= 'Interfaces multimodales')
