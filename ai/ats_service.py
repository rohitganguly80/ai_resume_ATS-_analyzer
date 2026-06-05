from ai.llm_client import ask_llm
from ai.prompt_templates import ATS_PROMPT


def generate_ats_report(
    resume_text,
    jd_text
):

    prompt = ATS_PROMPT.format(
        resume=resume_text,
        jd=jd_text
    )

    return ask_llm(prompt)