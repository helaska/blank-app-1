import streamlit as st
import random
import time

# Funkcja symulująca odczyt
def simulate():
   return random.choice([0, 1])
def generate():
 while True:
    yield simulate()
    time.sleep(1)

st.title("Operowanie przyciskiem")
st.write(
    "mocker"
)
placeholder = st.empty()
dane = []
for data in generate():
    dane.append(data)
    if len(dane) > 100:
        dane.pop(0)
    placeholder.line_chart(dane)
    time.sleep(1)
