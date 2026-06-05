from ai.llm_client import ask_llm
from ai.prompt_templates import ROADMAP_PROMPT


def generate_roadmap(
    resume_text,
    jd_text
):

    prompt = ROADMAP_PROMPT.format(
        resume=resume_text,
        jd=jd_text
    )

    return ask_llm(prompt)