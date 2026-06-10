import sys
from pathlib import Path

# Ensure project root is available when running modules directly
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.scoring.scoring_engine import (
    activity_score,
    recruitability_score,
    experience_score
)


def recruiter_score(
    jd_match,
    feature
):

    return (
        jd_match * 0.60
        +
        recruitability_score(feature) * 0.10
        +
        activity_score(feature) * 0.10
        +
        experience_score(
            feature["years_experience"]
        ) * 0.20
    )


if __name__ == "__main__":
    print("ranking_engine module loaded directly — use recruiter_score(jd_match, feature)")