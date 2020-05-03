import PyPDF2
import sys


template = PyPDF2.PdfFileReader(open('./pdf_playground/mega.pdf', 'rb'))
watermark= PyPDF2.PdfFileReader(open('./pdf_playground/wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('./pdf_playground/wtr_output.pdf', 'wb') as file:
        output.write(file)
