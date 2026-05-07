# Sales Forecasting System

## Project Overview

This project is a Multi-State Sales Forecasting System built using Machine Learning and Flask.

The system predicts future sales across different states using historical sales data and feature-engineered forecasting techniques.

The application provides a web interface where users can:
- Select a state
- Enter previous sales values
- Generate future sales predictions

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Flask
- HTML
- CSS
- Joblib

---

## Machine Learning Workflow

### Data Preprocessing
- Date conversion
- Sales cleaning
- Sorting by state and date
- Missing value handling

### Feature Engineering
- Lag Features
    - lag_1
    - lag_7
    - lag_30
- Rolling Features
    - rolling_mean_4
    - rolling_std_4
- Time Features
    - month
    - quarter
    - week_of_year
- State Encoding using LabelEncoder

### Model Training
The following models were explored:
- XGBoost
- ARIMA
- Prophet
- LSTM

XGBoost achieved the best performance and was selected for deployment.

---

## Model Performance

| Metric | Value |
|---|---|
| MAE | 9.5 Million |
| RMSE | 21.4 Million |

---

## Project Structure

```bash
forecasting-system/
│
├── app/
│   ├── app.py
│   ├── templates/
│   └── static/
│
├── data/
│
├── models/
│
├── notebooks/
│
├── requirements.txt
│
└── README.md
```

---

## How to Run the Project

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Virtual Environment

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Flask Application

```bash
python app/app.py
```

### 5. Open Browser

```bash
http://127.0.0.1:5000
```

---

## Features

- Multi-State Forecasting
- Professional UI
- Machine Learning Predictions
- Real-Time Forecast Generation
- Flask Deployment

---

## Future Improvements

- Automated Feature Generation
- Advanced Forecasting Pipelines
- Cloud Deployment
- Interactive Dashboards
- CatBoost / LightGBM experimentation

---

## Author

Developed as an end-to-end Machine Learning Forecasting Project.