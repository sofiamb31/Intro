import streamlit as st
from PIL import Image

st.title(" Mi Primera App Sofi")

st.header("Bingo")
st.write("Yo soy Bingo, Bingo soy yo")
image = Image.open('bingo.jpg')

st.image(image, caption= 'te quiero mucho bingo')


texto = st.text_input('Esta es mi primera app' , 'la estoy haciendo de bingo')
st.write('El texto escrito es', texto)
