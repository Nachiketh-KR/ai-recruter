import sys
from pathlib import Path

# Ensure the project root is on sys.path so `from src...` imports work
# when running this file directly (e.g. `python src/features/feature_engineering.py`).
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

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


def main():
    candidates = load_candidates("/Users/nachikethkr/Desktop/ai-recruter/candidates.jsonl", limit=10)

    for candidate in candidates:
        feature = extract_features(candidate)

        print(
            experience_score(
                feature["years_experience"]
            )
        )


if __name__ == "__main__":
    main()