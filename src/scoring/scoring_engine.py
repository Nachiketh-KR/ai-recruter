AI_TITLES = [
    "ML Engineer",
    "AI Engineer",
    "Data Scientist",
    "Data Engineer",
    "Machine Learning Engineer",
    "Research Engineer",
    "Applied Scientist"
]

AI_KEYWORDS = [
    "llm",
    "nlp",
    "machine learning",
    "deep learning",
    "speech recognition",
    "fine-tuning",
    "lora",
    "milvus",
    "vector",
    "embedding"
]

def experience_score(years):
    return min(years * 10, 100)

def calculate_skill_score(skills):

    score = 0

    proficiency_map = {
        "beginner": 1,
        "intermediate": 2,
        "advanced": 3,
        "expert": 4
    }

    for skill in skills:

        score += proficiency_map.get(
            skill.get("proficiency", "").lower(),
            0
        )

    return score

def recruitability_score(feature):

    score = 0

    if feature["open_to_work"]:
        score += 30

    response_rate = feature["response_rate"]
    if response_rate != -1:
        score += response_rate * 30

    offer_acceptance = feature["offer_acceptance"]
    if offer_acceptance != -1:
        score += offer_acceptance * 20

    notice_period = feature["notice_period"] or 90

    score += max(
        0,
        20 - (notice_period / 10)
    )

    return score

def activity_score(feature):

    github = feature["github_score"]

    if github == -1:
        return 0

    return github

def domain_score(feature):

    text = " ".join([
        feature.get("headline", ""),
        feature.get("summary", ""),
        " ".join(feature.get("career_titles", [])),
        " ".join(feature.get("career_descriptions", [])),
        " ".join(feature.get("skill_names", []))
    ]).lower()

    score = 0

    for keyword in AI_KEYWORDS:
        if keyword in text:
            score += 10

    return min(score, 100)

def final_score(feature):

    return (
        experience_score(
            feature["years_experience"]
        ) * 0.25

        +

        recruitability_score(
            feature
        ) * 0.20

        +

        domain_score(
            feature
        ) * 0.25

        +

        activity_score(
            feature
        ) * 0.10

        +
        calculate_skill_score(feature["skills"])
    )