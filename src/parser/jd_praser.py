from docx import Document

SKILLS_DB = [
    "Python",
    "Java",
    "AWS",
    "GCP",
    "Azure",
    "Spark",
    "Kafka",
    "SQL",
    "Machine Learning",
    "Deep Learning",
    "NLP",
    "LLM",
    "RAG",
    "Vector Database",
    "LangChain",
    "PyTorch",
    "TensorFlow",
    "LangChain",
    "FAISS",
    "Pinecone"
]

def load_jd(docx_path):

    doc = Document(docx_path)
    text = []

    for para in doc.paragraphs:
        text.append(para.text)

    return "\n".join(text)

jd_text = load_jd("/Users/nachikethkr/Desktop/ai-recruter/job_description.docx")

#print(jd_text)



def extract_jd_features(jd_text):

    found_skills = set()

    text = jd_text.lower()

    for skill in SKILLS_DB:

        if skill.lower() in text:
            found_skills.add(skill)

    return {
        "required_skills": found_skills
    }

features = extract_jd_features(jd_text)

print(features)

jd_features = {
    "required_skills": [...],
    "min_experience": 3
}


# def extract_jd_features(jd):
#     pass

# # print(job_description)

# def skill_match_score(
#     candidate_skills,
#     jd_skills
# ):
#     pass

# def experience_match_score(
#     candidate_exp,
#     required_exp
# ):
#     pass