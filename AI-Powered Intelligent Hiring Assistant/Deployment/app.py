import gradio as gr
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# ==========================
# LOAD MODEL
# ==========================
model = SentenceTransformer('all-MiniLM-L6-v2')

# ==========================
# JOB DESCRIPTION
# ==========================
job_description = """
We are hiring a Data Scientist with strong expertise in Python, SQL, Machine Learning, Deep Learning, TensorFlow, Pandas, and Statistics.
The ideal candidate should have experience in data preprocessing, predictive modeling, feature engineering, model evaluation, and deploying machine learning solutions.
Experience with analytics, visualization, and business problem-solving is preferred.
"""

jd_embedding = model.encode([job_description])

skills_required = [
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "pandas"
]

# ==========================
# HELPER FUNCTIONS
# ==========================
def check_skill(text, skill):
    return skill.lower() in text.lower()


def user_chatbot(query, candidate_profile, missing_skills):
    query = query.lower()

    score = candidate_profile['match_score']

    if score >= 80:
        verdict = "Strong Match"
    elif score >= 65:
        verdict = "Moderate Match"
    else:
        verdict = "Weak Match"

    if "score" in query:
        return f"""
Your match score is {score:.2f}%.
Verdict: {verdict}
"""

    elif "missing" in query or "skills" in query:
        if len(missing_skills) == 0:
            return "Excellent! You currently have all required core skills."
        else:
            return f"Missing Skills: {', '.join(missing_skills)}"

    elif "improve" in query:
        if len(missing_skills) == 0:
            return """
Your profile is already strong.

To improve further:
1. Build advanced projects
2. Add certifications
3. Gain real-world experience
"""
        else:
            return f"""
To improve your profile:
1. Learn {', '.join(missing_skills)}
2. Build practical projects
3. Add certifications
"""

    elif "why" in query:
        if len(missing_skills) == 0:
            return "Your score is already strong due to excellent skill alignment."
        else:
            return f"Your score is affected by missing skills: {', '.join(missing_skills)}"

    else:
        return """
You can ask:
- What is my score?
- What skills are missing?
- How can I improve?
- Why is my score low?
"""


# ==========================
# MAIN EVALUATION FUNCTION
# ==========================
def evaluate_candidate(name, resume_text, query):
    
    resume_embedding = model.encode([resume_text])

    score = cosine_similarity(jd_embedding, resume_embedding)[0][0]
    match_score = ((score + 1) / 2) * 100

    matched_skills = []

    for skill in skills_required:
        if check_skill(resume_text, skill):
            matched_skills.append(skill)

    missing_skills = [
        skill for skill in skills_required
        if skill not in matched_skills
    ]

    candidate_profile = {
        "match_score": match_score,
        "skills": matched_skills
    }

    if match_score >= 80:
        verdict = "Strong Match"
    elif match_score >= 65:
        verdict = "Moderate Match"
    else:
        verdict = "Weak Match"

    bot_response = user_chatbot(query, candidate_profile, missing_skills)

    result = f"""
Candidate Name: {name}
Role: Data Scientist

Match Score: {match_score:.2f}%
Verdict: {verdict}

Matched Skills: {', '.join(matched_skills) if matched_skills else 'None'}
Missing Skills: {', '.join(missing_skills) if missing_skills else 'None'}
"""

    return result, bot_response


# ==========================
# GRADIO UI
# ==========================
demo = gr.Interface(
    fn=evaluate_candidate,
    inputs=[
        gr.Textbox(label="Candidate Name"),
        gr.Textbox(lines=15, label="Paste Resume Text"),
        gr.Textbox(label="Ask AI Assistant")
    ],
    outputs=[
        gr.Textbox(label="Candidate Evaluation"),
        gr.Textbox(label="AI Assistant Response")
    ],
    title="AI-Powered Intelligent Hiring Tool",
    description="""
Data Scientist Role Evaluation

Job Description:
We are hiring a Data Scientist with strong expertise in Python, SQL, Machine Learning, Deep Learning, TensorFlow, Pandas, and Statistics.

The ideal candidate should have experience in:
• Data preprocessing
• Predictive modeling
• Feature engineering
• Model evaluation
• Deploying machine learning solutions

Preferred:
• Analytics
• Visualization
• Business problem-solving
"""
)

demo.launch()