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
    @import url('https://fonts.googleapis.com/css2?family=Lilita+One&family=Outfit:wght@400;600;700;800&family=Rajdhani:wght@600;700;800&display=swap');

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
        margin-top: 18px;
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

    /* Contenedor SVG de Árbol de Decisiones */
    .tree-panel-wrapper {
        margin-top: 14px;
        margin-bottom: 18px;
        border-radius: 18px;
        overflow: hidden;
        filter: drop-shadow(0 10px 25px rgba(0, 0, 0, 0.5));
    }
    </style>
""", unsafe_allow_html=True)

# Título y encabezado global
st.markdown('<div class="main-game-title">🎮 SISTEMA DE DECISIONES EN JUEGOS</div>', unsafe_allow_html=True)
st.markdown('<div class="main-subtitle">Modelado y Simulación Interactiva con Lógica Proposicional</div>', unsafe_allow_html=True)


# ==========================================
# FUNCIÓN GENERADORA DEL ÁRBOL DE DECISIONES SVG
# ==========================================
def render_decision_tree_svg(config, p_val, q_val, r_val):
    """
    Genera un panel SVG interactivo y reactivo con efecto de iluminación neón
    que resalta en tiempo real el camino activo según las selecciones de SÍ/NO.
    """
    uid = config["id"]
    formula = config["formula"]
    root_title, root_sub = config["root"]
    left_title, left_sub = config["left_node"]
    right_title, right_sub = config["right_node"]
    r_title, r_sub = config["r_node"]
    
    leaf_l_si_t, leaf_l_si_s, leaf_l_si_green = config["leaf_left_si"]
    leaf_l_no_t, leaf_l_no_s, leaf_l_no_green = config["leaf_left_no"]
    leaf_r_dir_t, leaf_r_dir_s, leaf_r_dir_green = config["leaf_right_direct"]
    leaf_r_si_t, leaf_r_si_s, leaf_r_si_green = config["leaf_r_si"]
    leaf_r_no_t, leaf_r_no_s, leaf_r_no_green = config["leaf_r_no"]
    
    right_direct_is_si = config.get("right_direct_is_si", True)
    root_is_q = config.get("root_is_q", False)

    first_val = q_val if root_is_q else p_val
    second_val = p_val if root_is_q else q_val
    third_val = r_val

    # Estados activos de nodos y ramas
    act_root = True
    act_branch_root_no = not first_val
    act_branch_root_si = first_val

    act_node_left = not first_val
    act_node_right = first_val

    act_branch_left_si = act_node_left and second_val
    act_branch_left_no = act_node_left and not second_val
    act_leaf_left_si = act_branch_left_si
    act_leaf_left_no = act_branch_left_no

    if right_direct_is_si:
        act_branch_right_dir = act_node_right and second_val
        act_leaf_right_dir = act_branch_right_dir
        act_branch_right_to_r = act_node_right and not second_val
        act_node_r = act_branch_right_to_r
    else:
        act_branch_right_dir = act_node_right and not second_val
        act_leaf_right_dir = act_branch_right_dir
        act_branch_right_to_r = act_node_right and second_val
        act_node_r = act_branch_right_to_r

    act_branch_r_si = act_node_r and third_val
    act_branch_r_no = act_node_r and not third_val
    act_leaf_r_si = act_branch_r_si
    act_leaf_r_no = act_branch_r_no

    def node_box(x, y, w, h, active, title, sub, is_leaf=False, is_green=False):
        if is_leaf:
            if is_green:
                if active:
                    style_rect = f'fill="#052814" stroke="#00E676" stroke-width="2.5" filter="url(#{uid}-glow-green)"'
                    style_t = 'fill="#00E676" font-weight="800" font-size="14.5px"'
                    style_s = 'fill="#86efac" font-weight="600" font-size="11.5px"'
                else:
                    style_rect = 'fill="#0a1818" stroke="#14532d" stroke-width="1.2" opacity="0.32"'
                    style_t = 'fill="#15803d" font-weight="700" font-size="14.5px"'
                    style_s = 'fill="#14532d" font-weight="500" font-size="11.5px"'
            else: # red
                if active:
                    style_rect = f'fill="#2c0808" stroke="#FF5252" stroke-width="2.5" filter="url(#{uid}-glow-red)"'
                    style_t = 'fill="#FF5252" font-weight="800" font-size="14.5px"'
                    style_s = 'fill="#fca5a5" font-weight="600" font-size="11.5px"'
                else:
                    style_rect = 'fill="#180a0a" stroke="#7f1d1d" stroke-width="1.2" opacity="0.32"'
                    style_t = 'fill="#b91c1c" font-weight="700" font-size="14.5px"'
                    style_s = 'fill="#7f1d1d" font-weight="500" font-size="11.5px"'
        else:
            # Nodo de pregunta
            if active:
                style_rect = f'fill="#071b30" stroke="#00E5FF" stroke-width="2.5" filter="url(#{uid}-glow-cyan)"'
                style_t = 'fill="#FFFFFF" font-weight="800" font-size="14px"'
                style_s = 'fill="#38bdf8" font-weight="700" font-size="12px"'
            else:
                style_rect = 'fill="#0b1322" stroke="#1e293b" stroke-width="1.2" opacity="0.35"'
                style_t = 'fill="#64748b" font-weight="600" font-size="14px"'
                style_s = 'fill="#475569" font-weight="600" font-size="12px"'

        return f'''
        <g class="tree-node">
            <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="13" {style_rect} />
            <text x="{x + w/2}" y="{y + h/2 - 4}" text-anchor="middle" dominant-baseline="middle" font-family="'Outfit', sans-serif" {style_t}>{title}</text>
            <text x="{x + w/2}" y="{y + h/2 + 15}" text-anchor="middle" dominant-baseline="middle" font-family="'Outfit', sans-serif" {style_s}>{sub}</text>
        </g>
        '''

    def pill_badge(cx, cy, active, text):
        w, h = 46, 24
        x, y = cx - w/2, cy - h/2
        if active:
            style_rect = f'fill="#002d4a" stroke="#00E5FF" stroke-width="2" filter="url(#{uid}-glow-cyan)"'
            style_t = 'fill="#00E5FF" font-weight="800"'
        else:
            style_rect = 'fill="#0b1322" stroke="#1e293b" stroke-width="1" opacity="0.35"'
            style_t = 'fill="#475569" font-weight="700"'
        return f'''
        <g>
            <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" {style_rect} />
            <text x="{cx}" y="{cy}" text-anchor="middle" dominant-baseline="central" font-family="'Outfit', sans-serif" font-size="11.5px" {style_t}>{text}</text>
        </g>
        '''

    def line_path(x1, y1, x2, y2, active):
        if active:
            return f'''
            <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#00E5FF" stroke-width="8" opacity="0.35" filter="url(#{uid}-glow-cyan)" stroke-linecap="round"/>
            <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#00f0ff" stroke-width="3.5" stroke-linecap="round"/>
            '''
        else:
            return f'''
            <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#1e293b" stroke-width="2" stroke-dasharray="5,5" opacity="0.4" stroke-linecap="round"/>
            '''

    # Configuración de conexiones de la rama derecha
    if right_direct_is_si:
        badge_r_dir_text = "SÍ"
        badge_r_to_r_text = "NO"
        x_r_dir_start, y_r_dir_start = 770, 240
        x_r_dir_end, y_r_dir_end = 810, 335
        cx_badge_r_dir, cy_badge_r_dir = 792, 285

        x_r_to_r_start, y_r_to_r_start = 670, 240
        x_r_to_r_end, y_r_to_r_end = 570, 315
        cx_badge_r_to_r, cy_badge_r_to_r = 618, 275
    else:
        badge_r_dir_text = "NO"
        badge_r_to_r_text = "SÍ"
        x_r_dir_start, y_r_dir_start = 770, 240
        x_r_dir_end, y_r_dir_end = 810, 335
        cx_badge_r_dir, cy_badge_r_dir = 792, 285

        x_r_to_r_start, y_r_to_r_start = 670, 240
        x_r_to_r_end, y_r_to_r_end = 570, 315
        cx_badge_r_to_r, cy_badge_r_to_r = 618, 275

    svg_content = f'''
    <div class="tree-panel-wrapper">
    <svg viewBox="0 0 940 525" width="100%" xmlns="http://www.w3.org/2000/svg" style="background: radial-gradient(circle at 50% 20%, #0f203c 0%, #091224 55%, #040812 100%); border: 1.5px solid #23385d; border-radius: 18px; box-shadow: 0 8px 32px rgba(0,0,0,0.6); display: block;">
        <defs>
            <filter id="{uid}-glow-cyan" x="-30%" y="-30%" width="160%" height="160%">
                <feGaussianBlur stdDeviation="4" result="blur1" />
                <feGaussianBlur stdDeviation="8" result="blur2" />
                <feMerge>
                    <feMergeNode in="blur2" />
                    <feMergeNode in="blur1" />
                    <feMergeNode in="SourceGraphic" />
                </feMerge>
            </filter>
            <filter id="{uid}-glow-green" x="-30%" y="-30%" width="160%" height="160%">
                <feGaussianBlur stdDeviation="5" result="blur1" />
                <feGaussianBlur stdDeviation="9" result="blur2" />
                <feMerge>
                    <feMergeNode in="blur2" />
                    <feMergeNode in="blur1" />
                    <feMergeNode in="SourceGraphic" />
                </feMerge>
            </filter>
            <filter id="{uid}-glow-red" x="-30%" y="-30%" width="160%" height="160%">
                <feGaussianBlur stdDeviation="5" result="blur1" />
                <feGaussianBlur stdDeviation="9" result="blur2" />
                <feMerge>
                    <feMergeNode in="blur2" />
                    <feMergeNode in="blur1" />
                    <feMergeNode in="SourceGraphic" />
                </feMerge>
            </filter>
        </defs>

        <!-- Header -->
        <text x="35" y="36" font-family="'Outfit', 'Rajdhani', sans-serif" font-weight="800" font-size="17px" fill="#38bdf8" letter-spacing="1px">{formula}</text>
        <g>
            <rect x="705" y="18" width="200" height="28" rx="8" fill="rgba(15, 23, 42, 0.7)" stroke="#1e293b" stroke-width="1"/>
            <text x="805" y="32" font-family="'Outfit', sans-serif" font-weight="600" font-size="11.5px" fill="#94a3b8" text-anchor="middle" dominant-baseline="central">⚡ Ruta Dinámica en Vivo</text>
        </g>

        <!-- Líneas: Raíz a Nivel 1 -->
        {line_path(430, 115, 240, 180, act_branch_root_no)}
        {line_path(510, 115, 720, 180, act_branch_root_si)}

        <!-- Pastillas: Raíz a Nivel 1 -->
        {pill_badge(330, 145, act_branch_root_no, "NO")}
        {pill_badge(620, 145, act_branch_root_si, "SÍ")}

        <!-- Líneas: Nodo Izquierdo a Hojas -->
        {line_path(190, 240, 130, 335, act_branch_left_si)}
        {line_path(290, 240, 350, 335, act_branch_left_no)}

        <!-- Pastillas: Nodo Izquierdo a Hojas -->
        {pill_badge(155, 285, act_branch_left_si, "SÍ")}
        {pill_badge(325, 285, act_branch_left_no, "NO")}

        <!-- Líneas: Nodo Derecho a Hoja Directa y a Nodo R -->
        {line_path(x_r_dir_start, y_r_dir_start, x_r_dir_end, y_r_dir_end, act_branch_right_dir)}
        {line_path(x_r_to_r_start, y_r_to_r_start, x_r_to_r_end, y_r_to_r_end, act_branch_right_to_r)}

        <!-- Pastillas: Nodo Derecho a Hoja Directa y a Nodo R -->
        {pill_badge(cx_badge_r_dir, cy_badge_r_dir, act_branch_right_dir, badge_r_dir_text)}
        {pill_badge(cx_badge_r_to_r, cy_badge_r_to_r, act_branch_right_to_r, badge_r_to_r_text)}

        <!-- Líneas: Nodo R a Hojas Nivel 3 -->
        {line_path(530, 375, 470, 425, act_branch_r_si)}
        {line_path(610, 375, 690, 425, act_branch_r_no)}

        <!-- Pastillas: Nodo R a Hojas Nivel 3 -->
        {pill_badge(495, 400, act_branch_r_si, "SÍ")}
        {pill_badge(655, 400, act_branch_r_no, "NO")}

        <!-- NODOS DE PREGUNTA -->
        <!-- Nodo Raíz -->
        {node_box(370, 55, 200, 60, act_root, root_title, root_sub)}

        <!-- Nodos Nivel 1 -->
        {node_box(140, 180, 200, 60, act_node_left, left_title, left_sub)}
        {node_box(620, 180, 200, 60, act_node_right, right_title, right_sub)}

        <!-- Nodo Nivel 2 (R) -->
        {node_box(470, 315, 200, 60, act_node_r, r_title, r_sub)}

        <!-- HOJAS / DECISIONES FINALES -->
        <!-- Hojas Izquierdas (y=335) -->
        {node_box(25, 335, 210, 58, act_leaf_left_si, leaf_l_si_t, leaf_l_si_s, is_leaf=True, is_green=leaf_l_si_green)}
        {node_box(245, 335, 210, 58, act_leaf_left_no, leaf_l_no_t, leaf_l_no_s, is_leaf=True, is_green=leaf_l_no_green)}

        <!-- Hoja Directa Derecha (y=335) -->
        {node_box(705, 335, 210, 58, act_leaf_right_dir, leaf_r_dir_t, leaf_r_dir_s, is_leaf=True, is_green=leaf_r_dir_green)}

        <!-- Hojas de Nodo R (y=425) -->
        {node_box(365, 425, 210, 58, act_leaf_r_si, leaf_r_si_t, leaf_r_si_s, is_leaf=True, is_green=leaf_r_si_green)}
        {node_box(585, 425, 210, 58, act_leaf_r_no, leaf_r_no_t, leaf_r_no_s, is_leaf=True, is_green=leaf_r_no_green)}

        <!-- Leyenda Inferior -->
        <g transform="translate(230, 500)">
            <circle cx="0" cy="0" r="5" fill="#00E676" filter="url(#{uid}-glow-green)"/>
            <text x="12" y="1" font-family="'Outfit', sans-serif" font-size="11.5px" font-weight="700" fill="#a7f3d0" dominant-baseline="middle">{config['legend_pos']}</text>

            <circle cx="170" cy="0" r="5" fill="#FF5252" filter="url(#{uid}-glow-red)"/>
            <text x="182" y="1" font-family="'Outfit', sans-serif" font-size="11.5px" font-weight="700" fill="#fca5a5" dominant-baseline="middle">{config['legend_neg']}</text>

            <circle cx="330" cy="0" r="5" fill="#00E5FF" filter="url(#{uid}-glow-cyan)"/>
            <text x="342" y="1" font-family="'Outfit', sans-serif" font-size="11.5px" font-weight="700" fill="#7dd3fc" dominant-baseline="middle">CAMINO ACTIVO</text>
        </g>
    </svg>
    </div>
    '''
    return svg_content


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

    # Configuración del árbol de decisiones para Brawl Stars
    brawl_tree_config = {
        "id": "brawl",
        "formula": "D = (P ∧ Q) ∨ (P ∧ R)",
        "legend_pos": "ACTIVAR SÚPER",
        "legend_neg": "GUARDAR SÚPER",
        "root_is_q": False,
        "right_direct_is_si": True,
        "root": ("¿Súper cargada al 100%?", "(P)"),
        "left_node": ("¿Enemigos agrupados?", "(Q)"),
        "right_node": ("¿Enemigos agrupados?", "(Q)"),
        "r_node": ("¿Salud crítica (< 20%)?", "(R)"),
        "leaf_left_si": ("🛡️ GUARDAR SÚPER", "¬P ∧ Q (Recargar súper)", False),
        "leaf_left_no": ("🛡️ GUARDAR SÚPER", "¬P ∧ ¬Q (Sin súper)", False),
        "leaf_right_direct": ("🔥 ACTIVAR SÚPER", "P ∧ Q (Impacto en área)", True),
        "leaf_r_si": ("🔥 ACTIVAR SÚPER", "P ∧ ¬Q ∧ R (Supervivencia)", True),
        "leaf_r_no": ("🛡️ GUARDAR SÚPER", "P ∧ ¬Q ∧ ¬R (Ahorrar súper)", False)
    }

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-header">🌳 ÁRBOL DE DECISIÓN DINÁMICO (CAMINO EN TIEMPO REAL)</div>', unsafe_allow_html=True)
    st.write("Observa cómo la ruta neón se ilumina en vivo según las opciones seleccionadas:")
    st.markdown(render_decision_tree_svg(brawl_tree_config, P_bs, Q_bs, R_bs), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-header">📊 ANÁLISIS LÓGICO</div>', unsafe_allow_html=True)
    
    p_b_tag = '<span class="val-true">✅ Verdadero (V)</span>' if P_bs else '<span class="val-false">❌ Falso (F)</span>'
    q_b_tag = '<span class="val-true">✅ Verdadero (V)</span>' if Q_bs else '<span class="val-false">❌ Falso (F)</span>'
    r_b_tag = '<span class="val-true">✅ Verdadero (V)</span>' if R_bs else '<span class="val-false">❌ Falso (F)</span>'

    st.markdown(f'''
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
        <span style="font-weight: 800; color: {'#00E676' if D_bs else '#FF5252'};">{'D = V (Verdadero)' if D_bs else 'D = F (Falso)'}</span>
    </div>
    ''', unsafe_allow_html=True)

    # Decisión Final Brawl Stars
    if D_bs:
        st.markdown('''
        <div class="result-box-green">
            <div class="result-title" style="color: #00E676;">🔥 DECISIÓN: ¡ACTIVAR SÚPER!</div>
            <div class="result-desc" style="color: #e8f5e9;">(Impacto alto o salvación / Supervivencia)</div>
        </div>
        ''', unsafe_allow_html=True)
    else:
        st.markdown('''
        <div class="result-box-red">
            <div class="result-title" style="color: #FF5252;">🛡️ DECISIÓN: ¡GUARDAR SÚPER!</div>
            <div class="result-desc" style="color: #ffebee;">(Ahorrar o recargar / No desperdiciar)</div>
        </div>
        ''', unsafe_allow_html=True)


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

    # Configuración del árbol de decisiones para Minecraft
    mine_tree_config = {
        "id": "mine",
        "formula": "D = (P ∧ Q) ∧ R",
        "legend_pos": "CREAR PICO",
        "legend_neg": "NO CRAFTEAR",
        "root_is_q": False,
        "right_direct_is_si": False,
        "root": ("¿Madera suficiente? (≥3)", "(P)"),
        "left_node": ("¿Mesa de crafteo?", "(Q)"),
        "right_node": ("¿Mesa de crafteo?", "(Q)"),
        "r_node": ("¿Piedra suficiente? (≥3)", "(R)"),
        "leaf_left_si": ("❌ NO CRAFTEAR", "¬P ∧ Q (Falta madera)", False),
        "leaf_left_no": ("❌ NO CRAFTEAR", "¬P ∧ ¬Q (Sin recursos)", False),
        "leaf_right_direct": ("❌ NO CRAFTEAR", "P ∧ ¬Q (Colocar mesa)", False),
        "leaf_r_si": ("⛏️ CREAR PICO", "P ∧ Q ∧ R (¡Crafteo exitoso!)", True),
        "leaf_r_no": ("❌ NO CRAFTEAR", "P ∧ Q ∧ ¬R (Falta piedra)", False)
    }

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-header">🌳 ÁRBOL DE DECISIÓN DINÁMICO (CAMINO EN TIEMPO REAL)</div>', unsafe_allow_html=True)
    st.write("Observa cómo la ruta neón se ilumina en vivo según las opciones seleccionadas:")
    st.markdown(render_decision_tree_svg(mine_tree_config, P_mc, Q_mc, R_mc), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-header">📊 ANÁLISIS LÓGICO</div>', unsafe_allow_html=True)
    
    p_m_tag = '<span class="val-true">✅ Verdadero (V)</span>' if P_mc else '<span class="val-false">❌ Falso (F)</span>'
    q_m_tag = '<span class="val-true">✅ Verdadero (V)</span>' if Q_mc else '<span class="val-false">❌ Falso (F)</span>'
    r_m_tag = '<span class="val-true">✅ Verdadero (V)</span>' if R_mc else '<span class="val-false">❌ Falso (F)</span>'

    st.markdown(f'''
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
        <span style="font-weight: 800; color: {'#00E676' if D_mc else '#FF5252'};">{'D = V (Verdadero)' if D_mc else 'D = F (Falso)'}</span>
    </div>
    ''', unsafe_allow_html=True)

    # Decisión Final Minecraft
    if D_mc:
        st.markdown('''
        <div class="result-box-green">
            <div class="result-title" style="color: #00E676;">⛏️ DECISIÓN: ¡CREAR PICO DE PIEDRA!</div>
            <div class="result-desc" style="color: #e8f5e9;">(¡Crafteo exitoso! Se cumplen todas las condiciones necesarias)</div>
        </div>
        ''', unsafe_allow_html=True)
    else:
        st.markdown('''
        <div class="result-box-red">
            <div class="result-title" style="color: #FF5252;">❌ DECISIÓN: ¡NO PODEMOS CREAR EL PICO!</div>
            <div class="result-desc" style="color: #ffebee;">(Faltan materiales o la mesa de crafteo no está colocada)</div>
        </div>
        ''', unsafe_allow_html=True)


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

    # Configuración del árbol de decisiones para League of Legends
    lol_tree_config = {
        "id": "lol",
        "formula": "D = (P ∧ Q) ∨ (Q ∧ R)",
        "legend_pos": "INICIAR PELEA",
        "legend_neg": "RETIRADA",
        "root_is_q": True,
        "right_direct_is_si": True,
        "root": ("¿Equipo agrupado?", "(Q)"),
        "left_node": ("¿Ventaja de oro?", "(P)"),
        "right_node": ("¿Ventaja de oro?", "(P)"),
        "r_node": ("¿Objetivo Dragón/Barón?", "(R)"),
        "leaf_left_si": ("🚫 RETIRADA", "¬Q ∧ P (Desventaja numérica)", False),
        "leaf_left_no": ("🚫 RETIRADA", "¬Q ∧ ¬P (Equipo disperso)", False),
        "leaf_right_direct": ("⚔️ INICIAR PELEA", "P ∧ Q (Ventaja económica)", True),
        "leaf_r_si": ("⚔️ INICIAR PELEA", "Q ∧ ¬P ∧ R (Disputar objetivo)", True),
        "leaf_r_no": ("🚫 RETIRADA", "Q ∧ ¬P ∧ ¬R (Sin condiciones)", False)
    }

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-header">🌳 ÁRBOL DE DECISIÓN DINÁMICO (CAMINO EN TIEMPO REAL)</div>', unsafe_allow_html=True)
    st.write("Observa cómo la ruta neón se ilumina en vivo según las opciones seleccionadas:")
    st.markdown(render_decision_tree_svg(lol_tree_config, P_lol, Q_lol, R_lol), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-header">📊 ANÁLISIS LÓGICO</div>', unsafe_allow_html=True)
    
    p_l_tag = '<span class="val-true">✅ Verdadero (V)</span>' if P_lol else '<span class="val-false">❌ Falso (F)</span>'
    q_l_tag = '<span class="val-true">✅ Verdadero (V)</span>' if Q_lol else '<span class="val-false">❌ Falso (F)</span>'
    r_l_tag = '<span class="val-true">✅ Verdadero (V)</span>' if R_lol else '<span class="val-false">❌ Falso (F)</span>'

    st.markdown(f'''
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
        <span style="font-weight: 800; color: {'#00E676' if D_lol else '#FF5252'};">{'D = V (Verdadero)' if D_lol else 'D = F (Falso)'}</span>
    </div>
    ''', unsafe_allow_html=True)

    # Decisión Final LoL
    if D_lol:
        st.markdown('''
        <div class="result-box-green">
            <div class="result-title" style="color: #00E676;">⚔️ DECISIÓN: ¡PELEAR (INICIAR PELEA)!</div>
            <div class="result-desc" style="color: #e8f5e9;">(Equipo agrupado con ventaja de oro u objetivo disponible)</div>
        </div>
        ''', unsafe_allow_html=True)
    else:
        st.markdown('''
        <div class="result-box-red">
            <div class="result-title" style="color: #FF5252;">🚫 DECISIÓN: ¡NO PELEAR (RETIRADA)!</div>
            <div class="result-desc" style="color: #ffebee;">(Riesgo alto: el equipo no está agrupado o no hay condiciones favorables)</div>
        </div>
        ''', unsafe_allow_html=True)
