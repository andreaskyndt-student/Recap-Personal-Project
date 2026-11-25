from io import BytesIO
from xml.sax.saxutils import escape
from docx import Document
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

def create_word_document(transcription, summary):
    doc = Document()
    doc.add_heading("Recap - Notes", 0)
    doc.add_heading("Transcription", level=1)
    doc.add_paragraph(transcription)
    doc.add_heading("Summary", level=1)
    doc.add_paragraph(summary)

    buffer = BytesIO()
    doc.save(buffer)

    return buffer.getvalue()

def create_pdf_document(transcription, summary):
    buffer = BytesIO()

    document = SimpleDocTemplate(
        buffer,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm
    )

    styles = getSampleStyleSheet()
    content = []

    title_style = ParagraphStyle(
        "Recap",
        parent=styles["Title"],
        alignment=TA_CENTER,
        textColor=colors.HexColor("#c7f9cc"),
    )

    content.append(
        Paragraph("Recap - Notes", title_style)
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph("Transcription", styles["Heading1"])
    )

    content.append(Spacer(1,8))

    transcription_text = "<br/>".join(
        escape(line) for line in transcription.splitlines()
    )

    content.append(
        Paragraph(transcription_text, styles["BodyText"])
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph("Summary", styles["Heading1"])
    )

    content.append(Spacer(1, 8))

    summary_text = "<br/>".join(
        escape(line) for line in summary.splitlines()
    )

    content.append(
        Paragraph(summary_text, styles["BodyText"])
    )

    document.build(content)

    return buffer.getvalue()