# main.py

from src.parser.candidate_parser import (
    load_candidates,
    extract_features
)

from src.scoring.scoring_engine import (
    calculate_skill_score,
    experience_score,
    final_score,
    recruitability_score,
    activity_score,
    domain_score
)

from src.matching.matcher import experience_match_score
from src.ranking.ranking_engine import recruiter_score


FILE_PATH = "/Users/nachikethkr/Desktop/ai-recruter/candidates.jsonl"

candidates = load_candidates(FILE_PATH, limit=50)

results = []

for candidate in candidates:
    feature = extract_features(candidate)

    jd_score = experience_match_score(
        feature["years_experience"],
        5
    )

    score = recruiter_score(
        jd_score,
        feature
    )

    results.append({
        "candidate_id": feature["candidate_id"],
        "score": score
    })

    print({
        "experience": experience_score(feature["years_experience"]),
        "skills": calculate_skill_score(feature["skills"]),
        "recruitability": recruitability_score(feature),
        "activity": activity_score(feature),
        "domain": domain_score(feature),
        "finalscore": final_score(feature)
    })

    print("\n")
    print("match score vs JD:")
    print(
        feature["candidate_id"],
        "matching score:",
        experience_match_score(feature["years_experience"], 9),
    )


results.sort(
    key=lambda x: x["score"],
    reverse=True
)

for rank, candidate in enumerate(results[:50], 1):
    print(rank, candidate["candidate_id"], candidate["score"])

