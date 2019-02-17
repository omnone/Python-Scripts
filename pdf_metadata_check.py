#!/usr/bin/python3
import PyPDF2
import os
import csv

# get all pdf files from directory
pdf_files = [filename for filename in os.listdir(
    '.') if filename.endswith('.pdf')]


with open('metadata_check.csv', mode='w', newline='') as check_file:

    csv_writer = csv.writer(check_file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['File:', 'Has_Meta:', 'Metadata:'])

    results = []

    for filename in pdf_files:
        pdfWriter = PyPDF2.PdfFileWriter()
        pdfFileObj = open(filename, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)

        metadata = pdfReader.getDocumentInfo()
        # print(metadata)
        meta_found = [key.strip('/').lower()+': '+value for key, value in metadata.items()
                      if value and key != '/Producer' and key != '/CreationDate'
                      and key != '/ModDate']

        if meta_found:
            #print(f'[-]:{filename} has metadata:')
            # for item in meta_found:
              # print(item)
            # print('--------------------------')
            results.append([filename, 'True', meta_found])
        else:
            results.append([filename, 'False', '-'])

    csv_writer.writerows(sorted(results, key=lambda x: x[1], reverse=True))
