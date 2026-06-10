def skill_match_score(
    candidate_skills,
    jd_skills
):

    candidate_set = {
        skill.lower()
        for skill in candidate_skills
    }

    jd_set = {
        skill.lower()
        for skill in jd_skills
    }

    matches = candidate_set.intersection(jd_set)

    score = (
        len(matches) /
        len(jd_set)
    ) * 100

    return {
        "score": round(score, 2),
        "matched_skills": list(matches)
    }

def experience_match_score(
    candidate_exp,
    required_exp
):

    if candidate_exp >= required_exp:
        return 100

    return round(
        (candidate_exp / required_exp) * 100,
        2
    )

