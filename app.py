import streamlit as st
import sqlite3
import pickle
import numpy as np
import base64

# ---------------- BACKGROUND IMAGE ----------------
def set_bg(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)),
                        url("data:image/jpg;base64,{encoded}");
            background-size: cover;
        }}
        </style>
    """, unsafe_allow_html=True)

set_bg("heart.jpg")

# ---------------- DATABASE ----------------
conn = sqlite3.connect("users.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users(
    username TEXT,
    password TEXT
)
""")
conn.commit()

def add_user(username, password):
    c.execute("INSERT INTO users VALUES (?,?)", (username, password))
    conn.commit()

def login_user(username, password):
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    return c.fetchall()

# ---------------- LOAD MODEL ----------------
model = pickle.load(open("heart_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# ---------------- SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- LOGIN ----------------
def auth_page():
    st.markdown("<h1 style='color:white;'>🔐 Login System</h1>", unsafe_allow_html=True)

    choice = st.selectbox("Select Option", ["Login", "Register"])

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if choice == "Login":
        if st.button("Login"):
            if login_user(username, password):
                st.session_state.logged_in = True
                st.success("Login Successful")
            else:
                st.error("Invalid Credentials")

    else:
        if st.button("Register"):
            add_user(username, password)
            st.success("Account Created")

# ---------------- PREDICTION ----------------
def prediction_page():
    st.markdown("<h1 style='color:white;'>❤️ Heart Disease Prediction</h1>", unsafe_allow_html=True)

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        age = st.slider("Age", 18, 80)
        gender = st.selectbox("Gender", ["Male", "Female"])
        height = st.slider("Height (cm)", 140, 200)
        weight = st.slider("Weight (kg)", 40, 120)

    with col2:
        bp = st.selectbox("Blood Pressure", ["Low", "Normal", "High"])
        chol = st.selectbox("Cholesterol", ["Normal", "High", "Very High"])
        sugar = st.selectbox("Sugar Level", ["Normal", "High", "Very High"])
        smoke = st.selectbox("Smoking", ["No", "Yes"])
        alco = st.selectbox("Alcohol", ["No", "Yes"])
        active = st.selectbox("Physical Activity", ["Yes", "No"])

    if st.button("🔍 Predict"):

        # -------- CONVERT --------
        gender = 1 if gender == "Male" else 2

        if bp == "Low":
            ap_hi, ap_lo = 100, 70
        elif bp == "Normal":
            ap_hi, ap_lo = 120, 80
        else:
            ap_hi, ap_lo = 150, 100

        cholesterol = {"Normal":1, "High":2, "Very High":3}[chol]
        glucose = {"Normal":1, "High":2, "Very High":3}[sugar]

        smoke = 1 if smoke == "Yes" else 0
        alco = 1 if alco == "Yes" else 0
        active = 1 if active == "Yes" else 0

        # -------- MODEL --------
        data = np.array([[age, gender, height, weight,
                          ap_hi, ap_lo,
                          cholesterol, glucose,
                          smoke, alco, active]])

        data = scaler.transform(data)

        prediction = model.predict(data)[0]
        probability = model.predict_proba(data)[0]

        # -------- OUTPUT --------
        st.markdown("## 📊 Result")

        if prediction == 1:
            st.error("⚠️ HIGH RISK")
        else:
            st.success("✅ LOW RISK")

        st.metric("Confidence", f"{max(probability)*100:.2f}%")
        st.bar_chart(probability)

# ---------------- MAIN ----------------
if st.session_state.logged_in:
    prediction_page()

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
else:
    auth_page()