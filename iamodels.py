import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.svm import OneClassSVM
import joblib
import os
from metrics import get_time
import time

def ModelTrain(ruta,features,categorical_features,data,settings):
    init_time = time.perf_counter()

    df = pd.DataFrame(data)
    X = df[features]

    for col in categorical_features:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col])

    ohe = OneHotEncoder(handle_unknown=settings["OneHotEncoder"]["handle_unknown"], sparse_output=settings["OneHotEncoder"]["sparse_output"])
    ohe_features = ohe.fit_transform(X[categorical_features])
    ohe_df = pd.DataFrame(ohe_features, columns=ohe.get_feature_names_out(categorical_features))
    X = X.drop(categorical_features, axis=settings["pandas"]["axis"])
    X = pd.concat([X, ohe_df], axis=settings["pandas"]["axis"])

    clf = OneClassSVM(nu=settings["OneClassSVM"]["nu"], kernel=settings["OneClassSVM"]["kernel"], gamma=settings["OneClassSVM"]["gamma"])
    clf.fit(X)

    model_path = f"{ruta}/model.joblib"
    joblib.dump(clf, model_path)

    print(f"Modelo entrenado y guardado en {model_path}")

    get_time(init_time)


def ModelMain(ruta,input_data,categorical_features,settings):
    init_time = time.perf_counter()

    try:
        clf = joblib.load(f"{ruta}/model.joblib")
    
        input_df = pd.DataFrame([input_data])
   
        for col in categorical_features:
            le = LabelEncoder()
            input_df[col] = le.fit_transform(input_df[col])

        ohe = OneHotEncoder(handle_unknown=settings["OneHotEncoder"]["handle_unknown"], sparse_output=settings["OneHotEncoder"]["sparse_output"])
        ohe_features = ohe.transform(input_df[categorical_features])
        ohe_df_input = pd.DataFrame(ohe_features, columns=ohe.get_feature_names_out(categorical_features))
        input_df = input_df.drop(categorical_features, axis=settings["pandas"]["axis"])
        input_df = pd.concat([input_df, ohe_df_input], axis=settings["pandas"]["axis"])

        prediction = clf.predict(input_df)

        if prediction[0] == 1:
            print("Todo en orden: 1")
        else:
            print("Problemas en la tarea: -1")

    except FileNotFoundError::
        print(f"Error: Modelo no encontrado en {model_path}. Ejecuta Train() primero.")

    get_time(init_time)