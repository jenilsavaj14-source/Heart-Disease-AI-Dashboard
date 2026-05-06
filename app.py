import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
import plotly.graph_objects as go

# --- 1. PAGE CONFIG & DYNAMIC STYLING ---
st.set_page_config(page_title="Heart Disease Intelligence", layout="wide", page_icon="❤️")

# Theme-aware CSS: Supports both Light and Dark modes
st.markdown("""
    <style>
    [data-testid="stMetric"] {
        border: 1px solid #4d4d4d;
        padding: 15px;
        border-radius: 12px;
        background-color: rgba(255, 255, 255, 0.05);
    }
    div.stButton > button:first-child {
        background-color: #e63946; 
        color: white !important; 
        border-radius: 10px; 
        width: 100%; 
        height: 3.5em; 
        font-weight: bold; 
        font-size: 18px;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. ASSET LOADING ---
current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, 'pipe1.pkl')
data_path = os.path.join(current_dir, 'data.pkl')
pbix_path = os.path.join(current_dir, 'Heart Disease Dashboard.pbix')

@st.cache_resource
def load_assets():
    try:
        model = pickle.load(open(model_path, 'rb'))
        reference_df = pickle.load(open(data_path, 'rb'))
        return model, reference_df
    except Exception as e:
        st.error(f"Error loading files: {e}")
        return None, None

pipe, df_ref = load_assets()

# --- 3. SIDEBAR INPUTS ---
st.sidebar.header("👤 Patient Identity & Data")
patient_name = st.sidebar.text_input("Full Patient Name", "Guest User")

with st.sidebar:
    age = st.slider("Age", 1, 100, 45)
    sex_label = st.selectbox("Sex", ["Male", "Female"])
    cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
    trestbps = st.number_input("Resting Blood Pressure (mmHg)", 80, 200, 120)
    chol = st.number_input("Serum Cholesterol (mg/dl)", 100, 600, 200)
    fbs_label = st.selectbox("Fasting Blood Sugar > 120", ["No", "Yes"])
    restecg = st.selectbox("Resting ECG Result", [0, 1, 2])
    thalach = st.slider("Max Heart Rate Achieved", 60, 220, 150)
    exang_label = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
    oldpeak = st.slider("ST Depression (Oldpeak)", 0.0, 6.0, 1.0)
    slope = st.selectbox("Slope of Peak ST", [0, 1, 2])
    ca = st.selectbox("Major Vessels (0-3)", [0, 1, 2, 3])
    thal = st.selectbox("Thalassemia", [1, 2, 3])

# --- 4. DASHBOARD HEADER ---
st.title(f"Heart Diagnostic Intelligence: {patient_name}")

m1, m2, m3, m4 = st.columns(4)
m1.metric("Age", age)
m2.metric("BP Status", "Normal" if trestbps <= 120 else "High")
m3.metric("Cholesterol", f"{chol} mg/dl")
m4.metric("Max Heart Rate", thalach)

st.divider()

# --- 5. DYNAMIC CLINICAL REASONING ---
reasons = []
if chol > 240: reasons.append("**High Cholesterol:** Levels > 240 mg/dl correlate with artery blockage.")
if trestbps > 140: reasons.append("**Hypertension:** High BP strains the heart muscle.")
if oldpeak > 2.0: reasons.append("**ST Depression:** Elevated 'Oldpeak' suggests heart stress.")
if exang_label == "Yes": reasons.append("**Exercise Angina:** Chest pain during activity is a high-risk marker.")
if not reasons: reasons.append("**Stable Profile:** Metrics are within standard ranges.")

col_reason, col_predict = st.columns([1, 1])

with col_reason:
    st.subheader("🔍 Clinical Reasoning")
    for r in reasons:
        st.markdown(f"- {r}")

# --- 6. PREDICTION & 3D PIE CHART ---
with col_predict:
    st.subheader("🚀 Diagnostic Control")
    run_diagnostic = st.button("💓 RUN FULL DIAGNOSTIC ANALYSIS")
    
    if run_diagnostic:
        input_data = pd.DataFrame({
            'age': [age], 'sex': [1 if sex_label == "Male" else 0], 'cp': [cp], 'trestbps': [trestbps],
            'chol': [chol], 'fbs': [1 if fbs_label == "Yes" else 0], 'restecg': [restecg], 'thalach': [thalach],
            'exang': [1 if exang_label == "Yes" else 0], 'oldpeak': [oldpeak], 'slope': [slope], 'ca': [ca], 'thal': [thal]
        })

        if pipe is not None:
            prediction = pipe.predict(input_data)[0]
            prob = pipe.predict_proba(input_data)[0]
            status = "High Risk Detected" if prediction == 1 else "Healthy / Low Risk"

            if prediction == 1:
                st.error(f"### RESULT: {status} ({prob[1]*100:.1f}%)")
            else:
                st.success(f"### RESULT: {status} ({prob[0]*100:.1f}%)")

            # 3D PIE CHART
            st.markdown("#### Clinical Feature Distribution (%)")
            labels = ['Age', 'BP', 'Cholesterol', 'Heart Rate', 'ST Depression']
            values = [age, trestbps, chol, thalach, oldpeak]
            
            fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3, pull=[0.1, 0.1, 0.1, 0.1, 0.1])])
            fig.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#000000', width=2)))
            fig.update_layout(showlegend=False, height=400, margin=dict(t=0, b=0, l=0, r=0), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig, use_container_width=True)

            # PERSONALIZED REPORT
            report_content = f"""
            HEART DIAGNOSTIC REPORT FOR: {patient_name.upper()}
            ==================================================
            Generated: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}
            
            FINAL STATUS: {status}
            AI CONFIDENCE: {max(prob)*100:.1f}%

            FULL CLINICAL PROFILE:
            ---------------------
            - Age: {age}
            - Sex: {sex_label}
            - Chest Pain Type: {cp}
            - Resting BP: {trestbps} mmHg
            - Serum Cholesterol: {chol} mg/dl
            - Max Heart Rate: {thalach}
            - Exercise Induced Angina: {exang_label}
            - ST Depression: {oldpeak}
            - ST Slope: {slope}
            - Major Vessels: {ca}
            - Thalassemia: {thal}

            CLINICAL REASONING:
            ------------------
            {chr(10).join(reasons).replace('**', '')}

            -----------------------
            Note: Verify with a medical professional.
            """
            st.divider()
            st.download_button(
                label=f"📂 Download Report for {patient_name}",
                data=report_content,
                file_name=f"Report_{patient_name.replace(' ', '_')}.txt",
                mime="text/plain"
            )

# --- 7. POWER BI DOWNLOAD ---
st.divider()
st.subheader("📊 Extended Analytics")
if os.path.exists(pbix_path):
    with open(pbix_path, "rb") as file:
        st.download_button(label="📥 Download Power BI Dashboard (.pbix)", data=file, file_name="Heart_Dashboard.pbix")