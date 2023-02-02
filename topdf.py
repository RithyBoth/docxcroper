from docx2pdf import convert
from pdf2image import convert_from_path
import sys
import os


input= sys.argv[1]
outputdir= sys.argv[2]
print(input)
# Store Pdf with convert_from_path function
convert(input, "temp.pdf")
images = convert_from_path('temp.pdf')
 
for i in range(len(images)):
   
      # Save pages as images in the pdf
    images[i].save(f'Output/{outputdir}-temp/page'+ str(i) +'.png', 'PNG')

os.remove("temp.pdf")

os.system(f"python crop2.py {outputdir}")

