from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 50)
        self.cell(0, 50, "CS50 Shirtificate", align="C")
        self.ln(20)

    def add_shirt_image(self, name):
        self.image("shirtificate.png", x=10, y=70, w=190)

        self.set_font("helvetica", "B", 25)
        self.set_text_color(255, 255, 255)
        self.text(x=50, y=140, txt=f"{name} took CS50")


def main():
    name = input("Name: ")

    pdf = PDF()
    pdf.add_page()
    pdf.add_shirt_image(name)

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
