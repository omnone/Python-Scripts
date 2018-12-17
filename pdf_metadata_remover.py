#!/usr/bin/python3
import PyPDF2, os

#get all pdf files from directory
pdf_files=[filename for filename in os.listdir('.') if filename.endswith('.pdf')]


for filename in pdf_files:
        pdfWriter = PyPDF2.PdfFileWriter()
        print(f'Removing metadata from {filename}')
        
        pdfFileObj = open(filename,'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj,strict=False)

        #if you want to skip first page change the range below from 0 to 1
        for page_num in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(page_num)
                pdfWriter.addPage(pageObj)

        #save output file
        pdfOutput = open(f'sanitized_{filename}','wb')
        pdfWriter.write(pdfOutput)
        pdfOutput.close()
