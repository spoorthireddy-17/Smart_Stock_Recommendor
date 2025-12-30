import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Smart Stock Recommendation System",
    page_icon="📈",
    layout="centered"
)

# ---------------- LOAD DATA ----------------
DATA_PATH = "data/processed/stock_features.csv"

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

df = load_data()

# ---------------- SIDEBAR NAVIGATION ----------------
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio(
    "Go to",
    ["🏠 Home", "📊 Dashboard", "📈 Stock Recommendation", "📊 Visualization", "ℹ️ About Project"]
)

# ---------------- HOME PAGE ----------------
if page == "🏠 Home":
    st.title("📈 Smart Stock Recommendation System")

    st.markdown("""
    ### Welcome 👋
    This application provides **risk-aware stock recommendations**
    using **data-driven financial analysis**.

    #### 🔹 Key Highlights
    - Quantile-based risk classification
    - Balanced Low / Medium / High risk groups
    - Interactive stock recommendations
    - Visual risk–return analysis

    👉 Use the sidebar to explore different sections.
    """)

# ---------------- DASHBOARD PAGE ----------------
elif page == "📊 Dashboard":
    st.title("📊 Dashboard Overview")

    # ---------- METRICS ----------
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Stocks", df.shape[0])
    col2.metric("Low Risk Stocks", (df["risk_level"] == "Low Risk").sum())
    col3.metric("Medium Risk Stocks", (df["risk_level"] == "Medium Risk").sum())
    col4.metric("High Risk Stocks", (df["risk_level"] == "High Risk").sum())

    st.markdown("---")

    # ---------- RISK DISTRIBUTION ----------
    st.subheader("📊 Stock Distribution by Risk Level")

    risk_counts = df["risk_level"].value_counts().sort_index()

    fig1, ax1 = plt.subplots()
    ax1.bar(risk_counts.index, risk_counts.values)
    ax1.set_xlabel("Risk Level")
    ax1.set_ylabel("Number of Stocks")
    ax1.set_title("Risk Level Distribution")

    st.pyplot(fig1)

    st.markdown("---")

    # ---------- AVERAGE RETURN PER RISK ----------
    st.subheader("📈 Average Return per Risk Level")

    avg_returns = df.groupby("risk_level")["avg_return"].mean().sort_index()

    fig2, ax2 = plt.subplots()
    ax2.bar(avg_returns.index, avg_returns.values)
    ax2.set_xlabel("Risk Level")
    ax2.set_ylabel("Average Return")
    ax2.set_title("Average Return by Risk Category")

    st.pyplot(fig2)

    st.markdown("---")

    # ---------- OVERALL RISK VS RETURN ----------
    st.subheader("⚖️ Risk vs Return Overview")

    fig3, ax3 = plt.subplots()
    ax3.scatter(
        df["volatility"],
        df["avg_return"],
        alpha=0.3
    )

    ax3.set_xlabel("Volatility (Risk)")
    ax3.set_ylabel("Average Return")
    ax3.set_title("Overall Risk vs Return Distribution")

    st.pyplot(fig3)

# ---------------- STOCK RECOMMENDATION PAGE ----------------
elif page == "📈 Stock Recommendation":
    st.title("📈 Stock Recommendation")

    risk_choice = st.selectbox(
        "Select Risk Appetite",
        ["Low Risk", "Medium Risk", "High Risk"]
    )

    num_stocks = st.slider(
        "Number of stocks to display",
        min_value=5,
        max_value=50,
        value=10
    )

    # Filter stocks by risk level
    filtered = df[df["risk_level"] == risk_choice]

    st.write(
        "Total stocks available in this risk level:",
        filtered.shape[0]
    )

    if st.button("Get Recommendations"):
        result = filtered.sort_values(
            "avg_return", ascending=False
        ).head(num_stocks)

        st.subheader(f"Top {num_stocks} Recommended Stocks ({risk_choice})")

        st.dataframe(
            result[["stock", "avg_return", "volatility", "risk_score"]]
            .reset_index(drop=True)
        )

        # Download option
        csv = result.to_csv(index=False).encode("utf-8")
        st.download_button(
            "📥 Download Recommendations",
            csv,
            "stock_recommendations.csv",
            "text/csv"
        )

# ---------------- VISUALIZATION PAGE ----------------
elif page == "📊 Visualization":
    st.title("📊 Risk vs Return Analysis")

    risk_choice = st.selectbox(
        "Select Risk Level",
        ["Low Risk", "Medium Risk", "High Risk"]
    )

    filtered = df[df["risk_level"] == risk_choice].sort_values(
        "avg_return", ascending=False
    ).head(30)

    fig, ax = plt.subplots()
    ax.scatter(
        filtered["volatility"],
        filtered["avg_return"],
        alpha=0.7
    )

    ax.set_xlabel("Volatility (Risk)")
    ax.set_ylabel("Average Return")
    ax.set_title(f"Risk vs Return ({risk_choice})")

    st.pyplot(fig)
    
    # ---------------- RISK DISTRIBUTION BAR CHART ----------------
    st.subheader("📊 Stock Distribution Across Risk Levels")

    risk_counts = df["risk_level"].value_counts().sort_index()

    fig2, ax2 = plt.subplots()
    ax2.bar(
        risk_counts.index,
        risk_counts.values
    )

    ax2.set_xlabel("Risk Level")
    ax2.set_ylabel("Number of Stocks")
    ax2.set_title("Distribution of Stocks by Risk Category")

    st.pyplot(fig2)


# ---------------- ABOUT PAGE ----------------
elif page == "ℹ️ About Project":
    st.title("ℹ️ About This Project")

    st.markdown("""
    **Project Title:** Smart Stock Recommendation System  

    **Domain:** Machine Learning + Finance  

    **Description:**  
    This system analyzes historical NSE stock data and computes
    a composite **risk score** using return–volatility characteristics.
    Stocks are classified into **Low, Medium, and High risk categories**
    using **quantile-based classification**, ensuring balanced and
    interpretable risk groups.

    **Technologies Used:**
    - Python
    - Pandas, NumPy
    - Streamlit
    - Matplotlib

    **Use Case:**  
    Helps investors make informed decisions based on their
    risk appetite.
    """)

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("Built using Python, Machine Learning (Quantile-based), and Streamlit")