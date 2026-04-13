# Python Text Grabber

Un'utility leggera e veloce, scritta in Python, per catturare istantaneamente il testo visibile sullo schermo tramite OCR e copiarlo direttamente negli appunti. Ispirato a PowerToys Text Extractor e Text-Grab.

## Prerequisiti

Essendo basato su Python, il progetto richiede l'installazione di **Tesseract OCR** nel sistema operativo, poiché le librerie Python si appoggiano al suo motore per il riconoscimento dei caratteri.

### Installare Tesseract OCR
* **Windows**: Scarica l'installer da [UB-Mannheim Tesseract Wiki](https://github.com/UB-Mannheim/tesseract/wiki). 
* **macOS**: Esegui `brew install tesseract tesseract-lang` (se usi Homebrew).
* **Linux**: Esegui `sudo apt install tesseract-ocr tesseract-ocr-ita tesseract-ocr-eng`.
