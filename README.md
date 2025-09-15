# Multiple Disease Prediction System using Machine Learning

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Framework](https://img.shields.io/badge/Framework-Streamlit-red.svg)
![Libraries](https://img.shields.io/badge/Libraries-Scikit--learn%20%7C%20Pandas-green.svg)

A user-friendly web application built with Streamlit that leverages machine learning to predict the likelihood of three common diseases: **Diabetes**, **Heart Disease**, and **Parkinson's Disease**.

---

## 📋 Features

-   **Three Prediction Models:**
    -   💉 **Diabetes Prediction:** Predicts the onset of diabetes based on diagnostic measures.
    -   ❤️ **Heart Disease Prediction:** Predicts the presence of heart disease based on clinical parameters.
    -   🧠 **Parkinson's Prediction:** Predicts Parkinson's disease using advanced voice signal measurements.
-   **Interactive Web Interface:** A clean and simple UI built with Streamlit that allows users to input their health metrics and get instant predictions.
-   **Reproducible Models:** The Jupyter notebooks used for data analysis, preprocessing, and model training are included, ensuring full transparency and reproducibility.
-   **Saved Models:** Trained models are saved using Pickle for fast and efficient deployment in the web app.

---

## 📂 Project Structure

```
.
├── saved_models/
│   ├── diabetes_model.sav
│   ├── heart_disease_model.sav
│   └── parkinsons_model.sav
├── notebooks/
│   ├── 01_diabetes_prediction.ipynb
│   ├── 02_heart_disease_prediction.ipynb
│   └── 03_parkinsons_prediction.ipynb
├── app.py                      # Main Streamlit application file
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## 🛠️ Setup and Installation

Follow these steps to set up and run the project on your local machine.

### Prerequisites

-   Python 3.9 or higher
-   `pip` package manager

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## 🚀 Usage

Once the installation is complete, you can run the Streamlit application.

1.  **Navigate to the project directory** in your terminal.
2.  **Run the following command:**
    ```bash
    streamlit run app.py
    ```
3.  Open your web browser and go to the local URL provided by Streamlit (usually `http://localhost:8501`).

---

## 🧠 Model Details

### 1. Diabetes Prediction

-   **Dataset:** PIMA Indians Diabetes Dataset.
-   **Model:** Support Vector Machine (SVM) with a linear kernel.
-   **Features:** `Pregnancies`, `Glucose`, `BloodPressure`, `SkinThickness`, `Insulin`, `BMI`, `DiabetesPedigreeFunction`, `Age`.

### 2. Heart Disease Prediction

-   **Dataset:** Cleveland Heart Disease dataset from UCI Machine Learning Repository.
-   **Model:** Logistic Regression.
-   **Features:** `age`, `sex`, `cp` (chest pain type), `trestbps`, `chol`, `fbs`, `restecg`, `thalach`, `exang`, `oldpeak`, `slope`, `ca`, `thal`.

### 3. Parkinson's Disease Prediction

-   **Dataset:** UCI ML Parkinson's Dataset, based on voice measurements.
-   **Model:** Support Vector Machine (SVM) with a linear kernel.
-   **Features:** A total of 22 voice measure features, including `MDVP:Fo(Hz)`, `MDVP:Fhi(Hz)`, `MDVP:Jitter(%)`, `MDVP:Shimmer`, `HNR`, `RPDE`, `DFA`, and `PPE`.

---
