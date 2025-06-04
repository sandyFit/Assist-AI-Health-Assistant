**Assist** project for the TRAE AI IDE Hackathon:

---

# 🩺 Assist — AI Health Assistant 

A guided AI-powered query and response flow for diabetes patient health support—ensuring clinical safety through a **doctor-in-the-loop** approach.

---

## 📌 Overview

**Assist — AI Health Assistant** is a prototype system designed to streamline how diabetes patients ask health-related questions, receive guidance powered by AI, and ultimately get reviewed responses from licensed doctors.
Built with **Streamlit** as the frontend interface, a **Langgraph AI assistant** as the reasoning engine, and [database pending selection] for secure data storage, the system supports traceability, privacy, and medical accountability.

---

## 🎯 Key Features

* 🧑‍⚕️ **Doctor-reviewed AI suggestions**
* 🧾 **Support for lab result uploads (PDF/Image)**
* 📜 **Conversation history and response logging**
* 🔐 **Secure patient login and query submission**
* ⚙️ **Seamless frontend–backend–database integration**

---

## 🧩 System Components

| Component          | Description                                                              |
| ------------------ | ------------------------------------------------------------------------ |
| **Patient**        | End-user submitting health questions.                                    |
| **Doctor**         | Healthcare provider reviewing and validating responses.                  |
| **Frontend**       | Built with **Streamlit**, provides the UI for both patients and doctors. |
| **System Backend** | Python with Langgraph flow for AI processing and decision logic.         |
| **Database**       | The database stores patient data, history, queries, and responses securely. |

---

## 🔄 Flow Summary

1. **Patient Interaction:**

   * Logs in, submits a health query (optionally uploads lab results).
   * Frontend sends data to backend → backend logs the query in the database.

2. **AI Draft Phase:**

   * Backend fetches patient history and processes the query using Langgraph.
   * A draft response is generated and saved in the database.

3. **Doctor Review:**

   * Doctor logs in, sees pending queries.
   * Reviews and either **approves**, **edits**, or **rewrites** the AI response.

4. **Final Response:**

   * Approved response is delivered back to the patient.
   * System logs all decisions and transitions for traceability.

---

## 🔐 Data Handling & Privacy

* All data (queries, responses, lab files) are securely stored and linked to patient IDs.
* Each step in the query-response cycle is logged in the database.
* Doctors are the final decision-makers; as the project's name implies, AI only assists.

---

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io)
* **Backend:** Python, [Langgraph](https://www.langgraph.dev/)
* **Database:** Pending selection (Firestore, Supabase, etc.)
* **Cloud Storage:** Pending selection (AWS S3, Streamlit, etc.)

---

## 👨‍⚕️ Roles & Contributors

| Role                   | Description                                             |
|------------------------|---------------------------------------------------------|
| **Frontend (UI/UX)**   | Patient/Doctor dashboards & interactions                |
| **Backend/AI Logic**   | Langgraph pipeline, Firestore logic                     |
| **Pitch/Story**        | Demo script, messaging, presentation                    |
| **Docs & Setup**       | Repo setup, README, onboarding docs                     |
| **Integrator + QA/Testing** | Glue the parts, test the flow, polish the demo     |


---

## 📽️ Demo & Presentation

> *Will include link to video presentation.*

---

## 📄 License

MIT License.

---
