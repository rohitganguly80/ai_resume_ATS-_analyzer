from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_resume_pdf(content):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    for line in content.split("\n"):

        if line.strip():

            story.append(
                Paragraph(line, styles["BodyText"])
            )

            story.append(
                Spacer(1, 6)
            )

    doc.build(story)

    buffer.seek(0)

    return buffer