from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Output file
output_file = "sample_legal_document.pdf"

# Create PDF
doc = SimpleDocTemplate(output_file, pagesize=LETTER)
styles = getSampleStyleSheet()
story = []

# Title
title = Paragraph("<b>Sample Legal Document</b>", styles['Title'])
story.append(title)
story.append(Spacer(1, 20))

# Sample legal text
text = """
This Non-Disclosure Agreement (NDA) is entered into between Party A and Party B. 
The purpose of this Agreement is to protect confidential information that may be disclosed between the parties. 
Confidential information includes but is not limited to trade secrets, financial data, and technical processes.

The receiving party agrees not to disclose any confidential information to third parties without prior written consent. 
The obligations of confidentiality shall remain in effect for a period of three (3) years from the date of disclosure.

In the event of a breach of this Agreement, the disclosing party shall be entitled to seek legal remedies, 
including but not limited to injunctive relief and damages. This Agreement shall be governed by the laws of the State of California.
"""

# Add paragraphs
for para in text.strip().split("\n\n"):
    story.append(Paragraph(para, styles['Normal']))
    story.append(Spacer(1, 12))

# Build PDF
doc.build(story)

print(f"PDF created: {output_file}")
