# 🏥 Assist — Your Friendly AI Companion for Diabetes Care

**Assist** is a collaborative AI assistant that helps diabetes patients draft clear and medically informed therapy requests based on their symptoms, clinical history, and doctor recommendations.

It’s designed for fast prototyping (e.g., hackathons!) with no complex medical databases—just the power of LLMs and thoughtful human-in-the-loop review. 💡

## Features

- Query enhancement using AI
- Safety scoring for medical queries
- Automated triage system
- Doctor approval workflow
- File upload and processing (.pdf, .csv, .txt)
- Role-based access (Patient, Doctor, Admin)

## Project Structure

```
/medical-assistant-app/
├── app/                    # FastAPI backend
│   ├── main.py            # FastAPI entrypoint
│   ├── routes/            # API endpoints
│   ├── models/            # Database models
│   ├── db/                # Database connection
│   ├── agents/            # AI agent scripts
├── ui/                    # Streamlit frontend
│   ├── streamlit_app.py   # Main UI
│   ├── components/        # UI components
├── tests/                 # Test files
├── data/                  # Sample data
├── docs/                  # Documentation
├── mcp-flow.yaml          # MCP agent flow
```

## Setup Instructions

### Prerequisites

- Python 3.9+
- pip

### Installation

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up environment variables (copy `.env.example` to `.env` and fill in values)

### Running the Application

1. Start the backend API:
   ```
   streamlit run app/main.py
   ```
   The API will be available at http://localhost:8000

2. Launch the Streamlit UI in a separate terminal:
   ```
   streamlit run ui/frontend.py
   ```
   The UI will be available at http://localhost:8501

3. Seed demo data (optional):
   ```
   python seed_db.py
   ```
   Alternatively, set the environment variable `SEED_DB=true` to automatically seed the database on startup.

## API Documentation

Once the backend is running, you can access the Swagger documentation at:
```
http://localhost:8000/docs
```

## Agent Strategy

This application uses multiple specialized AI agents:

1. **Query Enhancement Agent**: Improves user queries for better results
2. **Safety Scoring Agent**: Evaluates medical advice for safety
3. **Triage Agent**: Prioritizes queries based on urgency
4. **Doctor Approval Agent**: Reviews AI responses before delivery

All agents operate within a coordinated MCP flow defined in `mcp-flow.yaml`.

## Safety Rationale

Medical advice requires careful handling. Our multi-agent approach ensures:

- All responses are vetted for medical accuracy
- Safety scores prevent potentially harmful advice
- Doctor review for critical or uncertain cases
- Clear labeling of AI-generated content

## Demo Data

The application includes sample data for demonstration purposes. Run `seed_db.py` to populate the database with mock queries, file records, and safety scores.

## Role-Based Access

The application supports three user roles:

1. **Patient**: Can submit medical queries, upload files, and view responses
2. **Doctor**: Can review and approve/reject AI-generated responses, update triage levels
3. **Admin**: Has access to all features plus system monitoring

For the demo, role selection is available in the UI sidebar without authentication.

## License

This project is intended for demonstration purposes only.
