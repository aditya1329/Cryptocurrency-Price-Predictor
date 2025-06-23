#  Cryptocurrency Price Prediction using Machine Learning

This project aims to predict the prices of cryptocurrencies using historical data and machine learning techniques. It involves data preprocessing, exploratory data analysis (EDA), feature engineering, model building, evaluation, and visualization.

---

# Features

- Fetches and processes historical cryptocurrency price data
- Applies multiple ML models: Linear Regression, Random Forest, and LSTM
- Compares models using evaluation metrics like RMSE
- Visualizes trends and predictions using Matplotlib
- Modular and scalable code structure

---

## 📁 Project Structure

crypto-price-predictor/
├── data/ # Raw and processed data
├── notebooks/ # Jupyter Notebooks for EDA and modeling
├── models/ # Saved ML models
├── results/ # Prediction results and plots
├── crypto_predictor.py # Main script
├── requirements.txt # Python dependencies
└── README.md # Project overview


---

##  Machine Learning Models Used

- 📉 **Linear Regression**: Baseline model for trend prediction
- 🌳 **Random Forest Regressor**: Captures non-linear relationships
- 🧠 **LSTM (Long Short-Term Memory)**: Captures time dependencies in sequential price data

---

##  Tech Stack

- **Languages**: Python
- **Libraries**: Pandas, NumPy, Scikit-learn, TensorFlow/Keras, Matplotlib
- **Tools**: Jupyter Notebook, Git

---

##  Evaluation Metrics

- **RMSE** (Root Mean Squared Error)
- **MAE** (Mean Absolute Error)
- **Visualization** of actual vs predicted values

---

##  Installation

```bash
git clone https://github.com/aditya1329/crypto-price-predictor.git
cd crypto-price-predictor
pip install -r requirements.txt
