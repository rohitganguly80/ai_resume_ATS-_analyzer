from ai.llm_client import ask_llm
from ai.prompt_templates import COVER_LETTER_PROMPT


def generate_cover_letter(
    resume_text,
    jd_text
):

    prompt = COVER_LETTER_PROMPT.format(
        resume=resume_text,
        jd=jd_text
    )

    return ask_llm(prompt)