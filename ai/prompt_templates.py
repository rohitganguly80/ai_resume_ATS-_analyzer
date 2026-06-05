ATS_PROMPT = """
You are an ATS Expert.

Analyze the Resume and Job Description.

Return:

1. ATS Score (/100)
2. Match Percentage
3. Resume Summary
4. Skills Found
5. Missing Skills
6. Strengths
7. Weaknesses
8. Improvement Suggestions
9. Final Recommendation

Resume:
{resume}

Job Description:
{jd}
"""


SKILL_GAP_PROMPT = """
Compare Resume and JD.

Return:

1. Existing Skills
2. Matching Skills
3. Missing Skills
4. Skill Gap Percentage

Resume:
{resume}

JD:
{jd}
"""


INTERVIEW_PROMPT = """
Generate interview questions based on:

Resume:
{resume}

JD:
{jd}

Generate:

1. Technical Questions
2. Project Questions
3. HR Questions
4. Behavioral Questions
"""


ROADMAP_PROMPT = """
Based on Resume and JD:

Generate:

1. Missing Skills
2. Certifications
3. Courses
4. Projects
5. 30-60-90 Day Roadmap

Resume:
{resume}

JD:
{jd}
"""


COVER_LETTER_PROMPT = """
Generate a professional cover letter.

Resume:
{resume}

Job Description:
{jd}
"""
RESUME_REWRITE_PROMPT = """
Rewrite and improve the resume.

Improve:

1. Professional Summary
2. Project Descriptions
3. Experience Points
4. ATS Keywords

Resume:

{resume}
"""