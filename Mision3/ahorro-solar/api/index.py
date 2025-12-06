from flask import Flask, request, render_template
import os
import pickle
import pandas as pd

app = Flask(__name__,template_folder='../templates',static_folder='../static')
modelo = pickle.load(open(os.path.join(os.path.dirname(__file__),'../modelo/modelo.pkl'),'rb'))
columnas = pickle.load(open(os.path.join(os.path.dirname(__file__),'../modelo/columnas.pkl'),'rb'))

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/sobre-nosotros',methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/privacidad',methods=['GET'])
def privacy():
    return render_template('privacy.html')

@app.route('/contacto',methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/formulario',methods=['GET'])
def formulario():
    return render_template('formulario.html')

@app.route('/predict',methods=['POST'])
def predecir():
    datos={
    'ubicacion': request.form['ubicacion'],
    'tamano_hogar':int(request.form['tamano_hogar']),
    'costo_instalacion':float(request.form['costo_instalacion']),
    'energia_generada':float(request.form['energia_generada']),     
    }
    df = pd.DataFrame([datos])
    df_encoded=pd.get_dummies(df)
    for col in columnas:
        if col not in df_encoded:
            df_encoded[col]=0
    prediccion= modelo.predict(df_encoded[columnas])[0]
    prediccion = max(0, prediccion) # Ensure no negative savings
    prediccion_formateada = "{:,.0f} COP".format(prediccion).replace(',', '.')
    
    # Environmental Impact Calculations
    # Factor Colombia: ~0.2 kg CO2/kWh (conservative estimate for hydro-heavy grid)
    # Trees: ~20kg CO2/year per tree -> ~1.67 kg/month
    energia = datos['energia_generada']
    co2 = int(energia * 0.2)
    arboles = int(co2 / 1.67)
    
    return render_template('resultado.html', prediccion=prediccion_formateada, co2=co2, arboles=arboles)
if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)