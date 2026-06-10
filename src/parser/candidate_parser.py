import json

# Use package-relative import when running as part of the `src` package,
# but allow a top-level import fallback when running the file directly.
try:
    from ..scoring.scoring_engine import (
        calculate_skill_score,
        experience_score,
        recruitability_score,
        activity_score,
        domain_score,
        final_score
    )
except Exception:
    from scoring.scoring_engine import (
        calculate_skill_score,
        experience_score,
        recruitability_score,
        activity_score,
        domain_score,
        final_score
    )

def load_candidates(file_path, limit=10):
    """
    Load first N candidates from JSONL file
    """

    candidates = []

    with open(file_path, "r", encoding="utf-8") as f:
        for _ in range(limit):
            try:
                candidates.append(json.loads(next(f)))
            except StopIteration:
                break

    return candidates


def summarize_candidate(candidate):
    """
    Basic summary
    """

    return {
        "id": candidate.get("candidate_id"),

        "experience":
            candidate.get("profile", {})
                     .get("years_of_experience"),

        "skills_count":
            len(candidate.get("skills", [])),

        "career_entries":
            len(candidate.get("career_history", []))
    }


def extract_features(candidate):
    """
    Extract important fields for ranking
    """

    profile = candidate.get("profile", {})
    signals = candidate.get("redrob_signals", {})

    skills = candidate.get("skills", [])

    return {

        "candidate_id":
            candidate.get("candidate_id"),

        "headline":
            profile.get("headline"),

        "summary":
            profile.get("summary"),

        "years_experience":
            profile.get("years_of_experience", 0),

        "current_title":
            profile.get("current_title"),

        "industry":
            profile.get("current_industry"),

        "skills":
            skills,

        "skill_count":
            len(skills),

        "open_to_work":
            signals.get("open_to_work_flag"),

        "github_score":
            signals.get("github_activity_score"),

        "response_rate":
            signals.get("recruiter_response_rate"),

        "offer_acceptance":
            signals.get("offer_acceptance_rate"),

        "notice_period":
            signals.get("notice_period_days"),
        "career_descriptions": [
            job.get("description", "")
            for job in candidate.get("career_history", [])
        ],

        "career_titles": [
            job.get("title", "")
            for job in candidate.get("career_history", [])
        ],

        "skill_names": [
            skill.get("name", "")
            for skill in candidate.get("skills", [])
        ]

    }


if __name__ == "__main__":

    FILE_PATH = "/Users/nachikethkr/Desktop/ai-recruter/candidates.jsonl"

    candidates = load_candidates(FILE_PATH, limit=1)

    print(f"\nLoaded {len(candidates)} candidates\n")

    print("=" * 80)
    print("CANDIDATE OVERVIEW")
    print("=" * 80)

    for candidate in candidates:

        profile = candidate.get("profile", {})

        print(
            f"{candidate.get('candidate_id')} | "
            f"{profile.get('current_title')} | "
            f"{profile.get('years_of_experience')} years"
        )

    print("\n")
    print("=" * 80)
    print("EXTRACTED FEATURES")
    print("=" * 80)

    for candidate in candidates:

        feature = extract_features(candidate)

        print("\n")
        print(json.dumps(feature, indent=2))
        print(candidate["career_history"])
        print({
            "experience": experience_score(feature["years_experience"]),
            "skills": calculate_skill_score(feature["skills"]),
            "recruitability": recruitability_score(feature),
            "activity": activity_score(feature),
            "domain": domain_score(feature)
        })