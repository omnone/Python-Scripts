import PyPDF2, os

pdf_files = []

#get all pdf files from directory
pdf_files=[filename for filename in os.listdir('.') if filename.endswith('.pdf')]

#sort filenames 
pdf_files.sort()

pdfWriter = PyPDF2.PdfFileWriter()

#copy each pdf file to the final output file
for filename in pdf_files:
	print(f'Merging {filename} to main pdf file')
	pdfFileObj = open(filename,'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj,strict=False)

        #if you want to skip first page change the range below from 0 to 1
	for page_num in range(0,pdfReader.numPages):
		pageObj = pdfReader.getPage(page_num)
		pdfWriter.addPage(pageObj)

#save output file
pdfOutput = open('combined.pdf','wb')
pdfWriter.write(pdfOutput)

pdfOutput.close()
