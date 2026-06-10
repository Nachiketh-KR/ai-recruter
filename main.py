# main.py

from src.parser.candidate_parser import (
    load_candidates,
    extract_features
)

from src.scoring.scoring_engine import (
    calculate_skill_score,
    experience_score,
    recruitability_score,
    activity_score,
    domain_score
)

FILE_PATH = "/Users/nachikethkr/Desktop/ai-recruter/candidates.jsonl"

candidates = load_candidates(FILE_PATH, limit=10)

for candidate in candidates:

    feature = extract_features(candidate)

    print({
        "experience": experience_score(feature["years_experience"]),
        "skills": calculate_skill_score(feature["skills"]),
        "recruitability": recruitability_score(feature),
        "activity": activity_score(feature),
        "domain": domain_score(feature)
    })