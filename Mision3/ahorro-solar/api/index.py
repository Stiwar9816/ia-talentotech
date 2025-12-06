from flask import Flask, request, render_template
import os
import pickle
import pandas as pd
import requests

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

@app.route('/api/solar-data', methods=['POST'])
def get_solar_data():
    try:
        data = request.get_json()
        lat = data.get('lat')
        lon = data.get('lon')
        
        if not lat or not lon:
            return {'error': 'Missing coordinates'}, 400

        # NASA POWER API
        # Parameters: ALLSKY_SFC_SW_DWN (All Sky Surface Shortwave Downward Irradiance)
        # Community: RE (Renewable Energy)
        url = "https://power.larc.nasa.gov/api/temporal/climatology/point"
        params = {
            'parameters': 'ALLSKY_SFC_SW_DWN',
            'community': 'RE',
            'longitude': lon,
            'latitude': lat,
            'format': 'JSON'
        }
        
        response = requests.get(url, params=params)
        if response.status_code == 200:
            api_data = response.json()
            # Get annual average
            annual_irradiance = api_data['properties']['parameter']['ALLSKY_SFC_SW_DWN']['ANN']
            
            # Estimate generation: Irradiance (kWh/m2/day) * 30 days * Efficiency (0.15-0.20) * Area (approx 20m2 for standard system)
            # Simplified: Irradiance * 5 (peak hours approx) * 30 * SystemSize(kW)
            # Let's assume a standard 3kW system for the estimation
            estimated_generation = annual_irradiance * 30 * 3 * 0.75 # 0.75 performance ratio
            
            return {
                'irradiance': annual_irradiance,
                'estimated_generation': round(estimated_generation, 2),
                'message': 'Data fetched successfully'
            }
        else:
            return {'error': 'Failed to fetch data from NASA API'}, 500
            
    except Exception as e:
        return {'error': str(e)}, 500

def calculate_scenario(data):
    """Helper function to calculate prediction and impact for a single scenario"""
    df = pd.DataFrame([data])
    df_encoded = pd.get_dummies(df)
    for col in columnas:
        if col not in df_encoded:
            df_encoded[col] = 0
            
    prediccion = modelo.predict(df_encoded[columnas])[0]
    prediccion = max(0, prediccion) # Ensure no negative savings
    
    # Environmental Impact
    energia = data['energia_generada']
    co2 = int(energia * 0.2)
    arboles = int(co2 / 1.67)
    
    # ROI Calculation
    costo_instalacion = data['costo_instalacion']
    if prediccion > 0:
        meses_recuperacion = costo_instalacion / prediccion
        anios_recuperacion = meses_recuperacion / 12
    else:
        meses_recuperacion = 0
        anios_recuperacion = 0
        
    return {
        'prediccion_valor': prediccion,
        'prediccion': "{:,.0f} COP".format(prediccion).replace(',', '.'),
        'co2': co2,
        'arboles': arboles,
        'meses_recuperacion': int(meses_recuperacion),
        'anios_recuperacion': round(anios_recuperacion, 1),
        'costo_instalacion': costo_instalacion,
        'energia_generada': energia
    }

@app.route('/predict',methods=['POST'])
def predecir():
    # Common data
    ubicacion = request.form['ubicacion']
    tamano_hogar = int(request.form['tamano_hogar'])
    
    # Scenario A Data
    datos_a = {
        'ubicacion': ubicacion,
        'tamano_hogar': tamano_hogar,
        'costo_instalacion': float(request.form['costo_instalacion']),
        'energia_generada': float(request.form['energia_generada']),     
    }
    
    # Calculate Scenario A
    resultado_a = calculate_scenario(datos_a)
    
    return render_template('resultado.html', 
                           ubicacion=ubicacion,
                           tamano_hogar=tamano_hogar,
                           resultado_a=resultado_a,
                           prediccion=resultado_a['prediccion'], 
                           co2=resultado_a['co2'], 
                           arboles=resultado_a['arboles'],
                           meses_recuperacion=resultado_a['meses_recuperacion'],
                           anios_recuperacion=resultado_a['anios_recuperacion'],
                           costo_instalacion=resultado_a['costo_instalacion'],
                           energia_generada=resultado_a['energia_generada'])

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)