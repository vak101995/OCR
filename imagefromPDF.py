msg ="Roll a dice!"
print(msg)
from pdf2image import convert_from_path

images = convert_from_path('invoice.pdf',500,poppler_path= r'C:\Program Files\poppler-24.02.0\Library\bin')

for i in range(len(images)):

    images[i].save('data/page'+str(i)+'.jpg', 'JPEG')