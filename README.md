# SmartStock_Recommendor
# OVERVIEW:
The Smart Stock Recommendation System is a data-driven application that helps users make informed investment decisions by categorizing stocks into Low, Medium, and High risk groups.
The system analyzes historical stock market data, computes risk-related metrics, and provides risk-aware recommendations through an interactive Streamlit dashboard.

# OBJECTIVES:
 Analyze historical stock market data  
 
 Compute meaningful financial risk metrics  
 
 Classify stocks into risk categories using quantile-based analysis  
 
 Provide interactive visualizations and recommendations  
 
 Build a user-friendly web application for investors

# METHODOLOGY:
**1. DATA COLLECTION:**  

 Historical NSE stock data (Kaggle)  
 
 Raw data excluded from GitHub due to size constraints  
 
**2. DATA PREPROCESSING:**  

 Cleaning and formatting  
 
 Feature engineering:  
 
    Average Return  
    
    Volatility  
    
    Risk Score (return–volatility based)  
    
**3. RISK CLASSIFICATION:**  

 Quantile-based classification (33rd & 66th percentiles)  
 
 Categorizes stocks into:  
 
    Low Risk  
    
    Medium Risk  
    
    High Risk  
    
**4. VISUALIZATION AND ANALYSIS:**  

 Risk vs Return scatter plots  
 
 Risk distribution bar charts  
 
 Dashboard summary statistics  
 
**5. DEPLOYMENT**  

 Streamlit Cloud  
 
 Uses preprocessed data for fast and reliable execution  
 

# TECHNOLOGY STACK:
 Programming Language: Python  
 
 Libraries: Pandas, NumPy, Matplotlib, Seaborn  
 
 Web Framework: Streamlit  
 
 Tools: Git, GitHub, Jupyter Notebook  
 

# APPLICATION FEATURES:
 Dashboard overview of stock risk distribution  
 
 Risk vs Return visualization  
 
 Risk-based stock recommendations  
 
 Downloadable recommendation results  
 
 Clean navigation using sidebar  
 

# SAMPLE INSIGHTS:
 Stocks are evenly distributed across risk levels
 Higher risk generally correlates with higher returns
 Quantile-based classification provides stable and interpretable results
