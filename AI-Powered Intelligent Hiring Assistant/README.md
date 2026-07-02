# AI-Powered Intelligent Hiring Tool

An end-to-end AI-driven hiring system that evaluates candidate resumes against job requirements using Natural Language Processing (NLP), Machine Learning, and Deep Learning techniques. The system provides intelligent resume screening, candidate-job matching, skill gap analysis, personalized recommendations, and an interactive AI chatbot for candidate guidance.

---

## Project Overview

Traditional hiring processes often involve manual resume screening, which is time-consuming and prone to bias. This project aims to automate and improve the hiring workflow by leveraging AI for intelligent candidate evaluation.

The system analyzes resumes, compares them with job requirements, identifies strengths and missing skills, calculates a match score, and provides explainable feedback.

Additionally, it includes a conversational AI assistant that allows candidates to ask questions about their evaluation and receive personalized improvement suggestions.

---

## Key Features

- Resume preprocessing and text cleaning
- Resume semantic matching using Deep Learning
- Skill gap analysis
- Candidate-job match score generation
- Explainable AI-based feedback
- Retrieval-based intelligent chatbot
- Interactive Gradio user interface
- Live deployment on Hugging Face

---

## Problem Statement

Recruiters often face challenges such as:

- Large volume of resumes
- Time-consuming manual screening
- Difficulty identifying best-fit candidates
- Lack of personalized feedback for candidates

This project solves these problems by building an intelligent AI-powered hiring assistant.

---

## Objective

The primary objectives of this project are:

- Automate resume screening
- Evaluate resumes against job descriptions
- Measure candidate-job alignment
- Identify missing skills
- Generate actionable recommendations
- Provide an AI-based conversational interface for candidate interaction

---

## Project Workflow

```text
Resume Dataset
      ↓
EDA & Preprocessing
      ↓
Text Cleaning & Feature Engineering
      ↓
Semantic Embedding Generation
      ↓
Resume-Job Similarity Matching
      ↓
Skill Gap Analysis
      ↓
Candidate Evaluation
      ↓
AI Chatbot + Recommendations
      ↓
Deployment
```

---

## System Architecture

### 1. Data Preprocessing
- Resume dataset loading
- Data cleaning
- Text normalization
- Feature engineering

### 2. Deep Learning-Based Matching
Resume and job descriptions are converted into semantic embeddings using Sentence Transformers.

Cosine similarity is used to measure semantic alignment.

### 3. Skill Gap Analysis
Candidate skills are compared against required job skills.

Outputs:
- Matched skills
- Missing skills

### 4. Candidate Evaluation
The system generates:
- Match score
- Skill analysis
- Candidate verdict

### 5. Intelligent AI Chatbot
Candidates can ask:
- What is my score?
- What skills are missing?
- How can I improve?
- Why is my score low?

The chatbot generates explainable responses based on evaluation results.

---

## Technologies Used

### Programming Language
- Python

### Libraries & Frameworks
- Pandas
- NumPy
- Scikit-learn
- Sentence Transformers
- Gradio

### Deployment
- Hugging Face Spaces

### Development Environment
- Google Colab
- Jupyter Notebook

---

## Deep Learning Model Used

### Sentence Transformer
Model:
```python
all-MiniLM-L6-v2
```

Purpose:
- Generate semantic embeddings for resumes and job descriptions
- Compute similarity score using cosine similarity

---

## Job Role Evaluated

### Data Scientist

Required Skills:
- Python
- SQL
- Machine Learning
- Deep Learning
- TensorFlow
- Pandas
- Statistics

---

## Candidate Evaluation Metrics

The candidate evaluation is based on:

### Semantic Similarity Score
Measures how closely the resume aligns with the job description.

### Skill Match Score
Measures how many required skills are present in the resume.

### Final Evaluation Output
- Match Score
- Verdict
- Matched Skills
- Missing Skills
- Improvement Recommendations

---

## Repository Structure

```text
AI-Hiring-Tool/
│
├── notebooks/
│   ├── 01_EDA_Preprocessing.ipynb
│   └── 04_Candidate_Assistant_RAG_UI.ipynb
│
├── deployment/
│   ├── app.py
│   └── requirements.txt
│
├── screenshots/
│
└── README.md
```

---

## Notebooks Included

### EDA and Preprocessing
Covers:
- Dataset loading
- Data analysis
- Text preprocessing
- Feature engineering

### Candidate Assistant + RAG + UI
Covers:
- Semantic scoring
- Skill matching
- Candidate evaluation
- AI chatbot
- Gradio interface

---

## Live Demo

Hugging Face Deployment:

**https://huggingface.co/spaces/MDBITW/ai-hiring-tool**

---

## Screenshots

### Home Interface
<img width="1917" height="902" alt="Home Interface" src="https://github.com/user-attachments/assets/f9edb027-64e5-4c4d-82e4-bb56b9b4904d" />

### Another View 
<img width="1881" height="817" alt="Another view" src="https://github.com/user-attachments/assets/a0ee0fe0-66cf-4a1d-9759-5100fcaeb10c" />

### Candidate Input
<img width="1866" height="870" alt="Candidate Input" src="https://github.com/user-attachments/assets/99f946fb-6b5e-452d-9717-b10dbe1a33aa" />

### Candidate Evaluation Output
<img width="951" height="707" alt="Candidate Evaluation" src="https://github.com/user-attachments/assets/0f158195-d440-42ba-a3d9-9f955d414547" />

### AI Assistant Query
<img width="966" height="197" alt="Ai assistant query" src="https://github.com/user-attachments/assets/74085e97-ee8e-4e18-b14f-9b94903113d2" />

### AI Assistant Response
<img width="932" height="375" alt="Ai assistant response" src="https://github.com/user-attachments/assets/a00c904b-100c-4e77-ba88-65ba2f3a61ea" />


---

## Future Scope

Potential improvements include:

- Multi-role hiring support
- Resume PDF upload
- OCR integration
- Advanced RAG using vector databases
- Recruiter dashboard
- Candidate ranking system
- LLM-based feedback generation

---

## Conclusion

The AI-Powered Intelligent Hiring Tool demonstrates how NLP, Machine Learning, and Deep Learning can be used to transform traditional hiring processes.

By combining semantic resume matching, skill gap analysis, and conversational AI, this project provides a scalable and intelligent hiring solution that benefits both recruiters and candidates.

---

## Author

### Mayank Dhyani

Celebal Technologies Internship Project
