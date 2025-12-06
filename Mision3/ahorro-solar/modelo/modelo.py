from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import pickle

data = {
    'ubicacion': ['zona_1', 'zona_2', 'zona_1', 'zona_3', 'zona_2', 'zona_1', 'zona_3', 'zona_2', 'zona_1', 'zona_2', 'zona_1', 'zona_3'],
    'tamano_hogar': [80, 120, 60, 150, 90, 200, 110, 70, 130, 100, 40, 300],  # m2
    'costo_instalacion': [15000000, 22000000, 12000000, 28000000, 18000000, 35000000, 20000000, 14000000, 24000000, 19000000, 5000000, 50000000],  # COP
    'energia_generada': [250, 380, 180, 450, 300, 600, 350, 220, 400, 320, 80, 900],  # kWh/mes
    'ahorro_real': [120000, 200000, 90000, 250000, 150000, 350000, 180000, 110000, 220000, 160000, 40000, 550000]  # COP/mes
}

df = pd.DataFrame(data)
# Separar variables
x = df.drop(columns='ahorro_real')
y = df['ahorro_real']
# Codificar variables categóricas
x_encoded = pd.get_dummies(x)
# print(x_encoded)
# Dividir datos
x_train,x_test,y_train,y_test=train_test_split(x_encoded,y,test_size=0.2,random_state=42)
# Entrenar modelo
modelo = LinearRegression()
modelo.fit(x_train,y_train)
# Guardar modelo
with open('modelo.pkl','wb') as f:
    pickle.dump(modelo,f)
with open('columnas.pkl','wb') as f:
    pickle.dump(x_encoded.columns.tolist(),f)