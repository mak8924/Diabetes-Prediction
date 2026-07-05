# Diabetes Prediction System (For Women) 🩺

## Overview
This project is an end-to-end Machine Learning web application built with **Django** and **Scikit-Learn**. It is specifically designed to predict the likelihood of a **female patient** having diabetes based on various diagnostic measurements (such as Glucose level, BMI, Age, Pregnancies, etc.).

**Important Note:** The current version of this diagnostic model is trained exclusively on female health data. Expanding the system to diagnose both genders is planned for future development.

## Developer
* **Developed by:** Malak
* **Role:** Full-Stack Developer & Machine Learning Enthusiast

## Features
* **Targeted Machine Learning Model:** Utilizes a trained ML model (`diabetes_v1_female.joblib`) specifically optimized for women's health metrics.
* **Web Interface:** A user-friendly web interface built with Django to input patient data and get instant results.
* **Data Analysis:** Includes exploratory data analysis and data preprocessing notebooks (`analysis.ipynb`).
* **Visual Reports:** Includes performance metrics and correlation matrices (available in the `reports/` folder).

## Technologies Used
* **Backend:** Python, Django
* **Machine Learning:** Scikit-Learn, Pandas, NumPy
* **Data Visualization:** Matplotlib, Seaborn
* **Frontend:** HTML, CSS, JavaScript (in Django templates)

## Project Structure
* `config/`: Django project configuration and settings.
* `prediction_app/`: The main Django application containing views, models, and URLs.
* `models/`: Contains the pre-trained Machine Learning model (`.joblib` format).
* `data/`: Contains the dataset (`diabetes.csv`) used for training and testing.
* `notebooks/`: Jupyter notebooks for exploratory data analysis (EDA).
* `reports/`: Generated graphs showing model evaluation (Confusion Matrix, Correlation).

## How to Run the Project Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mak8924/Diabetes-Prediction.git
   cd Diabetes-Prediction
   ```

2. Create a virtual environment:
   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```
   
3. Install dependencies:
   ```bash
    pip install -r requirements.txt
   ```
   
4. Apply database migrations:
   ```bash
    python manage.py migrate
   ```
   
5. Run the development server:
   ```bash
    python manage.py runserver
   ```
   
Open your browser and go to `http://127.0.0.1:8000/prediction/predict/`

## Future Work
  * Train and integrate a new model to predict diabetes for male patients.

  * Improve the user interface with more interactive elements.
