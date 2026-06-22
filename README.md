

# 🚀 AI/ML Career Guidance System (Flask Backend + LLM + ML Model)

## 📌 Overview

This project is a Flask-based backend system that powers an AI-driven Career Guidance platform. It connects an existing HTML frontend with a trained Machine Learning model and an external LLM chatbot (OpenAI / Gemini) to provide intelligent career predictions, resume analysis, and conversational guidance.

The system is designed as a **portfolio-level full-stack AI application** with modular backend architecture.

## 🧠 Key Features

### 🎯 Career Prediction Engine

* Uses a trained **Random Forest Classifier**
* Accepts user skill/attribute input via API
* Returns **top 3 career predictions with probabilities**
* Handles encoding, validation, and unseen values

### 💬 AI Career Chatbot

* Integrated with **OpenAI / Google Gemini APIs**
* Provides personalized career guidance
* Maintains conversation history (frontend-managed)
* Uses strict **career-focused system prompt**

### 🔐 Authentication System

* User registration, login, logout APIs
* Passwords stored using **secure hashing**
* Session-based token authentication (in-memory)

### 📄 Resume Analysis

* Supports `.txt`, `.pdf`, `.doc`, `.docx` uploads
* Extracts or processes content for career suggestions
* Enforces file size and format validation

### 📊 System Monitoring

* `/api/health` → backend & model status
* `/api` → API discovery endpoint

### 🧩 Model Persistence

* Trained ML model saved using `joblib`
* Encoders and feature columns stored in `/models`
* Fast startup without retraining


## 🏗️ System Architecture

```
Frontend (HTML)
   ↓
Flask Backend (app.py)
   ↓
------------------------------------------------
| Prediction Engine | Chatbot Service | Auth   |
------------------------------------------------
   ↓              ↓
 ML Model      LLM API (OpenAI / Gemini)
```

## 🧱 Project Structure

```
.
├── app.py
├── config.py
├── requirements.txt
├── .env.example
├── models/
│   ├── rf_model.joblib
│   ├── label_encoders.joblib
│   └── feature_names.joblib
│
├── routes/
│   ├── auth.py
│   ├── predict.py
│   ├── chat.py
│   ├── resume.py
│   └── health.py
│
├── services/
│   ├── prediction.py
│   ├── chatbot.py
│   ├── auth.py
│   └── key_manager.py
│
└── users.db
```

## 🔌 API Endpoints

### Auth

* `POST /api/auth/register`
* `POST /api/auth/login`
* `POST /api/auth/logout`

### Prediction

* `POST /api/predict`
* `GET /api/model/features`

### Chatbot

* `POST /api/chat`

### Resume

* `POST /api/resume/analyze`

### System

* `GET /api/health`
* `GET /api`

## ⚙️ Tech Stack

* Python 3
* Flask
* Scikit-learn (Random Forest)
* Joblib (Model Serialization)
* SQLite (User Database)
* OpenAI / Google Gemini API
* Flask-CORS
* dotenv

## 🔐 Environment Variables

Create a `.env` file:

```
LLM_PROVIDER=openai

OPENAI_API_KEY=your_key_here
GEMINI_API_KEY=your_key_here

FLASK_SECRET_KEY=your_secret_key

FLASK_HOST=127.0.0.1
FLASK_PORT=5000
FLASK_DEBUG=true
```

## ▶️ Run the Project

```bash
# Install dependencies
pip install -r requirements.txt

# Run server
python app.py
```

## 📈 Design Highlights

* Modular **service-based architecture**
* Secure API key management using environment variables
* Stateless chatbot design with history passed from frontend
* Robust error handling with consistent JSON responses
* Supports multiple LLM providers (OpenAI / Gemini)
* Lightweight SQLite-based authentication system


## 🎯 Project Goal

To build an intelligent career guidance system that combines:

* Machine Learning (career prediction)
* Generative AI (chatbot guidance)
* Web backend engineering (Flask APIs)

  - <img width="919" height="436" alt="image" src="https://github.com/user-attachments/assets/ed1e7e07-832f-49e2-b494-2c295c8387f4" />


## 📌 Status

✔ Backend Design Completed
✔ API Structure Defined
✔ ML Integration Ready
# Random Forest Model Training

## Quick Start
### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```
### Step 2: Run the Model Training Script
```bash
python random_forest_model.py
```

## What the Script Does
1. **Loads Dataset**: Reads the Excel file `career data_ set.csv (1).xlsx`
2. **Explores Data**: Shows dataset shape, info, and missing values
3. **Preprocessing**:
   - Handles missing values (median for numeric, mode for categorical)
   - Encodes categorical variables using LabelEncoder
4. **Splits Data**: 80% training, 20% testing
5. **Trains Model**: Random Forest with 100 trees
6. **Evaluates**: Shows accuracy, classification report, and confusion matrix
7. **Visualizes**: Creates feature importance and confusion matrix plots

## Output
- **Console Output**: Accuracy, classification metrics
- **feature_importance.png**: Top 10 most important features
- **confusion_matrix.png**: Confusion matrix visualization

## Model Parameters (Customizable)
- `n_estimators`: Number of trees (default: 100)
- `max_depth`: Max tree depth (default: 15)
- `min_samples_split`: Min samples to split (default: 5)
- `min_samples_leaf`: Min samples at leaf (default: 2)
- `test_size`: Test set percentage (default: 0.2)

## Results Interpretation
- **Accuracy**: Percentage of correct predictions
- **Precision**: True positives / (True positives + False positives)
- **Recall**: True positives / (True positives + False negatives)
- **F1-Score**: Harmonic mean of precision and recall


✔ LLM Chatbot Integrated
<img width="929" height="433" alt="image" src="https://github.com/user-attachments/assets/fb9954a5-9442-4847-801f-8ecb0aa0f290" />


