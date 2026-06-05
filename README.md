# AI Resume ATS Analyzer 🚀

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Groq](https://img.shields.io/badge/Groq-LLM-green)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

An end-to-end AI-powered Resume Analysis Platform that helps candidates optimize resumes for Applicant Tracking Systems (ATS), improve job matching, generate interview questions, create tailored cover letters, and track ATS performance over time.

---

## 📌 Overview

AI Resume ATS Analyzer is a Streamlit-based application that combines Large Language Models (LLMs), NLP, SQLite, and interactive analytics to provide intelligent resume evaluation and career enhancement recommendations.

The platform allows users to:

- Upload Resume PDFs
- Upload or Paste Job Descriptions
- Analyze ATS Compatibility
- Generate Improved Resumes
- Create Tailored Cover Letters
- Generate Interview Questions
- Build Personalized Learning Roadmaps
- Track ATS Performance History
- Visualize Insights Through Interactive Dashboards

---

# ✨ Features

## 📄 Resume Parsing

- PDF Resume Upload
- Resume Text Extraction
- Skill & Experience Processing

## 🎯 ATS Analysis

- ATS Compatibility Score
- Skill Match Percentage
- Missing Keyword Detection
- Resume Improvement Suggestions

## ✍️ Resume Rewriter

- AI-Powered Resume Enhancement
- ATS-Friendly Content Optimization
- Downloadable Improved Resume PDF

## 🎤 Interview Question Generator

- Technical Questions
- Behavioral Questions
- Role-Specific Preparation

## 🗺️ Improvement Roadmap

- Skill Gap Analysis
- Learning Recommendations
- Personalized Career Growth Plan

## 📨 Cover Letter Generator

- AI-Generated Cover Letters
- Resume + JD Based Personalization

## 📊 ATS Insights Dashboard

- ATS Score Trends
- Historical Analysis Tracking
- Match Percentage Comparison
- Performance Prediction
- Interactive Visualizations

## 💾 Database Integration

- SQLite Storage
- ATS History Tracking
- Candidate Progress Monitoring

## 🧪 Automated Testing

- Pytest Unit Tests
- ATS Validation
- Service Testing

---

# 🎥 Demo

## Application Walkthrough

https://github.com/user-attachments/assets/af2560d4-d933-4e6a-be5c-2557e07378a4

### Demonstrates

- Resume Upload
- JD Upload
- ATS Analysis
- Resume Rewrite
- Interview Questions
- Roadmap Generation
- Cover Letter Generation

---

## Insights Dashboard Demo

https://github.com/user-attachments/assets/5125d07e-a1dd-4d0a-9f27-af8c87e95656

### Demonstrates

- ATS History Tracking
- ATS Trends
- Match Percentage Analytics
- Dashboard Metrics
- Performance Prediction

---

# 🖼️ Sample Generated Resume

<img width="587" height="655" alt="image" src="https://github.com/user-attachments/assets/f160745b-4ea7-4678-87b3-0b314e53be19" />
<img width="555" height="689" alt="image" src="https://github.com/user-attachments/assets/a54d044a-d026-4c49-9909-b7d920597b8b" />

---

# 🏗️ System Architecture

```text
Resume PDF
    │
    ▼
Resume Parser
    │
    ▼
AI Analysis Engine (Groq LLM)
    │
 ┌──┬────────┬─────────┬─────────┐
 ▼  ▼        ▼         ▼         ▼

ATS Rewrite Interview Roadmap Cover Letter

    │
    ▼
SQLite Database
    │
    ▼
Insights Dashboard
```

---

# 🛠️ Tech Stack

## Frontend

- Streamlit
- HTML/CSS
- Plotly

## Backend

- Python

## AI & NLP

- Groq API
- Llama Models

## Database

- SQLite

## Machine Learning

- Scikit-Learn

## Data Processing

- Pandas
- NumPy
- Regular Expressions

## Visualization

- Plotly Express

## PDF Processing

- PyPDF2
- FPDF2

## Testing

- Pytest

---

# 📂 Project Structure

```text
AI-Resume-ATS-Analyzer/
│
├── app.py
│
├── ai/
│   ├── ats_service.py
│   ├── interview_service.py
│   ├── roadmap_service.py
│   ├── cover_letter_service.py
│   ├── resume_rewriter_service.py
│   └── llm_client.py
│
├── parser/
│   ├── resume_parser.py
│   └── jd_parser.py
│
├── database/
│   └── db.py
│
├── services/
│   └── dashboard_service.py
│
├── reports/
│   └── pdf_generator.py
│
├── tests/
│   ├── test_ats.py
│   └── test_matching.py
│
├── screenshots/
│   ├── dashboard.png
│   └── improved_resume.png
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🗄️ Database Schema

```sql
CREATE TABLE CANDIDATE_ANALYSIS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME VARCHAR(100),
    ATS_SCORE INTEGER,
    MATCH_PERCENTAGE INTEGER,
    ANALYSIS_DATE TIMESTAMP
);
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/rohitganguly80/ai_resume_ATS-_analyzer.git
```

## 2. Move Into Project

```bash
cd ai_resume_ATS-_analyzer
```

## 3. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 5. Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

## 6. Run Application

```bash
streamlit run app.py
```

---

# 🧪 Running Tests

```bash
pytest
```

---

# 📈 Dashboard Analytics

The ATS Insights Dashboard provides:

- Total Analyses
- Average ATS Score
- Average Match Percentage
- Best ATS Score
- Predicted Future ATS Score
- ATS Trend Analysis
- Match Comparison
- Historical Records

---

# 🔮 Future Enhancements

- Multi Resume Comparison
- OCR Support
- Recruiter Dashboard
- Resume Ranking System
- LinkedIn Profile Analysis
- Job Recommendation Engine
- Cloud Deployment
- User Authentication

---

# 👨‍💻 Author

**Rohit Ganguly**

B.Tech Computer Science & Engineering

Interests:
- Artificial Intelligence
- Machine Learning
- Data Science
- Full Stack Development

GitHub: https://github.com/rohitganguly80

---

# 📄 License

This project is licensed under the MIT License.
