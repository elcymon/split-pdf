from PyPDF2 import PdfFileReader, PdfFileWriter

replacementPage = PdfFileReader('replacer.pdf', 'rb')
replacementPageNumber = 2
completeDocument = PdfFileReader('original.pdf', 'rb')

output = PdfFileWriter()

for i in range(completeDocument.getNumPages()):
    if i == replacementPageNumber:
        output.addPage(replacementPage.getPage(0))
    else:
        output.addPage(completeDocument.getPage(i))
with open('output-file.pdf', 'wb') as f:
    output.write(f)