import pytesseract
from PIL import Image
from pathlib import Path
import time

# Configurazione percorsi
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
RESULTS_DIR = BASE_DIR / "results" / "model_1_tesseract"

def run():
    print("Avvio elaborazione con Tesseract OCR...")
    # Cerca tutte le immagini nelle sottocartelle
    for img_path in DATA_DIR.rglob("*"):
        if img_path.suffix.lower() in ['.png', '.jpg', '.jpeg']:
            print(f"Elaborazione: {img_path.name}")
            
            # Ricrea la struttura delle cartelle in results
            relative_path = img_path.relative_to(DATA_DIR)
            result_file_path = RESULTS_DIR / relative_path.with_suffix('.txt')
            result_file_path.parent.mkdir(parents=True, exist_ok=True)
            
            start_time = time.time()
            try:
                # Esecuzione OCR
                img = Image.open(img_path)
                text = pytesseract.image_to_string(img)
                
                # Salvataggio risultati
                with open(result_file_path, "w", encoding="utf-8") as f:
                    f.write(text.strip())
                    
                print(f"  -> Completato in {time.time() - start_time:.2f}s")
            except Exception as e:
                print(f"  -> Errore su {img_path.name}: {e}")

if __name__ == "__main__":
    run()