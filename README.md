# One Class SVM

* **Este repositorio contiene un sistema de detección de anomalías basado en un algoritmo One-Class SVM. El modelo se entrena con datos históricos para identificar patrones normales y, posteriormente, detecta instancias que se desvían significativamente de estos patrones. El proceso implica dos etapas principales:**

	1. **Entrenamiento:** Un modelo One-Class SVM se entrena utilizando un conjunto de datos que representan el comportamiento normal del sistema o proceso que se está monitoreando. Este entrenamiento define los límites de la "normalidad".

	2. **Predicción:** Se utiliza el modelo entrenado para clasificar nuevos datos como "normales" o "anómalos". Los datos anómalos son aquellos que se encuentran fuera de los límites definidos durante el entrenamiento.

* **Sus aplicaciones potenciales incluyen, pero no se limitan a: detección de fraude, mantenimiento predictivo, monitoreo de la red, y control de calidad en procesos de manufactura. La modularidad del código facilita su integración en diferentes entornos y la adaptación a conjuntos de datos específicos.**



## Detalles Tecnicos 

El modelo utilizado es `sklearn.svm.OneClassSVM`, con la posibilidad de ajustar hiperparámetros como `nu` y `kernel` para optimizar el rendimiento. El preprocesamiento de datos incluye codificación one-hot para variables categóricas, asegurando la compatibilidad del modelo con diferentes tipos de datos. Se proporciona una función para entrenar el modelo y guardarlo utilizando `joblib`, y otra función para cargar el modelo y realizar predicciones. El código está escrito en Python y requiere las librerías `pandas`, `scikit-learn`, y `joblib`.


## Configuración

* Acceda a la ruta del proyecto a ejecutar y modifique el `config.json`

```json
{
 "json_file":"interest_048.json",
 "features" : [
  "intTskTime",
  "intTskStatus",
  "intPrjCollaborators",
  "intPrjFiles",
  "intPrjType",
  "intTskType"
 ],
 "categorical_features":[
  "intTskStatus",
  "intPrjType",
  "intTskType"
 ],
 "input_data":{
  "intTskTime": 120,
  "intTskStatus": "No finalizado",
  "intPrjCollaborators": 10,
  "intPrjFiles": 8,
  "intPrjType": "Desarrollo",
  "intTskType": "Desarrollo"
 },
 "settings":{
  "OneHotEncoder":{
   "handle_unknown":"ignore",
   "sparse_output":false
  },
  "OneClassSVM":{
   "nu":0.1,
   "kernel":"rbf",
   "gamma":0.1
  },
  "pandas":{
   "axis":1
  }
 }
}
```


### Explicación de los campos:

• "json_file": Ruta al archivo JSON que contiene los datos de entrenamiento.

• "features": Lista de nombres de columnas que se utilizarán como inputs para el modelo.

• "categorical_features": Subconjunto de "features" que son variables categóricas.

• "input_data": Un ejemplo de datos de entrada para realizar una predicción.

• "settings": Contiene la configuración de los parámetros para OneHotEncoder y OneClassSVM.


## Dependencias

Este proyecto requiere las siguientes librerías de Python:

• pandas
• scikit-learn
• joblib

Puedes instalarlas usando pip:

```shell
pip install -r requirements.txt
```