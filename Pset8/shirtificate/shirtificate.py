from fpdf import FPDF
from PIL import Image

class PDF():
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", "B", 48)
        self._pdf.set_auto_page_break
        self._pdf.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
        self._pdf.image("shirtificate.png", w=self._pdf.epw)
        self._pdf.set_font_size(24)
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.text(x=50, y=140, txt=f"{name} took CS50")

    def output(self, name):
        self._pdf.output(name)


name = input("Name: ")
# Instantiation of inherited class
pdf = PDF(name)
pdf.output("shirtificate.pdf")