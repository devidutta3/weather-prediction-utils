# 🌦️ Weather Prediction using Machine Learning & FastAPI

A production-ready Weather Prediction API built using **Python**, **Scikit-learn**, and **FastAPI**. The project predicts the **average temperature** based on historical weather and geographical features using a machine learning pipeline.

---

## 📌 Features

* Predicts **Average Temperature**
* End-to-End Machine Learning Pipeline
* Automatic Data Preprocessing
* One-Hot Encoding using `ColumnTransformer`
* Linear Regression Model
* FastAPI REST API
* Interactive Swagger Documentation
* Production-ready Model Serialization with Joblib

---

## 🛠️ Tech Stack

| Category         | Technologies  |
| ---------------- | ------------- |
| Language         | Python 3.x    |
| Machine Learning | Scikit-learn  |
| Data Processing  | Pandas, NumPy |
| API Framework    | FastAPI       |
| Model Storage    | Joblib        |
| Server           | Uvicorn       |
| Validation       | Pydantic      |

---

# 📂 Project Structure

```text
weather-prediction-utils/
│
├── api/
│   ├── main.py
│   ├── predictor.py
│   └── schema.py
│
├── data/
│
├── models/
│   └── weather_prediction_model.pkl
│
├── src/
│   └── weather_ai/
│
├── train_model.py
├── README.md
└── LICENSE
```

---

# 📊 Dataset Features

The model is trained using the following features:

| Feature             |
| ------------------- |
| Minimum Temperature |
| Maximum Temperature |
| Wind Speed          |
| Air Pressure        |
| Elevation           |
| Latitude            |
| Longitude           |
| Rainfall            |
| Season              |
| Station Name        |
| State               |
| District            |
| Year                |
| Month Number        |
| Day                 |

Target Variable:

* **Average Temperature**

---

# ⚙️ Machine Learning Pipeline

The project uses a Scikit-learn Pipeline.

```
Raw Data
     │
     ▼
Feature Engineering
     │
     ▼
ColumnTransformer
     │
     ├── Numerical Features
     └── OneHotEncoder
     │
     ▼
Linear Regression
     │
     ▼
Model Serialization (.pkl)
```

---

# 📈 Model Performance

| Metric   | Value      |
| -------- | ---------- |
| MAE      | **0.8788** |
| MSE      | **2.0237** |
| RMSE     | **1.4226** |
| R² Score | **0.9315** |

The model explains approximately **93.15%** of the variance in the dataset.

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/your-username/weather-prediction-utils.git
```

Move into the project directory

```bash
cd weather-prediction-utils
```

Create a virtual environment

```bash
python -m venv .env
```

Activate the virtual environment

### Windows

```bash
.env\Scripts\activate
```

### Linux / macOS

```bash
source .env/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Train the Model

```bash
python train_model.py
```

The trained model will be saved in:

```
models/weather_prediction_model.pkl
```

---

# ▶️ Run the FastAPI Server

```bash
python -m uvicorn api.main:app --reload
```

Open your browser:

```
http://127.0.0.1:8000/docs
```

Swagger UI will open automatically.

---

# 📩 Example API Request

```json
{
  "min_temp": 25.5,
  "max_temp": 34.2,
  "wind_speed": 8.5,
  "air_pressure": 1012.3,
  "elevation": 45,
  "latitude": 20.2961,
  "longitude": 85.8245,
  "rainfall": 2.5,
  "season": "Summer",
  "station_name": "Bhubaneswar",
  "state": "Odisha",
  "district": "Khordha",
  "year": 2025,
  "month_number": 7,
  "day": 27
}
```

---

# 📤 Example Response

```json
{
  "Predicted Average Temperature": 29.49
}
```

---

# 🧠 Future Improvements

* Random Forest Regressor
* XGBoost Regressor
* Feature Importance Analysis
* Model Versioning
* Docker Support
* CI/CD Pipeline
* Cloud Deployment
* Real-Time Weather Data Integration
* Logging & Monitoring
* Automated Retraining Pipeline

---

# 👨‍💻 Author

**Devidutta Das**

**Founder – CodeUdaan**

* AI & Machine Learning Enthusiast
* FastAPI Developer
* Machine Learning Engineer

---

# 📜 License

This project is licensed under the MIT License.

---

# ⭐ Support

If you found this project useful:

* ⭐ Star the repository
* 🍴 Fork the project
* 🛠️ Contribute improvements
* 📢 Share it with the community

Happy Coding! 🚀
