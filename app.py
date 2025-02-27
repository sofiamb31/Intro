import streamlit as st
from PIL import Image

st.title(" Mi Primera App Sofi")

st.header("Bingo")
st.write("Yo soy Bingo, Bingo soy yo")
image = Image.open('bingo.jpg')

st.image(image, caption= 'te quiero mucho bingo')


texto = st.text_input('Esta es mi primera app' , 'la estoy haciendo de bingo')
st.write('El texto escrito es', texto)

st.subheader("Ahora usemos 2 columnas")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("Bingo mejora la experiencia del usuario viendo Bluey")
  resp = st.checkbox('Estoy de acuerdo')
  if resp:
    st.write('Yo tambien!')

with col2:
  st.subheader("Esta es la segunda columna")
  modo = st.radio("Que personaje de Bluey es tu favorito?" , ('Bluey' , 'Bingo' , 'Bandit'))
  if modo == 'Bluey':
    st.write('Bluey es el personaje principal y la hermana mayor')
  if modo == 'Bingo':
    st.write('Bingo es la hermana menor y la mas consentida')
  if modo == 'Bandit':
    st.write('Bandit es el papa mas cool del universo')

st.subheader("Uso de botones")
if st.button('Presiona el botón'):
  st.write('Gracias por presionar')
else:
  st.write('No has presionado aun')

st.subheader("Selectbox")
in_mod = st.selectbox(
  "Selecciona tu personaje",
  ("Bluey" , "Bingo" , "Bandit"),
)
if in_mod =="Bluey":
  set_mod = "Reproducir Bluey"
elif in_mod == "Bingo":
  set_mod = "Reproducir Bingo"
elif in_mod == "Bandit":
  set_mod = "Activar Bandit"
st.write(" La acción es:" , set_mod)
