# Post Discharge Medical AI Assistant

A sophisticated **Agentic RAG (Retrieval-Augmented Generation)** system designed to support patients during their post-discharge recovery. This application bridges the gap between hospital care and home recovery by providing intelligent, context-aware assistance for medical queries, appointment scheduling, and health monitoring.

---

## � How It Works: The Agentic Architecture

This application is not just a simple chatbot; it is a **Multi-Agent System** built with **LangGraph**. It consists of specialized agents that collaborate to handle user requests intelligently.

### 1. The Workflow
The system follows a state-based workflow:

1.  **Receptionist Agent (The Gatekeeper)**
    *   **Role**: Acts as the first point of contact.
    *   **Responsibilities**: 
        *   Identifies the patient (asks for name).
        *   Retrieves patient records from the SQLite database.
        *   Handles general queries (appointments, well-being checks).
        *   **Crucial Step**: If the user asks a *medical question* (e.g., "Can I eat bananas?", "My legs are swelling"), the Receptionist detects this and initiates a **Handoff**.

2.  **The Router**
    *   **Role**: Traffic controller.
    *   **Logic**: Monitors the `handoff_to_clinical` flag. If set to `True`, it seamlessly transfers the conversation state (including patient history) to the Clinical Agent.

3.  **Clinical Agent (The Specialist)**
    *   **Role**: Handles medical and health-related queries.
    *   **Tools**:
        *   **`rag_tool`**: Queries a local Vector Database (ChromaDB) containing verified medical documents (e.g., Nephrology guidelines). It uses this for questions about diet, symptoms, and standard care.
        *   **`web_search_tool`**: Used *only* when the user explicitly asks for "latest news", "new research", or "2024 updates".
    *   **Context**: It has access to the specific patient's medical record (medications, diagnosis) to provide personalized answers (e.g., "Since you are on *Lisinopril*, you should avoid...").

---

## 📂 Data Formats & Sample Data

### 1. Patient Data Structure
The system uses a structured SQL database (`patients.db`) to store patient profiles. Here is the format of a patient record:

```json
{
  "id": 1,
  "name": "Abhishek B Shetty",
  "discharge_date": "2024-02-01",
  "primary_diagnosis": "Chronic Kidney Disease Stage 2",
  "medications": ["Metformin 500mg", "Atorvastatin 20mg"],
  "dietary_restrictions": "Diabetic renal diet, limit sugar",
  "follow_up": "Endocrinology in 1 month",
  "warning_signs": "Dizziness, high blood sugar, swelling",
  "discharge_instructions": "Check blood sugar daily, maintain diet."
}
```

### 2. Medical Knowledge Base (RAG Data)
*   **Source**: `backend/data/nephrology_reference.txt`
*   **Content**: Contains clinical guidelines for managing Chronic Kidney Disease (CKD), dietary restrictions for different stages, medication side effects, and warning signs.
*   **Storage**: This text is chunked, embedded using **HuggingFace Embeddings**, and stored in **ChromaDB** for fast semantic retrieval.

---

## 🧪 Sample Patients for Testing

The database is pre-seeded with specific profiles you can use to test different scenarios.

| Name | Condition | Key Scenario to Test |
| :--- | :--- | :--- |
| **Abhishek B Shetty** | CKD Stage 2 (Diabetic) | **Dietary Query**: *"Can I eat sweets?"* (Should reference diabetic diet)<br>**Medication**: *"What is Metformin for?"* |
| **John Smith** | CKD Stage 3 | **Symptom Check**: *"I have swelling in my legs."* (Should trigger warning signs check)<br>**Diet**: *"Is salt okay?"* (Should reference low sodium) |
| **James Smith** | CKD Stage 4 | **Severe Case**: *"I feel breathless."* (Should advise immediate medical attention) |

*(Note: There are ~30 other random patients seeded with names like "Mary Johnson", "Robert Davis", etc.)*

---

## 🚀 Getting Started

### Prerequisites
*   Node.js (v18+)
*   Python (v3.9+)
*   Google Gemini API Key (for the LLM)

### 1. Backend Setup

1.  **Navigate to backend:**
    ```bash
    cd backend
    ```

2.  **Create Virtual Environment:**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment:**
    Create a `.env` file in `backend/`:
    ```env
    GOOGLE_API_KEY=your_gemini_api_key_here
    ```

5.  **Seed Database & Ingest RAG Data:**
    This script creates the SQLite DB and ingests the medical text into ChromaDB.
    ```bash
    python scripts/seed_patients.py
    python app/rag/ingest.py
    ```

6.  **Run Server:**
    ```bash
    uvicorn app.main:app --reload
    ```

### 2. Frontend Setup

1.  **Navigate to frontend:**
    ```bash
    cd frontend
    ```

2.  **Install Dependencies:**
    ```bash
    npm install
    ```

3.  **Run Development Server:**
    ```bash
    npm run dev
    ```

4.  **Open App**: Go to `http://localhost:5173`

---

## 🛠️ Tech Stack

*   **Orchestration**: LangGraph (Multi-Agent State Machine)
*   **LLM**: Google Gemini Flash 2.5
*   **Vector Store**: ChromaDB
*   **Embeddings**: HuggingFace (`all-MiniLM-L6-v2`)
*   **Backend**: FastAPI, SQLAlchemy
*   **Frontend**: React, TypeScript, Vite (Vanilla CSS)

## 📄 License
MIT