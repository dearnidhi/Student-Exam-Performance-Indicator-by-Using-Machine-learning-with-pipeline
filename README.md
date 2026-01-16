# 🎓 Student Exam Performance Indicator (ML Pipeline)

This project is an **end-to-end machine learning application** that predicts student exam performance based on academic and demographic features. It demonstrates the complete ML lifecycle including data ingestion, preprocessing, model training, prediction pipeline, and deployment setup.

The project is structured using a modular pipeline-based approach, making it suitable for real-world ML systems and production deployment.

---

## 🚀 Features

- End-to-end machine learning pipeline
- Data ingestion, transformation, and model training
- Prediction pipeline for inference
- Modular project structure
- Web-based prediction interface (templates)
- Deployment-ready configuration (Azure App Service)
- Experiment tracking artifacts

---

## 🧠 Project Workflow

1. **Data Ingestion**
   - Load and validate raw student performance data

2. **Data Transformation**
   - Handle missing values
   - Feature encoding and scaling

3. **Model Training**
   - Train ML models using pipeline architecture
   - Save trained models as artifacts

4. **Prediction Pipeline**
   - Load trained model
   - Predict student performance on new input data

5. **Deployment**
   - Application configured for cloud deployment (Azure)

---

## 📂 Project Structure

```text
Student-Exam-Performance-Indicator/
│
├── src/                  # Core ML pipeline code
├── notebook/             # Experiments and EDA
├── templates/            # HTML templates for UI
├── artifacts/            # Trained models and outputs
├── catboost_info/        # Model training logs
├── application.py        # Main application entry point
├── requirements.txt      # Project dependencies
├── setup.py              # Package setup
└── README.md             # Project documentation

▶️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/dearnidhi/Student-Exam-Performance-Indicator-by-Using-Machine-learning-with-pipeline.git
cd Student-Exam-Performance-Indicator-by-Using-Machine-learning-with-pipeline

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
python application.py

🛠️ Tech Stack
Python
Machine Learning (Scikit-learn / CatBoost)
Pandas, NumPy
Jupyter Notebook
Flask (for deployment interface)
Azure App Service

⚠️ Notes
Project is intended for learning and demonstration purposes
Dataset quality directly impacts prediction accuracy
Not meant for real academic evaluation or decision-making
