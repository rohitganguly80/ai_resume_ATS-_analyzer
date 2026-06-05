from ai.llm_client import ask_llm
from ai.prompt_templates import RESUME_REWRITE_PROMPT


def rewrite_resume(
    resume_text
):

    prompt = RESUME_REWRITE_PROMPT.format(
        resume=resume_text
    )

    return ask_llm(prompt)