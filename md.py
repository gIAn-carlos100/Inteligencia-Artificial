import os
import streamlit as st

# Configuración principal de la página
st.set_page_config(
    page_title="Lógica Proposicional en Videojuegos",
    page_icon="🎮",
    layout="centered"
)

# Estilos CSS personalizados para ambientación Gamer / Arcade
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lilita+One&family=Outfit:wght@400;600;700;800&family=Rajdhani:wght@600;700&display=swap');

    /* Fondo y tipografía global */
    .stApp {
        background: radial-gradient(circle at 50% 10%, #17233d 0%, #0c1322 55%, #050811 100%);
        color: #FFFFFF;
        font-family: 'Outfit', sans-serif;
    }

    /* Título Principal */
    .main-game-title {
        font-family: 'Lilita One', cursive, sans-serif;
        font-size: 2.7rem;
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

    .main-subtitle {
        text-align: center;
        color: #94a9d6;
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 1.2rem;
    }

    /* Estilo de las pestañas (Tabs) */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: rgba(15, 23, 42, 0.7);
        padding: 8px;
        border-radius: 12px;
        border: 1px solid #283759;
    }

    .stTabs [data-baseweb="tab"] {
        height: 48px;
        border-radius: 8px;
        font-family: 'Lilita One', cursive, sans-serif;
        font-size: 1.15rem;
        letter-spacing: 0.5px;
        color: #94a3b8;
        padding: 0 18px;
        transition: all 0.2s ease;
    }

    .stTabs [data-baseweb="tab"]:hover {
        color: #FFDE00;
        background: rgba(255, 222, 0, 0.08);
    }

    .stTabs [aria-selected="true"] {
        background-color: #2563eb !important;
        color: #FFFFFF !important;
        box-shadow: 0 4px 14px rgba(37, 99, 235, 0.4);
    }

    /* Títulos de sección dentro de los juegos */
    .section-header {
        font-family: 'Lilita One', cursive, sans-serif;
        color: #FFDE00;
        font-size: 1.45rem;
        letter-spacing: 1px;
        text-shadow: 2px 2px 0 #000;
        margin-top: 15px;
        margin-bottom: 12px;
    }

    /* Estilos de Radio Buttons */
    .stRadio > label {
        color: #FFDE00 !important;
        font-weight: 700 !important;
        font-size: 1.05rem !important;
    }

    .stRadio div[role="radiogroup"] {
        gap: 16px;
        margin-top: 4px;
        margin-bottom: 8px;
    }

    /* Items de análisis lógico */
    .logic-card {
        background: rgba(11, 18, 34, 0.85);
        border: 1px solid #1e293b;
        border-left: 4px solid #3b82f6;
        border-radius: 10px;
        padding: 12px 16px;
        margin-bottom: 9px;
        font-size: 1.02rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .val-true {
        color: #00E676;
        font-weight: 800;
        background: rgba(0, 230, 118, 0.15);
        padding: 4px 12px;
        border-radius: 6px;
        border: 1px solid rgba(0, 230, 118, 0.3);
    }

    .val-false {
        color: #FF5252;
        font-weight: 800;
        background: rgba(255, 82, 82, 0.15);
        padding: 4px 12px;
        border-radius: 6px;
        border: 1px solid rgba(255, 82, 82, 0.3);
    }

    /* Cuadros de decisión final */
    .result-box-green {
        background: linear-gradient(135deg, #0a331a 0%, #14532d 100%);
        border: 3px solid #00E676;
        border-radius: 18px;
        padding: 22px;
        text-align: center;
        box-shadow: 0 0 28px rgba(0, 230, 118, 0.4);
        margin-top: 15px;
    }

    .result-box-red {
        background: linear-gradient(135deg, #3d0c0c 0%, #7f1d1d 100%);
        border: 3px solid #FF5252;
        border-radius: 18px;
        padding: 22px;
        text-align: center;
        box-shadow: 0 0 28px rgba(255, 82, 82, 0.4);
        margin-top: 15px;
    }

    .result-title {
        font-family: 'Lilita One', cursive, sans-serif;
        font-size: 1.85rem;
        letter-spacing: 1px;
        margin-bottom: 6px;
        text-shadow: 2px 2px 0 #000;
    }

    .result-desc {
        font-size: 1.05rem;
        font-weight: 600;
        opacity: 0.95;
    }
    </style>
""", unsafe_allow_html=True)

# Título y encabezado global
st.markdown('<div class="main-game-title">🎮 SISTEMA DE DECISIONES EN JUEGOS</div>', unsafe_allow_html=True)
st.markdown('<div class="main-subtitle">Modelado y Simulación Interactiva con Lógica Proposicional</div>', unsafe_allow_html=True)

# Pestañas para cada videojuego
tab_brawl, tab_mine, tab_lol = st.tabs([
    "⭐ Brawl Stars",
    "⛏️ Minecraft",
    "⚔️ League of Legends"
])

base_dir = os.path.dirname(__file__)

# ==========================================
# 1. BRAWL STARS
# ==========================================
with tab_brawl:
    st.markdown('<div class="section-header">⭐ BRAWL STARS: LÓGICA DE SUPERATAQUES</div>', unsafe_allow_html=True)
    
    # Infografía en grande antes de la decisión
    img_brawl = os.path.join(base_dir, "infografia_brawl_stars.jpg")
    if os.path.exists(img_brawl):
        st.image(img_brawl, caption="📊 Tabla de Verdad y Lógica de Superataques en Brawl Stars", use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-header">⚡ SIMULADOR DE COMBATE</div>', unsafe_allow_html=True)
    st.write("Selecciona el estado actual de tu partida:")

    col1, col2, col3 = st.columns(3)
    with col1:
        p_brawl = st.radio(
            "🔹 **P:** ¿Súper cargada al 100%?",
            options=["Sí", "No"],
            index=1,
            horizontal=True,
            key="brawl_p"
        )
    with col2:
        q_brawl = st.radio(
            "🔹 **Q:** ¿≥ 2 enemigos agrupados?",
            options=["Sí", "No"],
            index=1,
            horizontal=True,
            key="brawl_q"
        )
    with col3:
        r_brawl = st.radio(
            "🔹 **R:** ¿Salud crítica (< 20%)?",
            options=["Sí", "No"],
            index=1,
            horizontal=True,
            key="brawl_r"
        )

    # Booleanos
    P_bs = p_brawl.strip().lower() in ["sí", "si", "s"]
    Q_bs = q_brawl.strip().lower() in ["sí", "si", "s"]
    R_bs = r_brawl.strip().lower() in ["sí", "si", "s"]

    # Fórmula: D = (P ∧ Q) ∨ (P ∧ R)
    D_bs = (P_bs and Q_bs) or (P_bs and R_bs)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-header">📊 ANÁLISIS LÓGICO</div>', unsafe_allow_html=True)
    
    p_b_tag = '<span class="val-true">✅ Verdadero (V)</span>' if P_bs else '<span class="val-false">❌ Falso (F)</span>'
    q_b_tag = '<span class="val-true">✅ Verdadero (V)</span>' if Q_bs else '<span class="val-false">❌ Falso (F)</span>'
    r_b_tag = '<span class="val-true">✅ Verdadero (V)</span>' if R_bs else '<span class="val-false">❌ Falso (F)</span>'
    d_b_color = '#00E676' if D_bs else '#FF5252'
    d_b_text = 'D = V (Verdadero)' if D_bs else 'D = F (Falso)'

    st.markdown(f"""
    <div class="logic-card">
        <span><b>P</b> - Súper cargada al 100%</span>
        {p_b_tag}
    </div>
    <div class="logic-card">
        <span><b>Q</b> - Enemigos en zona de impacto (≥ 2)</span>
        {q_b_tag}
    </div>
    <div class="logic-card">
        <span><b>R</b> - Salud crítica (&lt; 20%)</span>
        {r_b_tag}
    </div>
    <div class="logic-card" style="border-left-color: #f59e0b; background: rgba(245, 158, 11, 0.1);">
        <span><b>Fórmula Lógica:</b> <code>D = (P ∧ Q) ∨ (P ∧ R)</code></span>
        <span style="font-weight: 800; color: {d_b_color};">{d_b_text}</span>
    </div>
    """, unsafe_allow_html=True)

    # Decisión Final Brawl Stars
    if D_bs:
        st.markdown("""
        <div class="result-box-green">
            <div class="result-title" style="color: #00E676;">🔥 DECISIÓN: ¡ACTIVAR SÚPER!</div>
            <div class="result-desc" style="color: #e8f5e9;">(Impacto alto o salvación / Supervivencia)</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="result-box-red">
            <div class="result-title" style="color: #FF5252;">🛡️ DECISIÓN: ¡GUARDAR SÚPER!</div>
            <div class="result-desc" style="color: #ffebee;">(Ahorrar o recargar / No desperdiciar)</div>
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# 2. MINECRAFT
# ==========================================
with tab_mine:
    st.markdown('<div class="section-header">⛏️ MINECRAFT: LÓGICA DE CRAFTEO (PICO DE PIEDRA)</div>', unsafe_allow_html=True)
    
    # Infografía en grande antes de la decisión
    img_mine = os.path.join(base_dir, "infografia_minecraft.png")
    if os.path.exists(img_mine):
        st.image(img_mine, caption="📊 Tabla de Verdad y Lógica de Crafteo en Minecraft", use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-header">🌲 SIMULADOR DE INVENTARIO Y CRAFTEO</div>', unsafe_allow_html=True)
    st.write("Indica los recursos y elementos disponibles:")

    c1, c2, c3 = st.columns(3)
    with c1:
        p_mine = st.radio(
            "🪵 **P:** ¿Madera suficiente? (≥3 troncos)",
            options=["Sí", "No"],
            index=1,
            horizontal=True,
            key="mine_p"
        )
    with c2:
        q_mine = st.radio(
            "📦 **Q:** ¿Mesa de crafteo colocada?",
            options=["Sí", "No"],
            index=1,
            horizontal=True,
            key="mine_q"
        )
    with c3:
        r_mine = st.radio(
            "🪨 **R:** ¿Piedra suficiente? (≥3 cobblestone)",
            options=["Sí", "No"],
            index=1,
            horizontal=True,
            key="mine_r"
        )

    # Booleanos
    P_mc = p_mine.strip().lower() in ["sí", "si", "s"]
    Q_mc = q_mine.strip().lower() in ["sí", "si", "s"]
    R_mc = r_mine.strip().lower() in ["sí", "si", "s"]

    # Fórmula: D = (P ∧ Q) ∧ R
    D_mc = (P_mc and Q_mc) and R_mc

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-header">📊 ANÁLISIS LÓGICO</div>', unsafe_allow_html=True)
    
    p_m_tag = '<span class="val-true">✅ Verdadero (V)</span>' if P_mc else '<span class="val-false">❌ Falso (F)</span>'
    q_m_tag = '<span class="val-true">✅ Verdadero (V)</span>' if Q_mc else '<span class="val-false">❌ Falso (F)</span>'
    r_m_tag = '<span class="val-true">✅ Verdadero (V)</span>' if R_mc else '<span class="val-false">❌ Falso (F)</span>'
    d_m_color = '#00E676' if D_mc else '#FF5252'
    d_m_text = 'D = V (Verdadero)' if D_mc else 'D = F (Falso)'

    st.markdown(f"""
    <div class="logic-card">
        <span><b>P</b> - Madera suficiente (≥ 3 troncos)</span>
        {p_m_tag}
    </div>
    <div class="logic-card">
        <span><b>Q</b> - Mesa de crafteo colocada</span>
        {q_m_tag}
    </div>
    <div class="logic-card">
        <span><b>R</b> - Materiales de piedra (≥ 3 cobblestone)</span>
        {r_m_tag}
    </div>
    <div class="logic-card" style="border-left-color: #f59e0b; background: rgba(245, 158, 11, 0.1);">
        <span><b>Fórmula Lógica:</b> <code>D = (P ∧ Q) ∧ R</code></span>
        <span style="font-weight: 800; color: {d_m_color};">{d_m_text}</span>
    </div>
    """, unsafe_allow_html=True)

    # Decisión Final Minecraft
    if D_mc:
        st.markdown("""
        <div class="result-box-green">
            <div class="result-title" style="color: #00E676;">⛏️ DECISIÓN: ¡CREAR PICO DE PIEDRA!</div>
            <div class="result-desc" style="color: #e8f5e9;">(¡Crafteo exitoso! Se cumplen todas las condiciones necesarias)</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="result-box-red">
            <div class="result-title" style="color: #FF5252;">❌ DECISIÓN: ¡NO PODEMOS CREAR EL PICO!</div>
            <div class="result-desc" style="color: #ffebee;">(Faltan materiales o la mesa de crafteo no está colocada)</div>
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# 3. LEAGUE OF LEGENDS
# ==========================================
with tab_lol:
    st.markdown('<div class="section-header">⚔️ LEAGUE OF LEGENDS: INICIAR TEAMFIGHT</div>', unsafe_allow_html=True)
    
    # Infografía en grande antes de la decisión
    img_lol = os.path.join(base_dir, "infografia_lol.png")
    if os.path.exists(img_lol):
        st.image(img_lol, caption="📊 Tabla de Verdad y Toma de Decisiones en League of Legends", use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-header">🛡️ SIMULADOR DE TEAMFIGHT</div>', unsafe_allow_html=True)
    st.write("Evalúa el estado de la partida antes de iniciar la pelea:")

    l1, l2, l3 = st.columns(3)
    with l1:
        p_lol = st.radio(
            "💰 **P:** ¿Ventaja de oro?",
            options=["Sí", "No"],
            index=1,
            horizontal=True,
            key="lol_p"
        )
    with l2:
        q_lol = st.radio(
            "👥 **Q:** ¿Equipo agrupado?",
            options=["Sí", "No"],
            index=1,
            horizontal=True,
            key="lol_q"
        )
    with l3:
        r_lol = st.radio(
            "🐉 **R:** ¿Objetivo disponible (Dragón/Barón)?",
            options=["Sí", "No"],
            index=1,
            horizontal=True,
            key="lol_r"
        )

    # Booleanos
    P_lol = p_lol.strip().lower() in ["sí", "si", "s"]
    Q_lol = q_lol.strip().lower() in ["sí", "si", "s"]
    R_lol = r_lol.strip().lower() in ["sí", "si", "s"]

    # Fórmula: D = (P ∧ Q) ∨ (Q ∧ R)
    D_lol = (P_lol and Q_lol) or (Q_lol and R_lol)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-header">📊 ANÁLISIS LÓGICO</div>', unsafe_allow_html=True)
    
    p_l_tag = '<span class="val-true">✅ Verdadero (V)</span>' if P_lol else '<span class="val-false">❌ Falso (F)</span>'
    q_l_tag = '<span class="val-true">✅ Verdadero (V)</span>' if Q_lol else '<span class="val-false">❌ Falso (F)</span>'
    r_l_tag = '<span class="val-true">✅ Verdadero (V)</span>' if R_lol else '<span class="val-false">❌ Falso (F)</span>'
    d_l_color = '#00E676' if D_lol else '#FF5252'
    d_l_text = 'D = V (Verdadero)' if D_lol else 'D = F (Falso)'

    st.markdown(f"""
    <div class="logic-card">
        <span><b>P</b> - Ventaja de oro</span>
        {p_l_tag}
    </div>
    <div class="logic-card">
        <span><b>Q</b> - Nuestro equipo está agrupado</span>
        {q_l_tag}
    </div>
    <div class="logic-card">
        <span><b>R</b> - Objetivo importante disponible (Dragón / Barón)</span>
        {r_l_tag}
    </div>
    <div class="logic-card" style="border-left-color: #f59e0b; background: rgba(245, 158, 11, 0.1);">
        <span><b>Fórmula Lógica:</b> <code>D = (P ∧ Q) ∨ (Q ∧ R)</code></span>
        <span style="font-weight: 800; color: {d_l_color};">{d_l_text}</span>
    </div>
    """, unsafe_allow_html=True)

    # Decisión Final LoL
    if D_lol:
        st.markdown("""
        <div class="result-box-green">
            <div class="result-title" style="color: #00E676;">⚔️ DECISIÓN: ¡PELEAR (INICIAR PELEA)!</div>
            <div class="result-desc" style="color: #e8f5e9;">(Equipo agrupado con ventaja de oro u objetivo disponible)</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="result-box-red">
            <div class="result-title" style="color: #FF5252;">🚫 DECISIÓN: ¡NO PELEAR (RETIRADA)!</div>
            <div class="result-desc" style="color: #ffebee;">(Riesgo alto: el equipo no está agrupado o no hay condiciones favorables)</div>
        </div>
        """, unsafe_allow_html=True)