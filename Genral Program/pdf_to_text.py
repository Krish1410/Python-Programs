# # import pypdf2
# import PyPDF2

# PdfPath=input("Enter your pdf locashion: ")
# obj=PyPDF2.PdfFileReader(PdfPath)

# text=""

# # pages=obj.numPages
# # print(pages)
# for i in range(0,5):
#     text+=obj.getPage(i).extractText()
#     print(text)

# print(text)
# filename=input("Enter file name for save the pdf text:")
# with open (filename,"w") as f:
#     f.write(text)


import os
import subprocess

for top, dirs, files in os.walk('K:\My Pdf\Ecco.pdf'):
    for filename in files:
        if filename.endswith('.pdf'):
            abspath = os.path.join(top, filename)
            subprocess.call('lowriter --invisible --convert-to doc "{}"'
                            .format(abspath), shell=True)