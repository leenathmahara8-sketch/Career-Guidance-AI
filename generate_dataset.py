"""
generate_dataset.py — Generates synthetic student career dataset and writes to data/student_career_data.csv
Run once: python generate_dataset.py
"""

import os
import numpy as np
import pandas as pd

np.random.seed(42)

CAREERS = [
    "Software Engineer",
    "Data Scientist",
    "Doctor",
    "Lawyer",
    "Teacher",
    "Business Analyst",
    "Graphic Designer",
    "Nurse",
    "Accountant",
    "Mechanical Engineer",
]

# (math_mean, math_std, science_mean, science_std, english_mean, english_std, cs_mean, cs_std)
SCORE_PROFILES = {
    "Software Engineer":   (80, 8,  70, 10, 60, 10, 88, 7),
    "Data Scientist":      (85, 7,  78, 8,  62, 10, 85, 8),
    "Doctor":              (82, 8,  92, 5,  65, 10, 55, 12),
    "Lawyer":              (65, 10, 60, 10, 92, 5,  55, 12),
    "Teacher":             (68, 10, 65, 10, 82, 7,  58, 12),
    "Business Analyst":    (72, 9,  65, 10, 78, 8,  70, 10),
    "Graphic Designer":    (55, 12, 52, 12, 70, 10, 65, 12),
    "Nurse":               (65, 10, 82, 8,  72, 9,  50, 12),
    "Accountant":          (82, 7,  65, 10, 68, 10, 62, 12),
    "Mechanical Engineer": (85, 7,  82, 7,  60, 10, 65, 12),
}

SKILLS_POOL = {
    "Software Engineer":   ["python", "java", "problem_solving", "teamwork", "analysis"],
    "Data Scientist":      ["python", "analysis", "math", "research", "problem_solving"],
    "Doctor":              ["research", "analysis", "leadership", "teamwork", "problem_solving"],
    "Lawyer":              ["writing", "communication", "research", "analysis", "leadership"],
    "Teacher":             ["communication", "leadership", "writing", "teamwork", "creativity"],
    "Business Analyst":    ["analysis", "communication", "leadership", "problem_solving", "math"],
    "Graphic Designer":    ["design", "creativity", "communication", "problem_solving", "writing"],
    "Nurse":               ["teamwork", "communication", "research", "problem_solving", "leadership"],
    "Accountant":          ["math", "analysis", "problem_solving", "research", "teamwork"],
    "Mechanical Engineer": ["math", "problem_solving", "analysis", "research", "teamwork"],
}

INTERESTS_POOL = {
    "Software Engineer":   ["technology", "engineering", "science"],
    "Data Scientist":      ["technology", "science", "research"],
    "Doctor":              ["healthcare", "science", "social_work"],
    "Lawyer":              ["law", "social_work", "education"],
    "Teacher":             ["education", "social_work", "arts"],
    "Business Analyst":    ["business", "finance", "technology"],
    "Graphic Designer":    ["arts", "technology", "creativity"],
    "Nurse":               ["healthcare", "social_work", "science"],
    "Accountant":          ["finance", "business", "math"],
    "Mechanical Engineer": ["engineering", "science", "technology"],
}

ALL_SKILLS = ["python", "java", "communication", "analysis", "design", "writing",
              "math", "research", "leadership", "creativity", "problem_solving", "teamwork"]
ALL_INTERESTS = ["technology", "healthcare", "business", "law", "education",
                 "arts", "science", "finance", "engineering", "social_work"]

rows = []
samples_per_career = 55  # 55 * 10 = 550 rows

for career in CAREERS:
    mm, ms, sm, ss, em, es, cm, cs_s = SCORE_PROFILES[career]
    primary_skills = SKILLS_POOL[career]
    primary_interests = INTERESTS_POOL[career]

    for _ in range(samples_per_career):
        math = int(np.clip(np.random.normal(mm, ms), 20, 100))
        science = int(np.clip(np.random.normal(sm, ss), 20, 100))
        english = int(np.clip(np.random.normal(em, es), 20, 100))
        cs = int(np.clip(np.random.normal(cm, cs_s), 20, 100))

        # Pick 3-5 skills: mostly from primary, occasionally random
        n_skills = np.random.randint(3, 6)
        skills = list(np.random.choice(primary_skills, size=min(n_skills, len(primary_skills)), replace=False))
        if len(skills) < n_skills:
            extras = [s for s in ALL_SKILLS if s not in skills]
            skills += list(np.random.choice(extras, size=n_skills - len(skills), replace=False))

        # Pick 2-3 interests: mostly from primary
        n_interests = np.random.randint(2, 4)
        interests = list(np.random.choice(primary_interests, size=min(n_interests, len(primary_interests)), replace=False))
        if len(interests) < n_interests:
            extras = [i for i in ALL_INTERESTS if i not in interests]
            interests += list(np.random.choice(extras, size=n_interests - len(interests), replace=False))

        rows.append({
            "math_score": math,
            "science_score": science,
            "english_score": english,
            "cs_score": cs,
            "skills": ",".join(skills),
            "interests": ",".join(interests),
            "career_label": career,
        })

df = pd.DataFrame(rows)
os.makedirs("data", exist_ok=True)
df.to_csv("data/student_career_data.csv", index=False)
print(f"Generated {len(df)} rows -> data/student_career_data.csv")
