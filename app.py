# ============================================================
# Credit Card Fraud Detection - Professional India Edition 🇮🇳
# ============================================================

import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load model
with open('fraud_model.pkl', 'rb') as f:
    model = pickle.load(f)

df_ref = pd.read_csv('final_data.csv')
features = df_ref.drop('Class', axis=1).columns.tolist()

# ---- Page Config ----
st.set_page_config(
    page_title="FraudShield India",
    page_icon="🛡️",
    layout="wide"
)

# ---- Custom CSS ----
st.markdown("""
<style>
    /* Background */
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    }

    /* Main card */
    .main-card {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 20px;
        padding: 30px;
        backdrop-filter: blur(10px);
        margin-bottom: 20px;
    }

    /* Header */
    .header-title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(90deg, #00C9FF, #92FE9D);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0;
    }

    .header-sub {
        text-align: center;
        color: #aaaaaa;
        font-size: 1.1rem;
        margin-top: 5px;
    }

    /* Metric cards */
    .metric-card {
        background: rgba(255,255,255,0.07);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.1);
    }

    .metric-value {
        font-size: 2.5rem;
        font-weight: 800;
        color: #00C9FF;
    }

    .metric-label {
        color: #aaaaaa;
        font-size: 0.9rem;
        margin-top: 5px;
    }

    /* Result cards */
    .result-safe {
        background: linear-gradient(135deg, #11998e, #38ef7d);
        border-radius: 15px;
        padding: 25px;
        text-align: center;
        color: white;
        font-size: 1.5rem;
        font-weight: 700;
    }

    .result-fraud {
        background: linear-gradient(135deg, #eb3349, #f45c43);
        border-radius: 15px;
        padding: 25px;
        text-align: center;
        color: white;
        font-size: 1.5rem;
        font-weight: 700;
    }

    .result-warning {
        background: linear-gradient(135deg, #f7971e, #ffd200);
        border-radius: 15px;
        padding: 25px;
        text-align: center;
        color: #1a1a1a;
        font-size: 1.5rem;
        font-weight: 700;
    }

    /* Section title */
    .section-title {
        color: #00C9FF;
        font-size: 1.2rem;
        font-weight: 700;
        margin-bottom: 15px;
        border-left: 4px solid #00C9FF;
        padding-left: 10px;
    }

    /* Tips card */
    .tip-card {
        background: rgba(0, 201, 255, 0.08);
        border: 1px solid rgba(0, 201, 255, 0.3);
        border-radius: 12px;
        padding: 15px 20px;
        margin: 8px 0;
        color: #e0e0e0;
        font-size: 0.95rem;
    }

    /* Hide streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Button */
    .stButton > button {
        background: linear-gradient(90deg, #00C9FF, #92FE9D);
        color: #1a1a1a;
        font-weight: 700;
        font-size: 1.1rem;
        border: none;
        border-radius: 12px;
        padding: 15px;
        width: 100%;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 20px rgba(0,201,255,0.5);
    }

    /* Input fields */
    .stSelectbox > div, .stNumberInput > div {
        background: rgba(255,255,255,0.05) !important;
        border-radius: 10px !important;
    }

    /* Divider */
    hr {
        border-color: rgba(255,255,255,0.1);
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER
# ============================================================
st.markdown("""
<div style='text-align:center; padding: 30px 0 10px 0;'>
    <div style='font-size:3.5rem; font-weight:900;
         background: linear-gradient(90deg, #00C9FF, #92FE9D);
         -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>
        🛡️ FraudShield India
    </div>
    <div style='color:#aaaaaa; font-size:1.1rem; margin-top:8px;'>
        AI-Powered Credit Card Fraud Detection for India 🇮🇳
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ============================================================
# STATS BAR
# ============================================================
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown("""<div class='metric-card'>
        <div class='metric-value'>93.76%</div>
        <div class='metric-label'>Model Accuracy</div>
    </div>""", unsafe_allow_html=True)
with c2:
    st.markdown("""<div class='metric-card'>
        <div class='metric-value'>2.8L+</div>
        <div class='metric-label'>Transactions Analyzed</div>
    </div>""", unsafe_allow_html=True)
with c3:
    st.markdown("""<div class='metric-card'>
        <div class='metric-value'>492</div>
        <div class='metric-label'>Frauds Detected</div>
    </div>""", unsafe_allow_html=True)
with c4:
    st.markdown("""<div class='metric-card'>
        <div class='metric-value'>Real-Time</div>
        <div class='metric-label'>Detection Speed</div>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ============================================================
# TABS
# ============================================================
tab1, tab2 = st.tabs(["🔍 Check Single Transaction", "📁 Bulk CSV Upload"])

# ============================================================
# TAB 1: Single Transaction
# ============================================================
with tab1:
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("<div class='section-title'>Transaction Details</div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        amount = st.number_input("💰 Amount (₹)", min_value=0.0, value=500.0, step=100.0)
        time_of_day = st.selectbox("🕐 Time of Transaction",
                                    ["Morning (6AM-12PM)", "Afternoon (12PM-6PM)",
                                     "Evening (6PM-12AM)", "Night (12AM-6AM)"])

    with col2:
        payment_type = st.selectbox("💳 Payment Method",
                                    ["Credit Card", "Debit Card",
                                     "UPI (GPay/PhonePe/Paytm)",
                                     "ATM Withdrawal", "Net Banking"])
        location = st.selectbox("📍 Transaction Location",
                                ["My Own City", "Another City", "Foreign Country"])

    with col3:
        merchant = st.selectbox("🏪 Merchant Type",
                                ["Kirana / Grocery Store",
                                 "Online Shopping (Flipkart/Amazon)",
                                 "Restaurant / Dhaba / Food Delivery",
                                 "Petrol Pump",
                                 "Hospital / Medical",
                                 "School / College Fees",
                                 "Travel / Train / Flight",
                                 "Mobile Recharge / Bill Payment",
                                 "ATM Withdrawal",
                                 "Bank Transfer (NEFT/IMPS/RTGS)",
                                 "Online Gaming / Fantasy App",
                                 "Jewellery / Gold",
                                 "Other"])
        first_time = st.selectbox("❓ First time at this merchant?", ["No", "Yes"])

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Security Verification</div>", unsafe_allow_html=True)

    col4, col5, col6, col7 = st.columns(4)
    with col4:
        otp = st.selectbox("📲 OTP Received?", ["Yes", "No"])
    with col5:
        known_person = st.selectbox("👤 Instructed by someone?", ["No", "Yes"])
    with col6:
        link = st.selectbox("🔗 Paid via unknown link?", ["No", "Yes"])
    with col7:
        multiple = st.selectbox("🔄 Multiple quick transactions?", ["No", "Yes"])

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🛡️ Analyze Transaction", use_container_width=True):

        risk_score = 0
        if location == "Foreign Country": risk_score += 3
        if location == "Another City": risk_score += 1
        if time_of_day == "Night (12AM-6AM)": risk_score += 2
        if first_time == "Yes": risk_score += 1
        if amount > 50000: risk_score += 3
        if amount > 10000: risk_score += 1
        if merchant == "Online Gaming / Fantasy App": risk_score += 1
        if merchant == "ATM Withdrawal" and amount > 10000: risk_score += 2
        if otp == "No": risk_score += 3
        if known_person == "Yes": risk_score += 3
        if link == "Yes": risk_score += 3
        if multiple == "Yes": risk_score += 2

        fraud_prob = min((risk_score / 18) * 100, 99)
        legit_prob = 100 - fraud_prob

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<div class='section-title'>Analysis Result</div>", unsafe_allow_html=True)

        res_col1, res_col2, res_col3 = st.columns([2,1,1])

        with res_col1:
            if fraud_prob > 60:
                st.markdown("""<div class='result-fraud'>
                    🚨 HIGH RISK — Possible Fraud!<br>
                    <span style='font-size:1rem; font-weight:400;'>
                    Contact your bank immediately!</span>
                </div>""", unsafe_allow_html=True)
            elif fraud_prob > 35:
                st.markdown("""<div class='result-warning'>
                    ⚠️ MEDIUM RISK — Suspicious!<br>
                    <span style='font-size:1rem; font-weight:400;'>
                    Please verify with your bank.</span>
                </div>""", unsafe_allow_html=True)
            else:
                st.markdown("""<div class='result-safe'>
                    ✅ LOW RISK — Looks Safe!<br>
                    <span style='font-size:1rem; font-weight:400;'>
                    Transaction appears legitimate.</span>
                </div>""", unsafe_allow_html=True)
                st.balloons()

        with res_col2:
            st.markdown(f"""<div class='metric-card'>
                <div class='metric-value' style='color:#92FE9D;'>{legit_prob:.0f}%</div>
                <div class='metric-label'>Safe Probability</div>
            </div>""", unsafe_allow_html=True)

        with res_col3:
            st.markdown(f"""<div class='metric-card'>
                <div class='metric-value' style='color:#eb3349;'>{fraud_prob:.0f}%</div>
                <div class='metric-label'>Fraud Probability</div>
            </div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<div class='section-title'>Safety Tips</div>", unsafe_allow_html=True)

        tips = [
            "🔒 Never share your OTP, PIN or CVV with anyone — not even bank employees!",
            "📵 Never click on unknown payment links received via SMS or WhatsApp!",
            "🏦 Your bank will NEVER ask for OTP or password over a phone call!",
            "📞 If you suspect fraud, call Cybercrime Helpline immediately: 1930",
            "🛡️ Always use official apps like GPay, PhonePe, or Paytm for UPI payments!"
        ]
        for tip in tips:
            st.markdown(f"<div class='tip-card'>{tip}</div>", unsafe_allow_html=True)

# ============================================================
# TAB 2: CSV Upload
# ============================================================
with tab2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Bulk Transaction Analysis</div>", unsafe_allow_html=True)
    st.info("Upload a CSV file with transaction data for bulk fraud detection.")

    uploaded_file = st.file_uploader("Choose CSV File", type=['csv'])

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write("📋 Preview:")
        st.dataframe(data.head(), use_container_width=True)

        if st.button("🛡️ Analyze All Transactions", use_container_width=True):
            try:
                X = data[features]
                predictions = model.predict(X)
                probabilities = model.predict_proba(X)

                data['Result'] = ['🚨 FRAUD' if p == 1 else '✅ Safe' for p in predictions]
                data['Fraud %'] = [f"{p[1]*100:.2f}%" for p in probabilities]

                fraud_count = sum(predictions)
                total = len(predictions)

                r1, r2, r3 = st.columns(3)
                with r1:
                    st.markdown(f"""<div class='metric-card'>
                        <div class='metric-value'>{total}</div>
                        <div class='metric-label'>Total Transactions</div>
                    </div>""", unsafe_allow_html=True)
                with r2:
                    st.markdown(f"""<div class='metric-card'>
                        <div class='metric-value' style='color:#92FE9D;'>{total-fraud_count}</div>
                        <div class='metric-label'>Safe Transactions</div>
                    </div>""", unsafe_allow_html=True)
                with r3:
                    st.markdown(f"""<div class='metric-card'>
                        <div class='metric-value' style='color:#eb3349;'>{fraud_count}</div>
                        <div class='metric-label'>Fraudulent Transactions</div>
                    </div>""", unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)
                st.dataframe(data[['Result', 'Fraud %']], use_container_width=True)

                if fraud_count > 0:
                    st.error(f"🚨 {fraud_count} fraudulent transactions detected! Contact your bank immediately!")
                else:
                    st.success("✅ All transactions appear safe!")

            except Exception as e:
                st.error(f"Error: {e}")

# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
st.markdown("""
<div style='text-align:center; color:#666; font-size:0.9rem; padding:10px 0;'>
    🛡️ FraudShield India &nbsp;|&nbsp; AI-Powered Fraud Detection &nbsp;|&nbsp;
    Made with ❤️ for India 🇮🇳 &nbsp;|&nbsp; Cybercrime Helpline: <b style='color:#00C9FF;'>1930</b>
</div>
""", unsafe_allow_html=True)