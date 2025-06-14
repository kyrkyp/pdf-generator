from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=15)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font("arial", size=24, style='B')
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 12, txt=row['Topic'], ln=1, align='C')
    pdf.line(10, 21, 200, 21)

    # Add a footer with the main page
    pdf.ln(265)
    pdf.set_font("arial", size=8, style='I')
    pdf.set_text_color(180, 180, 180)
    pdf.cell(0, 10, txt=row['Topic'], ln=1, align='R')

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Add the footer with the other pages
        pdf.ln(277)
        pdf.set_font("arial", size=8, style='I')
        pdf.set_text_color(180, 180, 180)
        pdf.cell(0, 10, txt=row['Topic'], ln=1, align='R')

pdf.output("demo.pdf")