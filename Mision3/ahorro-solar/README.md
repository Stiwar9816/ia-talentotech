# ☀️ SolarTech - Calculadora de Ahorro Solar con IA

**SolarTech** es una aplicación web inteligente diseñada para estimar el ahorro económico potencial al implementar energía solar en hogares colombianos. Utiliza un modelo de **Machine Learning (Regresión Lineal)** entrenado con datos del mercado energético para predecir ahorros basados en la ubicación, tamaño del hogar, costo de instalación y generación de energía.

![SolarTech Banner](static/slider_1.png)

## 🚀 Características Principales

- **Predicción Inteligente**: Estimación precisa del ahorro mensual en la factura de luz utilizando Inteligencia Artificial.
- **Visualización de Datos**: Gráficos interactivos (Chart.js) que proyectan el ahorro a 1 mes, 1 año, 5 años y 10 años.
- **Impacto Ambiental**: Cálculo del CO2 evitado y árboles equivalentes plantados gracias al uso de energía solar.
- **Interfaz Moderna**: Diseño responsivo y minimalista construido con **Tailwind CSS**.
- **Modo Oscuro/Claro**: Soporte nativo para temas claro y oscuro, respetando la preferencia del sistema.
- **Animaciones**: Experiencia de usuario fluida con animaciones al hacer scroll (AOS).
- **Guía de Zonas**: Herramienta interactiva para ayudar a los usuarios a identificar su zona solar en Colombia.

## 🛠️ Tecnologías Utilizadas

### Backend
- **Python 3**: Lenguaje principal.
- **Flask**: Framework web ligero para servir la aplicación y la API.
- **Scikit-learn**: Biblioteca para crear y entrenar el modelo de regresión lineal.
- **Pandas**: Manipulación y análisis de datos para el entrenamiento y predicción.
- **Pickle**: Serialización del modelo entrenado.

### Frontend
- **HTML5 / Jinja2**: Estructura y motor de plantillas.
- **Tailwind CSS**: Framework de utilidad para estilos modernos y responsivos.
- **JavaScript (Vanilla)**: Lógica del lado del cliente.
- **Chart.js**: Librería para gráficos interactivos.
- **AOS (Animate On Scroll)**: Librería para animaciones de entrada.

## 📦 Instalación y Ejecución

Sigue estos pasos para correr el proyecto en tu máquina local:

### 1. Prerrequisitos
Asegúrate de tener instalado **Python 3.8+** y **Git**.

### 2. Clonar el Repositorio
```bash
git clone <url-del-repositorio>
cd ahorro-solar
```

### 3. Crear un Entorno Virtual
Es recomendable usar un entorno virtual para aislar las dependencias.

**En Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**En Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 4. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 5. Entrenar el Modelo (Opcional)
Si deseas regenerar el modelo con nuevos datos:
```bash
cd modelo
python modelo.py
cd ..
```

### 6. Ejecutar la Aplicación
```bash
python api/index.py
```

La aplicación estará disponible en: `http://localhost:5000`

## 📂 Estructura del Proyecto

```
ahorro-solar/
├── api/
│   └── index.py          # Punto de entrada de la aplicación Flask
├── modelo/
│   ├── modelo.py         # Script de entrenamiento del modelo
│   ├── modelo.pkl        # Modelo entrenado serializado
│   └── columnas.pkl      # Columnas del modelo para consistencia
├── static/               # Archivos estáticos (imágenes, JS, CSS)
│   ├── favicon.png
│   ├── slider_1.png
│   └── ...
├── templates/            # Plantillas HTML (Jinja2)
│   ├── base.html         # Layout base (Navbar, Footer)
│   ├── index.html        # Página de inicio
│   ├── formulario.html   # Calculadora
│   ├── resultado.html    # Página de resultados
│   ├── about.html        # Sobre Nosotros
│   ├── contact.html      # Contacto
│   └── privacy.html      # Política de Privacidad
├── requirements.txt      # Lista de dependencias
└── README.md             # Documentación del proyecto
```

## 🤝 Contribución
Este proyecto fue desarrollado como parte de la **Misión 3 de IA - TalentoTech**.

---
© 2025 SolarTech. Todos los derechos reservados.
