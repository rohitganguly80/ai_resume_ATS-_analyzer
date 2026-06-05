from ai.llm_client import ask_llm
from ai.prompt_templates import INTERVIEW_PROMPT


def generate_interview_questions(
    resume_text,
    jd_text
):

    prompt = INTERVIEW_PROMPT.format(
        resume=resume_text,
        jd=jd_text
    )

    return ask_llm(prompt)