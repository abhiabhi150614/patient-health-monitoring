# Post Discharge Medical AI Assistant

A sophisticated multi-agent AI system designed to support patients during their post-discharge recovery phase. This application bridges the gap between hospital care and home recovery by providing intelligent, context-aware assistance for medical queries, appointment scheduling, and health monitoring.

## 🚀 Features

### 🤖 Multi-Agent Architecture
The system employs a LangGraph-based architecture with specialized agents:
- **Receptionist Agent**: The first point of contact. It handles patient identification, retrieves medical records, manages appointment scheduling, and answers general administrative queries.
- **Clinical Agent**: A specialized medical assistant that handles clinical queries. It has access to the patient's specific medical history, medications, and discharge instructions to provide personalized advice.
- **Router**: Intelligently routes queries between agents based on context and complexity.

### 🧠 Advanced AI Capabilities
- **RAG (Retrieval-Augmented Generation)**: Utilizes ChromaDB to store and retrieve relevant medical knowledge (e.g., nephrology references) to ground the AI's responses in verified medical data.
- **Context Awareness**: Maintains conversation history and patient state across interactions.
- **Handoff Mechanism**: Seamlessly transfers the conversation from the Receptionist to the Clinical agent when medical advice is detected.

### 🏥 Patient Management
- **Health Monitoring**: Tracks vital signs and symptoms reported by the patient.
- **Medication Tracking**: Knows the patient's specific medication schedule and dosage.
- **Dietary Guidance**: Provides advice based on the patient's specific dietary restrictions (e.g., Renal Diabetic Diet).

## 🛠️ Tech Stack

- **Backend**: Python, FastAPI, LangGraph, LangChain, SQLAlchemy, ChromaDB
- **Frontend**: React, TypeScript, Vite, TailwindCSS
- **Database**: SQLite (for patient records), ChromaDB (for vector embeddings)

## 📂 Project Structure

```
datasmith/
├── backend/
│   ├── app/
│   │   ├── agents/         # LangGraph agent definitions (Receptionist, Clinical)
│   │   ├── rag/            # RAG implementation and vector store logic
│   │   ├── routers/        # FastAPI route handlers
│   │   ├── models.py       # SQLAlchemy database models
│   │   └── db.py           # Database connection and session management
│   ├── data/               # Reference medical data for RAG
│   ├── scripts/            # Utility scripts (seeding data)
│   └── test_api.py         # Integration testing script
├── frontend/
│   ├── src/
│   │   ├── components/     # React components
│   │   └── ...
│   └── ...
└── ...
```

## 🧪 Sample Data

The system comes pre-loaded with sample patient data for testing and demonstration purposes. You can use these profiles to interact with the bot.

### 1. Abhishek B Shetty
- **Condition**: Chronic Kidney Disease Stage 2
- **Discharge Date**: Feb 1, 2024
- **Medications**: Metformin 500mg, Atorvastatin 20mg
- **Diet**: Diabetic renal diet, limit sugar
- **Warning Signs**: Dizziness, high blood sugar, swelling
- **Example Query**: *"Hi, I'm Abhishek. Can I eat bananas with my condition?"*

### 2. John Smith
- **Condition**: Chronic Kidney Disease Stage 3
- **Discharge Date**: Jan 15, 2024
- **Medications**: Lisinopril 10mg, Furosemide 20mg
- **Diet**: Low sodium (2g/day), fluid restriction (1.5L/day)
- **Example Query**: *"My legs are swelling up, what should I do?"*

*(Note: If the database is empty, run the seed script as shown below)*

## ⚡ Getting Started

### Prerequisites
- Node.js (v18+)
- Python (v3.9+)

### Backend Setup

1. **Navigate to backend:**
   ```bash
   cd backend
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Mac/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration:**
   Create a `.env` file in the `backend/` directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   # Add other keys if necessary (e.g., GOOGLE_API_KEY)
   ```

5. **Seed the Database:**
   Initialize the database with sample patients:
   ```bash
   python scripts/seed_patients.py
   ```

6. **Run the Server:**
   ```bash
   uvicorn app.main:app --reload
   ```

### Frontend Setup

1. **Navigate to frontend:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Run Development Server:**
   ```bash
   npm run dev
   ```

## ✅ Verification

To verify that the backend is working correctly and the agents are performing as expected, you can run the included test script:

1. Ensure the backend server is running (`uvicorn app.main:app --reload`).
2. In a new terminal (inside `backend/`):
   ```bash
   python test_api.py
   ```
   This script will:
   - Simulate a chat session.
   - Verify patient lookup for "Abhishek B Shetty".
   - Test the handoff mechanism from Receptionist to Clinical agent.

## 📄 License

MIT