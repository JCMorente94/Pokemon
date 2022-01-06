import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


df_pokemon = pd.read_csv("pokemon.csv")

st.title("Pokemon Dataset")
pokedex_number = st.number_input(label="Pokedex Number", min_value=1, max_value=721, value=1)

df = df_pokemon[df_pokemon["pokedex_number"] == pokedex_number]

st.image(f"pokemon_jpg/{pokedex_number}.jpg")

list_attributes = ['name', 'attack', 'defense', 'hp', 'sp_attack', 'sp_defense', 'speed', 'type1', 'type2', 'experience_growth', 'base_happiness']

for attribute in list_attributes:
    st.write(f"{attribute}: {df[attribute].values[0]}")
