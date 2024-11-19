import json
import iamodels
import pickle
import os

def fuctions_execute(config_json_path: str):
    # Leer el archivo de configuración
    with open(config_json_path, 'r', encoding='utf-8') as file:
        config = json.load(file)

    #Ruta del proyecto
    ruta = config["proyect"]
    with open(f"{ruta}/{config_json_path}", 'r', encoding='utf-8') as file:
        config = json.load(file)


    # Usar los valores del archivo JSON
    categorical_features = config["categorical_features"]
    input_data = config["input_data"]
    settings = config["settings"]

    # Llamar al modelo y mostrar los resultados
    iamodels.ModelMain(ruta,input_data,categorical_features,settings)

def main():

    config_json_path = "config.json"

    result = fuctions_execute(config_json_path)

if __name__ == "__main__":
    main()
