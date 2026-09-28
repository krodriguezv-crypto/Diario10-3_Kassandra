import streamlit as st

# ==========================================
# 1. CONFIGURACIÓN INICIAL DE LA PÁGINA
# ==========================================
st.set_page_config(
    page_title="Relocate & Expat Assistant",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. DICCIONARIO DE TRADUCCIONES (i18n)
# ==========================================
TRANSLATIONS = {
    "ES": {
        "title": "🌐 Asistente y Concierge para Extranjeros",
        "subtitle": "Tu guía integral para comprar, alquilar y gestionar trámites legales sin complicaciones.",
        "lang_select": "Idioma / Language:",
        "nav_title": "Menú Principal",
        "nav_home": "Inicio",
        "nav_vehicles": "🚗 Vehículos (Autos)",
        "nav_realestate": "🏠 Bienes Raíces (Casas/Terrenos)",
        "nav_legal": "⚖️ Trámites Legales",
        "nav_contact": "🤝 Solicitud de Intermediario",
        "mode_title": "Selecciona cómo deseas realizar tu gestión:",
        "mode_diy": "📖 Guía Paso a Paso (Hacerlo yo mismo)",
        "mode_assisted": "🤝 Deseo un Intermediario / Ayuda Profesional",
        # Vehículos
        "veh_rent_title": "Alquiler de Vehículos",
        "veh_buy_title": "Compra de Vehículos",
        "veh_rent_steps": [
            "1. **Licencia y Pasaporte**: Ten tu pasaporte vigente y la licencia de conducir de tu país de origen.",
            "2. **Tarjeta de Crédito**: Requerida para el depósito de garantía (generalmente entre $500 y $1500 USD).",
            "3. **Seguro Vehicular**: Verifica si tu tarjeta de crédito cubre CDW/LDW o contrata el seguro obligatorio local.",
            "4. **Revisión del Auto**: Inspecciona raspones, llantas y combustible antes de firmar el contrato de entrega."
        ],
        "veh_buy_steps": [
            "1. **Búsqueda y Elección**: Selecciona el vehículo en agencias o vendedores particulares.",
            "2. **Inspección Mecánica**: Realiza un chequeo exhaustivo en un taller de confianza.",
            "3. **Verificación Legal**: Consulta el registro de la propiedad para confirmar que no tenga embargos ni multas.",
            "4. **Contrato y Traspaso**: Firma ante Notario Público el protocolo de compraventa y realiza el pago.",
            "5. **Inscripción Registro**: El notario inscribe la propiedad a tu nombre o al de tu sociedad local."
        ],
        # Bienes Raíces
        "re_houses": "Casas / Aptos",
        "re_land": "Terrenos",
        "re_rent": "Alquiler",
        "re_buy": "Compra",
        "re_rent_steps": [
            "1. **Definir Presupuesto y Zona**: Revisa servicios, conectividad y seguridad de la zona.",
            "2. **Comprobante de Ingresos / Referencias**: Muchos arrendadores solicitan prueba de fondos o carta laboral.",
            "3. **Depósito de Garantía**: Por lo general equivale a 1 mes de alquiler pagado por adelantado.",
            "4. **Contrato de Arrendamiento**: Revisa cláusulas sobre mantenimiento, mascotas, tiempo mínimo de contrato y servicios incluidos.",
            "5. **Inventario Inicial**: Firma un acta con el estado físico de la propiedad antes de mudarte."
        ],
        "re_buy_steps": [
            "1. **Estudio de Título (Due Diligence)**: Solicita a un abogado revisar la certificación registral y planos catastrados.",
            "2. **Oferta Formal y Contrato de Opción de Compra**: Firma una opción formal con un depósito de garantía (escrow).",
            "3. **Uso de Suelo y Permisos**: Verifica los permisos municipales (especialmente crucial para terrenos).",
            "4. **Firma de Escritura Pública**: Proceso ante Notario Público para transferir la propiedad formalmente.",
            "5. **Pago de Impuestos y Traslado**: Cubre los honorarios notariales e impuestos de traspaso para inscribir en el Registro."
        ],
        # Legal
        "legal_residency": "Residencia y Visas",
        "legal_license": "Homologación de Licencia",
        "legal_company": "Apertura de Empresa / Cuenta Bancaria",
        "legal_res_steps": [
            "1. **Certificado de Nacimiento**: Debe estar apostillado o legalizado en tu país de origen.",
            "2. **Record Policial / Antecedentes Penales**: Apostillado y emitiendo con menos de 6 meses de antigüedad.",
            "3. **Prueba de Fondos / Inversión**: Demostrar pensión, renta fija o inversión según la categoría de visa.",
            "4. **Traducciones Oficiales**: Todos los documentos en otro idioma deben ser traducidos por un traductor oficial.",
            "5. **Presentación ante Migración**: Filiación, huellas dactilares y pago de timbres correspondientes."
        ],
        "legal_license_steps": [
            "1. **Estatus Migratorio**: Contar con residencia aprobada o visado de estancia vigente.",
            "2. **Licencia de Conducir Extranjera**: Presentar documento original y vigente.",
            "3. **Dictamen Médico**: Examen físico y de la vista emitido por un médico autorizado local.",
            "4. **Cita en Educación Vial**: Agendar y acudir a la oficina correspondiente para solicitar la convalidación."
        ],
        # Formulario
        "form_title": "🤝 Solicitud de Asistencia Personalizada",
        "form_desc": "Completa el formulario y un asesor experto se pondrá en contacto contigo para actuar como tu intermediario legal y gestor.",
        "form_name": "Nombre completo:",
        "form_email": "Correo electrónico:",
        "form_phone": "Teléfono / WhatsApp:",
        "form_service": "Servicio en el que necesitas ayuda:",
        "form_notes": "Detalles adicionales sobre tu solicitud:",
        "form_submit": "Enviar Solicitud",
        "form_success": "✅ ¡Solicitud recibida con éxito! Un intermediario se comunicará contigo pronto."
    },
    "EN": {
        "title": "🌐 Expat Assistance & Concierge App",
        "subtitle": "Your end-to-end guide to rent, buy, and navigate legal procedures stress-free.",
        "lang_select": "Language / Idioma:",
        "nav_title": "Main Menu",
        "nav_home": "Home",
        "nav_vehicles": "🚗 Vehicles (Cars)",
        "nav_realestate": "🏠 Real Estate (Houses/Land)",
        "nav_legal": "⚖️ Legal Procedures",
        "nav_contact": "🤝 Request an Intermediary",
        "mode_title": "Choose how you want to complete your procedure:",
        "mode_diy": "📖 Step-by-Step Guide (Do It Yourself)",
        "mode_assisted": "🤝 I want an Intermediary / Professional Assistance",
        # Vehicles
        "veh_rent_title": "Car Rentals",
        "veh_buy_title": "Car Purchasing",
        "veh_rent_steps": [
            "1. **Driver's License & Passport**: Have a valid passport and your home country driver's license ready.",
            "2. **Credit Card**: Mandatory for the security deposit holding (usually $500 - $1500 USD).",
            "3. **Car Insurance**: Verify if your credit card covers CDW/LDW or purchase local mandatory insurance.",
            "4. **Vehicle Inspection**: Check scratches, tires, and fuel level before signing the handover form."
        ],
        "veh_buy_steps": [
            "1. **Search & Selection**: Choose a vehicle at dealerships or private sellers.",
            "2. **Mechanical Inspection**: Have a trusted mechanic perform a thorough inspection.",
            "3. **Legal Check**: Verify property register to ensure there are no liens, mortgages, or unpaid tickets.",
            "4. **Bill of Sale**: Sign the purchase agreement before a Public Notary and complete the payment.",
            "5. **Title Registration**: The notary registers the title under your personal name or local corporation."
        ],
        # Real Estate
        "re_houses": "Houses / Apartments",
        "re_land": "Land / Lots",
        "re_rent": "Rent",
        "re_buy": "Buy",
        "re_rent_steps": [
            "1. **Budget & Location**: Check local amenities, connectivity, and neighborhood safety.",
            "2. **Proof of Income / References**: Landlords usually request proof of funds or job contract.",
            "3. **Security Deposit**: Typically equivalent to 1 month of rent paid upfront.",
            "4. **Lease Agreement**: Review clauses regarding maintenance, pets, lease term, and utilities included.",
            "5. **Initial Inventory**: Sign a property condition report prior to moving in."
        ],
        "re_buy_steps": [
            "1. **Title Search (Due Diligence)**: Have an attorney review title certificates and survey maps.",
            "2. **Purchase Agreement & Escrow**: Sign a formal option to purchase with an escrow deposit.",
            "3. **Zoning & Land Use**: Verify municipal land use permits (especially critical for vacant land).",
            "4. **Public Deed Signing**: Finalize the transaction before a Public Notary to transfer ownership.",
            "5. **Taxes & Registration**: Pay notary fees and transfer taxes to register the property in your name."
        ],
        # Legal
        "legal_residency": "Residency & Visas",
        "legal_license": "Driver's License Reciprocity",
        "legal_company": "Company / Bank Account Setup",
        "legal_res_steps": [
            "1. **Birth Certificate**: Must be apostilled or legalized in your home country.",
            "2. **Police Check / Background Record**: Apostilled and issued within the last 6 months.",
            "3. **Proof of Funds / Investment**: Prove pension, annuity, or qualifying investment.",
            "4. **Official Translations**: All foreign documents must be translated by a certified official translator.",
            "5. **Immigration Submission**: Biometrics, fingerprints, and payment of official government fees."
        ],
        "legal_license_steps": [
            "1. **Immigration Status**: Valid approved residency or current legal stay visa status.",
            "2. **Foreign Driver's License**: Present original valid license.",
            "3. **Medical Checkup**: Physical and vision exam issued by an authorized local doctor.",
            "4. **Appointment**: Schedule and attend the official traffic department appointment for endorsement."
        ],
        # Form
        "form_title": "🤝 Request Personalized Assistance",
        "form_desc": "Fill out this form and a dedicated local expert will contact you to act as your liaison and legal intermediary.",
        "form_name": "Full Name:",
        "form_email": "Email Address:",
        "form_phone": "Phone / WhatsApp:",
        "form_service": "Service needed:",
        "form_notes": "Additional details or questions:",
        "form_submit": "Submit Request",
        "form_success": "✅ Request received successfully! An intermediary will contact you shortly."
    }
}

# ==========================================
# 3. BARRA LATERAL (CONFIGURACIÓN E IDIOMA)
# ==========================================
st.sidebar.title("🌐 Expat Portal")

lang_code = st.sidebar.radio(
    "Language / Idioma",
    options=["ES", "EN"],
    format_func=lambda x: "Español 🇪🇸" if x == "ES" else "English 🇺🇸"
)

t = TRANSLATIONS[lang_code]

st.sidebar.markdown("---")
st.sidebar.subheader(t["nav_title"])
menu_option = st.sidebar.radio(
    "Go to / Ir a:",
    [t["nav_home"], t["nav_vehicles"], t["nav_realestate"], t["nav_legal"], t["nav_contact"]]
)

# ==========================================
# 4. COMPONENTE REUTILIZABLE PARA ASISTENCIA
# ==========================================
def render_assistance_form(default_service="General"):
    st.info("💡 " + t["form_desc"])
    with st.form(key=f"assistance_form_{default_service}"):
        name = st.text_input(t["form_name"])
        email = st.text_input(t["form_email"])
        phone = st.text_input(t["form_phone"])
        service = st.selectbox(t["form_service"], [default_service, "Vehicles", "Real Estate", "Legal Procedures", "Other"])
        notes = st.text_area(t["form_notes"])
        submitted = st.form_submit_button(t["form_submit"])
        if submitted:
            if name and email:
                st.success(t["form_success"])
            else:
                st.warning("Please fill in required fields (Name & Email)." if lang_code == "EN" else "Por favor completa los campos obligatorios (Nombre y Correo).")

# ==========================================
# 5. VISTAS PRINCIPALES
# ==========================================

# --- INICIO ---
if menu_option == t["nav_home"]:
    st.title(t["title"])
    st.subheader(t["subtitle"])
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 🚗 " + t["nav_vehicles"])
        st.write("Rent or purchase a vehicle safely with clear step-by-step guidance." if lang_code == "EN" else "Alquila o compra un vehículo de forma segura con instructivos claros.")
    with col2:
        st.markdown("### 🏠 " + t["nav_realestate"])
        st.write("Find apartments, homes, or land to rent or buy without legal traps." if lang_code == "EN" else "Encuentra casas, apartamentos o terrenos para comprar o alquilar sin sorpresas.")
    with col3:
        st.markdown("### ⚖️ " + t["nav_legal"])
        st.write("Handle residency, driver licenses, and business permits easily." if lang_code == "EN" else "Gestiona tu residencia, licencia de conducir y apertura de negocios fácilmente.")

    st.markdown("---")
    st.markdown("#### 🌟 " + ("How it works" if lang_code == "EN" else "Cómo funciona"))
    st.write(
        "1. **Select your language** at the left sidebar.\n"
        "2. **Choose the service** you need help with.\n"
        "3. Decide whether to follow our **Step-by-Step DIY Guide** or hire our **Intermediary Concierge Service** to manage everything for you!"
        if lang_code == "EN" else
        "1. **Selecciona tu idioma** en la barra lateral izquierda.\n"
        "2. **Elige el servicio** que necesitas.\n"
        "3. ¡Decide si quieres seguir nuestra **Guía Paso a Paso** por tu cuenta o contratar a nuestro **Intermediario Concierge** para que haga el trámite por ti!"
    )

# --- VEHÍCULOS ---
elif menu_option == t["nav_vehicles"]:
    st.title(t["nav_vehicles"])
    
    sub_tab1, sub_tab2 = st.tabs([t["veh_rent_title"], t["veh_buy_title"]])
    
    with sub_tab1: # Alquiler
        mode = st.radio(t["mode_title"], [t["mode_diy"], t["mode_assisted"]], key="veh_rent_mode")
        if mode == t["mode_diy"]:
            st.markdown(f"### {t['veh_rent_title']} - {t['mode_diy']}")
            for step in t["veh_rent_steps"]:
                st.write(step)
        else:
            st.markdown(f"### {t['veh_rent_title']} - {t['mode_assisted']}")
            render_assistance_form("Car Rental")

    with sub_tab2: # Compra
        mode = st.radio(t["mode_title"], [t["mode_diy"], t["mode_assisted"]], key="veh_buy_mode")
        if mode == t["mode_diy"]:
            st.markdown(f"### {t['veh_buy_title']} - {t['mode_diy']}")
            for step in t["veh_buy_steps"]:
                st.write(step)
        else:
            st.markdown(f"### {t['veh_buy_title']} - {t['mode_assisted']}")
            render_assistance_form("Car Purchase")

# --- BIENES RAÍCES ---
elif menu_option == t["nav_realestate"]:
    st.title(t["nav_realestate"])
    
    property_type = st.radio("Property Type / Tipo de Propiedad:", [t["re_houses"], t["re_land"]], horizontal=True)
    action_type = st.radio("Operation / Operación:", [t["re_rent"], t["re_buy"]], horizontal=True)
    
    st.markdown("---")
    mode = st.radio(t["mode_title"], [t["mode_diy"], t["mode_assisted"]], key="re_mode")
    
    if mode == t["mode_diy"]:
        st.markdown(f"### {action_type} - {property_type} ({t['mode_diy']})")
        steps = t["re_rent_steps"] if action_type == t["re_rent"] else t["re_buy_steps"]
        for step in steps:
            st.write(step)
    else:
        st.markdown(f"### {action_type} - {property_type} ({t['mode_assisted']})")
        render_assistance_form(f"Real Estate: {property_type} ({action_type})")

# --- TRÁMITES LEGALES ---
elif menu_option == t["nav_legal"]:
    st.title(t["nav_legal"])
    
    legal_topic = st.selectbox(
        "Select Legal Procedure / Selecciona el trámite:",
        [t["legal_residency"], t["legal_license"], t["legal_company"]]
    )
    
    st.markdown("---")
    mode = st.radio(t["mode_title"], [t["mode_diy"], t["mode_assisted"]], key="legal_mode")
    
    if mode == t["mode_diy"]:
        st.markdown(f"### {legal_topic} - {t['mode_diy']}")
        if legal_topic == t["legal_residency"]:
            for step in t["legal_res_steps"]:
                st.write(step)
        elif legal_topic == t["legal_license"]:
            for step in t["legal_license_steps"]:
                st.write(step)
        else:
            st.write("1. **Select Business Entity**: Choose LLC, Corporation (S.A.), or Sole Proprietorship.")
            st.write("2. **Name Availability**: Verify name availability in the National Registry.")
            st.write("3. **Bank Account Opening**: Present KYC docs, source of funds, and passport.")
    else:
        st.markdown(f"### {legal_topic} - {t['mode_assisted']}")
        render_assistance_form(f"Legal Procedure: {legal_topic}")

# --- CONTACTO / INTERMEDIARIO ---
elif menu_option == t["nav_contact"]:
    st.title(t["form_title"])
    render_assistance_form("Direct Intermediary Request")