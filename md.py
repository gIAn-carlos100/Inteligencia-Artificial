import os
import streamlit as st

# Configuración de la página web
st.set_page_config(
    page_title="Decisión - Brawl Stars",
    page_icon="🎮",
    layout="centered"
)

# Estilos CSS personalizados para ambientar el juego (Estilo Brawl Stars)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lilita+One&family=Outfit:wght@400;600;800&display=swap');

    /* Fondo y tipografía general */
    .stApp {
        background: radial-gradient(circle at 50% 10%, #1a2a4c 0%, #0c1322 60%, #060911 100%);
        color: #FFFFFF;
        font-family: 'Outfit', sans-serif;
    }

    /* Título estilo Brawl Stars */
    .brawl-title {
        font-family: 'Lilita One', cursive, sans-serif;
        font-size: 2.6rem;
        color: #FFDE00;
        text-align: center;
        text-shadow: 
            -2px -2px 0 #000,  
             2px -2px 0 #000,
            -2px  2px 0 #000,
             2px  2px 0 #000,
             0px  4px 0 #C46D00,
             0px  8px 15px rgba(0,0,0,0.8);
        letter-spacing: 1.5px;
        margin-top: -10px;
        margin-bottom: 0.2rem;
    }

    .brawl-subtitle {
        text-align: center;
        color: #79a6d2;
        font-size: 1.05rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
    }

    /* Tarjeta contenedora estilo juego */
    .brawl-card {
        background: rgba(18, 27, 49, 0.9);
        border: 2px solid #2b3d68;
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.5), inset 0 1px 1px rgba(255,255,255,0.1);
        margin-bottom: 20px;
    }

    .brawl-section-title {
        font-family: 'Lilita One', cursive, sans-serif;
        color: #FFCC00;
        font-size: 1.45rem;
        letter-spacing: 1px;
        text-shadow: 2px 2px 0 #000;
        margin-bottom: 12px;
    }

    /* Estilos de las preguntas */
    .stRadio > label {
        color: #FFDE00 !important;
        font-weight: 700 !important;
        font-size: 1.05rem !important;
    }
    
    .stRadio div[role="radiogroup"] {
        gap: 15px;
    }

    /* Análisis Lógico Item */
    .logic-item {
        background: rgba(10, 16, 30, 0.7);
        border-left: 4px solid #3b82f6;
        border-radius: 8px;
        padding: 10px 15px;
        margin-bottom: 8px;
        font-size: 1rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .val-true {
        color: #00E676;
        font-weight: 800;
        background: rgba(0, 230, 118, 0.15);
        padding: 3px 10px;
        border-radius: 6px;
        border: 1px solid rgba(0, 230, 118, 0.3);
    }

    .val-false {
        color: #FF5252;
        font-weight: 800;
        background: rgba(255, 82, 82, 0.15);
        padding: 3px 10px;
        border-radius: 6px;
        border: 1px solid rgba(255, 82, 82, 0.3);
    }

    /* Cuadros de decisión final */
    .result-box-activate {
        background: linear-gradient(135deg, #0d381e 0%, #155724 100%);
        border: 3px solid #00E676;
        border-radius: 18px;
        padding: 22px;
        text-align: center;
        box-shadow: 0 0 30px rgba(0, 230, 118, 0.45);
    }

    .result-box-save {
        background: linear-gradient(135deg, #3d0c0c 0%, #681616 100%);
        border: 3px solid #FF5252;
        border-radius: 18px;
        padding: 22px;
        text-align: center;
        box-shadow: 0 0 30px rgba(255, 82, 82, 0.45);
    }

    .result-title {
        font-family: 'Lilita One', cursive, sans-serif;
        font-size: 1.85rem;
        letter-spacing: 1px;
        margin-bottom: 6px;
        text-shadow: 2px 2px 0 #000;
    }

    .result-subtitle {
        font-size: 1.05rem;
        font-weight: 600;
        opacity: 0.95;
    }

    /* Imagen decorativa */
    .image-container {
        border-radius: 16px;
        overflow: hidden;
        border: 3px solid #2b3d68;
        box-shadow: 0 10px 30px rgba(0,0,0,0.6);
        margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# Encabezado temático
st.markdown('<div class="brawl-title">🎮 DECISIÓN - BRAWL STARS</div>', unsafe_allow_html=True)
st.markdown('<div class="brawl-subtitle">Lógica Proposicional y Toma de Decisiones de Superataques</div>', unsafe_allow_html=True)

# 1. IMAGEN DE LA INFOGRAFÍA EN GRANDE (Antes de la toma de decisiones)
image_path = os.path.join(os.path.dirname(__file__), "infografia_brawl_stars.jpg")
if os.path.exists(image_path):
    st.image(image_path, caption="📊 Guía Completa de Lógica de Superataques (Tabla de Verdad y Ejemplos)", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# 2. SECCIÓN DE PREGUNTAS INTERACTIVAS
st.markdown('<div class="brawl-section-title">⚡ SIMULADOR DE COMBATE</div>', unsafe_allow_html=True)
st.write("Responde las condiciones actuales de tu partida:")

# Preguntas interactivas con botones de opción
p_res = st.radio(
    "🔹 **P:** ¿El Brawler tiene la Súper cargada al 100%?",
    options=["Sí", "No"],
    index=1,
    horizontal=True
)

q_res = st.radio(
    "🔹 **Q:** ¿Hay al menos 2 enemigos en la zona de impacto?",
    options=["Sí", "No"],
    index=1,
    horizontal=True
)

r_res = st.radio(
    "🔹 **R:** ¿La salud del Brawler es crítica (< 20%)?",
    options=["Sí", "No"],
    index=1,
    horizontal=True
)

# Evaluación Booleana rigurosa
P = p_res.strip().lower() in ["sí", "si", "s", "true"]
Q = q_res.strip().lower() in ["sí", "si", "s", "true"]
R = r_res.strip().lower() in ["sí", "si", "s", "true"]

# Lógica Booleana: D = (P ∧ Q) ∨ (P ∧ R)
D = (P and Q) or (P and R)

st.markdown("<br>", unsafe_allow_html=True)

# 3. ANÁLISIS LÓGICO EN TIEMPO REAL
st.markdown('<div class="brawl-section-title">📊 ANÁLISIS LÓGICO</div>', unsafe_allow_html=True)

p_badge = '<span class="val-true">✅ Verdadero (V)</span>' if P else '<span class="val-false">❌ Falso (F)</span>'
q_badge = '<span class="val-true">✅ Verdadero (V)</span>' if Q else '<span class="val-false">❌ Falso (F)</span>'
r_badge = '<span class="val-true">✅ Verdadero (V)</span>' if R else '<span class="val-false">❌ Falso (F)</span>'

st.markdown(f'''
<div class="logic-item">
    <span><b>P</b> - Súper cargada al 100%</span>
    {p_badge}
</div>
<div class="logic-item">
    <span><b>Q</b> - Enemigos en zona (≥ 2)</span>
    {q_badge}
</div>
<div class="logic-item">
    <span><b>R</b> - Salud crítica (&lt; 20%)</span>
    {r_badge}
</div>
<div class="logic-item" style="border-left-color: #f59e0b; background: rgba(245, 158, 11, 0.1);">
    <span><b>Fórmula Lógica:</b> <code>D = (P ∧ Q) ∨ (P ∧ R)</code></span>
    <span style="font-weight: 800; color: {'#00E676' if D else '#FF5252'};">{'D = V' if D else 'D = F'}</span>
</div>
''', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 4. DECISIÓN FINAL
if D:
    # SI D ES VERDADERO -> VERDE: ACTIVAR SÚPER
    st.markdown('''
    <div class="result-box-activate">
        <div class="result-title" style="color: #00E676;">🔥 DECISIÓN: ¡ACTIVAR SÚPER!</div>
        <div class="result-subtitle" style="color: #e8f5e9;">(Impacto alto o salvación / Supervivencia)</div>
    </div>
    ''', unsafe_allow_html=True)
else:
    # SI D ES FALSO -> ROJO: GUARDAR SÚPER
    st.markdown('''
    <div class="result-box-save">
        <div class="result-title" style="color: #FF5252;">🛡️ DECISIÓN: ¡GUARDAR SÚPER!</div>
        <div class="result-subtitle" style="color: #ffebee;">(Ahorrar o recargar / No desperdiciar)</div>
    </div>
    ''', unsafe_allow_html=True)
