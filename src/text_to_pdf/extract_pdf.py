from fpdf import FPDF

from src.util import generate_path

pdf = FPDF()
pdf.add_page()
font_path = generate_path("/font/cmr10.ttf")
pdf.add_font("MS Gothic", "", font_path, uni=True)
pdf.set_font("MS Gothic", size=16)
text = "Hello, World! こんにちは、世界！"
pdf.cell(200, 10, txt=text, ln=True)
pdf.output(generate_path("/output/abc.pdf"))
