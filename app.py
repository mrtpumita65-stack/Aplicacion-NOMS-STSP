import streamlit as st

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Consultoría NOM-STPS Digital",
    page_icon="👷‍♂️",
    layout="wide"
)

# --- ESTILOS PERSONALIZADOS (CSS) ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stApp {
        color: #1E3A8A;
    }
    .nom-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1E3A8A;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .category-badge {
        background-color: #E0E7FF;
        color: #1E3A8A;
        padding: 4px 12px;
        border-radius: 15px;
        font-size: 0.8rem;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DATOS INTERNA (NORMAS) ---
NORMAS = {
    "NOM-001": {
        "titulo": "Edificios, locales, instalaciones y áreas en los centros de trabajo - Condiciones de seguridad.",
        "categoria": "Seguridad",
        "objetivo": "Establecer las condiciones de seguridad de los edificios y áreas de trabajo para su funcionamiento y conservación, a fin de prevenir riesgos a los trabajadores.",
        "aplicacion": "Todo el territorio nacional y aplica en todos los centros de trabajo.",
        "obligaciones": [
            "Conservar en condiciones seguras las instalaciones.",
            "Realizar verificaciones oculares anuales.",
            "Contar con sanitarios limpios y seguros.",
            "Proporcionar ventilación natural o artificial adecuada."
        ]
    },
    "NOM-002": {
        "titulo": "Condiciones de seguridad - Prevención y protección contra incendios.",
        "categoria": "Seguridad",
        "objetivo": "Establecer los requerimientos para la prevención y protección contra incendios en los centros de trabajo.",
        "aplicacion": "Centros de trabajo con riesgo de incendio.",
        "obligaciones": [
            "Contar con extintores vigentes y señalizados.",
            "Tener un plan de atención a emergencias de incendio.",
            "Capacitar a las brigadas contra incendio.",
            "Realizar simulacros al menos una vez al año."
        ]
    },
    "NOM-009": {
        "titulo": "Condiciones de seguridad para realizar trabajos en altura.",
        "categoria": "Seguridad",
        "objetivo": "Establecer los requerimientos mínimos de seguridad para prevenir riesgos de caída en trabajos realizados a más de 1.8 metros.",
        "aplicacion": "Centros donde se realicen trabajos a más de 1.8 metros de altura.",
        "obligaciones": [
            "Proporcionar sistemas de protección personal (arnés, líneas de vida).",
            "Supervisar que los trabajos en altura se realicen con seguridad.",
            "Contar con exámenes médicos de los trabajadores.",
            "Tener un plan de rescate en caso de caída."
        ]
    },
    "NOM-017": {
        "titulo": "Equipo de protección personal (EPP) - Selección, uso y manejo.",
        "categoria": "Organización",
        "objetivo": "Establecer los requisitos mínimos para que el patrón seleccione, adquiera y proporcione el EPP necesario.",
        "aplicacion": "Centros de trabajo que requieran uso de equipo de protección según los riesgos.",
        "obligaciones": [
            "Identificar y analizar los riesgos de trabajo por puesto.",
            "Determinar el EPP adecuado para cada trabajador.",
            "Proporcionar el equipo y capacitar en su uso.",
            "Revisar que el EPP se mantenga en condiciones óptimas."
        ]
    },
    "NOM-019": {
        "titulo": "Constitución, integración, organización y funcionamiento de las comisiones de seguridad e higiene.",
        "categoria": "Organización",
        "objetivo": "Establecer los lineamientos para la formación de las comisiones que vigilan la seguridad.",
        "aplicacion": "Todos los centros de trabajo en México.",
        "obligaciones": [
            "Constituir y registrar la Comisión de Seguridad e Higiene.",
            "Realizar recorridos de verificación mensuales o trimestrales.",
            "Investigar las causas de los accidentes y enfermedades.",
            "Proporcionar capacitación a los integrantes de la comisión."
        ]
    },
    "NOM-020": {
        "titulo": "Recipientes sujetos a presión, recipientes criogénicos y generadores de vapor - Funcionamiento y condiciones de seguridad.",
        "categoria": "Seguridad",
        "objetivo": "Establecer condiciones de seguridad para evitar explosiones en equipos que manejan presión.",
        "aplicacion": "Centros que utilicen calderas, compresores o tanques de gas.",
        "obligaciones": [
            "Clasificar los equipos por categorías (I, II o III).",
            "Contar con un listado actualizado de los equipos.",
            "Disponer de un expediente de cada equipo con sus pruebas de presión.",
            "Capacitar al personal que opera estos equipos."
        ]
    },
    "NOM-030": {
        "titulo": "Servicios preventivos de seguridad y salud en el trabajo - Funciones y actividades.",
        "categoria": "Organización",
        "objetivo": "Establecer las funciones de los servicios preventivos para prevenir accidentes y enfermedades.",
        "aplicacion": "Obligatoria para todos los centros de trabajo.",
        "obligaciones": [
            "Designar a un responsable de seguridad y salud.",
            "Elaborar un diagnóstico de seguridad y salud.",
            "Establecer un programa de seguridad con acciones preventivas.",
            "Reportar el seguimiento del programa anualmente."
        ]
    },
    "NOM-033": {
        "titulo": "Condiciones de seguridad para realizar trabajos en espacios confinados.",
        "categoria": "Seguridad",
        "objetivo": "Prevenir riesgos a la salud y vida de trabajadores que entran a lugares con ventilación deficiente.",
        "aplicacion": "Centros de trabajo donde se realicen actividades en espacios confinados.",
        "obligaciones": [
            "Identificar los espacios confinados y evaluar sus riesgos.",
            "Contar con procedimientos de entrada y salida seguros.",
            "Monitorear la calidad del aire antes y durante el trabajo.",
            "Tener siempre un vigía (persona afuera) para emergencias."
        ]
    },
    "NOM-035": {
        "titulo": "Factores de riesgo psicosocial en el trabajo - Identificación, análisis y prevención.",
        "categoria": "Salud",
        "objetivo": "Establecer elementos para identificar y prevenir factores de riesgo psicosocial y promover un entorno organizacional favorable.",
        "aplicacion": "Todos los centros de trabajo, con requisitos según el número de trabajadores.",
        "obligaciones": [
            "Establecer una política de prevención de riesgos psicosociales.",
            "Aplicar cuestionarios de identificación de factores de riesgo.",
            "Adoptar medidas para prevenir la violencia laboral.",
            "Difundir información sobre la salud mental en el trabajo."
        ]
    },
    "NOM-036": {
        "titulo": "Factores de riesgo ergonómico en el trabajo - Manejo manual de cargas.",
        "categoria": "Salud",
        "objetivo": "Prevenir lesiones en trabajadores que realizan carga, acarreo o levantamiento de objetos.",
        "aplicacion": "Donde existan trabajadores que manejen cargas de más de 3kg habitualmente.",
        "obligaciones": [
            "Analizar los riesgos por manejo de cargas.",
            "Adoptar medidas de seguridad (fajas, técnicas de levantamiento).",
            "Vigilar la salud de los trabajadores expuestos.",
            "Capacitar en higiene de columna y posturas seguras."
        ]
    }
}

GLOSARIO = {
    "EPP": "Equipo de Protección Personal: Accesorios y ropa para proteger al trabajador de riesgos.",
    "STPS": "Secretaría del Trabajo y Previsión Social.",
    "Riesgo": "Probabilidad de que un peligro se materialice y cause daño.",
    "Peligro": "Fuente, situación o acto con potencial de daño.",
    "Acto Inseguro": "Acción que realiza un trabajador que lo omite un procedimiento seguro.",
    "Condición Insegura": "Falla en las instalaciones o herramientas que pueden causar un accidente."
}

# --- BARRA LATERAL (SIDEBAR) ---
st.sidebar.image("https://www.gob.mx/cms/uploads/action_program/main_image/26330/post_stps.png", width=200)
st.sidebar.title("Navegación")

menu = st.sidebar.radio(
    "Selecciona una opción:",
    ["🏠 Inicio / Buscador", "📚 Categorías NOM", "💡 Conceptos Básicos"]
)

st.sidebar.divider()
st.sidebar.info("📌 **Nota:** Esta herramienta es informativa. Consulte siempre el Diario Oficial de la Federación (DOF) para textos legales vigentes.")

# --- LÓGICA PRINCIPAL ---

if menu == "🏠 Inicio / Buscador":
    st.title("🔍 Consultoría NOM-STPS Digital")
    st.write("Bienvenido. Utiliza el buscador para encontrar normas por número o palabra clave.")

    search_query = st.text_input("Ejemplo: '035' o 'incendios'", "").lower()

    # Filtrar normas
    resultados = []
    for cod, info in NORMAS.items():
        if search_query in cod.lower() or search_query in info['titulo'].lower() or search_query in info['objetivo'].lower():
            resultados.append((cod, info))

    if resultados:
        for cod, info in resultados:
            with st.container():
                st.markdown(f"""
                <div class="nom-card">
                    <span class="category-badge">{info['categoria']}</span>
                    <h3>{cod} - {info['titulo']}</h3>
                    <p><b>🎯 Objetivo:</b> {info['objetivo']}</p>
                    <p><b>📍 Campo de Aplicación:</b> {info['aplicacion']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                with st.expander("✅ Ver Obligaciones Principales del Patrón"):
                    for obl in info['obligaciones']:
                        st.write(f"- {obl}")
    else:
        st.warning("No se encontraron normas que coincidan con tu búsqueda.")

elif menu == "📚 Categorías NOM":
    st.title("Categorías Oficiales")
    cat_seleccionada = st.selectbox("Selecciona una categoría:", ["Seguridad", "Salud", "Organización", "Específicas", "Producto"])
    
    st.subheader(f"Normas de {cat_seleccionada}")
    
    # Filtrar por categoría
    normas_cat = {k: v for k, v in NORMAS.items() if v['categoria'] == cat_seleccionada}
    
    if normas_cat:
        for cod, info in normas_cat.items():
            st.info(f"**{cod}**: {info['titulo']}")
            if st.button(f"Ver detalles de {cod}", key=cod):
                st.write(f"**Objetivo:** {info['objetivo']}")
                st.write(f"**¿A quién aplica?:** {info['aplicacion']}")
    else:
        st.write("Próximamente se añadirán más normas a esta categoría.")

elif menu == "💡 Conceptos Básicos":
    st.title("💡 Conceptos de Seguridad Industrial")
    st.write("Entiende los términos técnicos de forma sencilla.")
    
    cols = st.columns(2)
    for i, (termino, defn) in enumerate(GLOSARIO.items()):
        with cols[i % 2]:
            st.chat_message("human").write(f"**{termino}**: {defn}")

# --- PIE DE PÁGINA ---
st.divider()
st.caption("Desarrollado para la gestión de Seguridad y Salud en el Trabajo | 2024")
