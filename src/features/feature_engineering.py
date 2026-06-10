from src.parser.candidate_parser import (
    load_candidates,
    extract_features
)
from src.scoring.scoring_engine import (
    experience_score,
    recruitability_score,
    activity_score,
    domain_score,
    final_score
)

candidates = load_candidates("/Users/nachikethkr/Desktop/ai-recruter/candidates.jsonl", limit=10)

for candidate in candidates:

    feature = extract_features(candidate)

    print(
        experience_score(
            feature["years_experience"]
        )
    )