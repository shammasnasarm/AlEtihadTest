import os
import json
import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import pagesizes
from reportlab.lib.units import inch

from constants import OUTPUT_FOLDER


def load_data(file_path):
    if file_path.endswith(".json"):
        with open(file_path, "r") as f:
            return json.load(f)

    elif file_path.endswith(".csv"):
        df = pd.read_csv(file_path)
        return df.to_dict(orient="records")

    else:
        raise ValueError("Unsupported file format. Use JSON or CSV.")


def create_pdf(user_data):
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    filename = os.path.join(OUTPUT_FOLDER, f"{user_data['name'].replace(' ', '_')}_report.pdf")

    doc = SimpleDocTemplate(
        filename,
        pagesize=pagesizes.A4
    )

    elements = []
    styles = getSampleStyleSheet()

    # Title
    title_style = styles["Heading1"]
    title_style.alignment = 1
    elements.append(Paragraph("Personalized Performance Report", title_style))
    elements.append(Spacer(1, 0.3 * inch))

    body_style = styles["Normal"]
    elements.append(Paragraph(f"<b>Name:</b> {user_data.get('name', '-')}", body_style))
    elements.append(Paragraph(f"<b>Email:</b> {user_data.get('email', '-')}", body_style))
    elements.append(Paragraph(f"<b>Department:</b> {user_data.get('department', '-')}", body_style))
    elements.append(Paragraph(f"<b>Score:</b> {user_data.get('score', '-')}", body_style))
    elements.append(Spacer(1, 0.5 * inch))

    # Table Section
    table_data = [
        ["Field", "Value"],
    ]

    for key, value in user_data.items():
        table_data.append([key.capitalize(), str(value)])

    table = Table(table_data, hAlign='LEFT')

    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("PADDING", (0, 0), (-1, -1), 6),
    ]))

    elements.append(table)

    doc.build(elements)

    print(f"Generated: {filename}")