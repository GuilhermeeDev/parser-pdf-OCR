import matplotlib.pyplot as plt

from doctr.io import DocumentFile
from doctr.models import ocr_predictor

doc = DocumentFile.from_pdf("input/teste.pdf")
print(f"Number of pages: {len(doc)}")

# predictor = ocr_predictor(pretrained=True)

# resul = predictor(doc)

# resul.show()