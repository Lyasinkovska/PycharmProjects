from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter
from pathlib import Path

pdf_path = (Path.home() / 'PycharmProjects' / 'Beetroot/PDF_project' / '2020_BA_diplom_Python.pdf')
pdf_reader = PdfFileReader(str(pdf_path), strict=False)
pdf_writer = PdfFileWriter()

pdf_writer.addBlankPage(width=72, height=72)

with Path("blank.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)

# output_file_path = (Path.home() / 'PycharmProjects' / 'Beetroot/PDF_project' / '2020_BA_diplom_Python.txt')
# with output_file_path.open(mode="w") as output_file:
#     title = pdf_reader.documentInfo.title
#     num_pages = pdf_reader.getNumPages()
#     output_file.write(f"{title}\nNumber of pages: {num_pages}\n\n")
#
#     for page in pdf_reader.pages:
#         text = page.extractText()
#         output_file.write(text)
