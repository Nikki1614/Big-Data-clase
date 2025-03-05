import requests,json, dash
import pandas as pd
import plotly.express as px
from dash import html,dcc

from pymongo import MongoClient
 
 #Cadena de conexión
URI = "mongodb+srv://nikkiawa:24mSrAJu816pV9OB@cluster0.8uier.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    connection = MongoClient(URI)
except: 
    print("Error") 

db = connection['Pokemon']
collection = db['Info']

def obtenerDatos():
    url = "https://pokeapi.co/api/v2/pokemon?limit=20"  # 🔹 Solo 20 Pokémon
    data = requests.get(url).json()
    lista_pokemons = data["results"]

    habilidades_dict = {}  # Diccionario para contar Pokémon por habilidad

    for pokemon in lista_pokemons:
        pokemon_data = requests.get(pokemon["url"]).json()  # Obtener datos del Pokémon
        collection.insert_one(pokemon_data)  # Guardar en MongoDB
        
        for h in pokemon_data["abilities"]:
            habilidad = h["ability"]["name"]
            if habilidad in habilidades_dict:
                habilidades_dict[habilidad] += 1
            else:
                habilidades_dict[habilidad] = 1

    # 🔹 Convertir diccionario a DataFrame
    df = pd.DataFrame(list(habilidades_dict.items()), columns=["Habilidad", "Cantidad de Pokémon"])

    return df

dataF = obtenerDatos()

# 🔹 Construcción de la App Dash
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Cantidad de Pokémon por Habilidad"),
    dcc.Graph(
        id="grafico",
        figure=px.bar(dataF, x="Habilidad", y="Cantidad de Pokémon", title="Número de Pokémon con cada habilidad")
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)