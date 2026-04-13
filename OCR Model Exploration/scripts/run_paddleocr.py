from paddleocr import PaddleOCR
from pathlib import Path
import time

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
RESULTS_DIR = BASE_DIR / "results" / "model_2_paddleocr"

def run():
    print("Avvio elaborazione con PaddleOCR...")
    # Inizializza il modello (usa l'inglese di default, puoi cambiare in 'it' o 'multilingual')
    ocr = PaddleOCR(use_angle_cls=True, lang='en', show_log=False)
    
    for img_path in DATA_DIR.rglob("*"):
        if img_path.suffix.lower() in ['.png', '.jpg', '.jpeg']:
            print(f"Elaborazione: {img_path.name}")
            
            relative_path = img_path.relative_to(DATA_DIR)
            result_file_path = RESULTS_DIR / relative_path.with_suffix('.txt')
            result_file_path.parent.mkdir(parents=True, exist_ok=True)
            
            start_time = time.time()
            try:
                # Esecuzione OCR
                result = ocr.ocr(str(img_path), cls=True)
                
                # PaddleOCR restituisce una lista complessa con coordinate e confidenza
                # Estraiamo solo il testo
                extracted_text = []
                if result and result[0]:
                    for line in result[0]:
                        text = line[1][0]
                        extracted_text.append(text)
                
                # Salvataggio risultati
                with open(result_file_path, "w", encoding="utf-8") as f:
                    f.write("\n".join(extracted_text))
                    
                print(f"  -> Completato in {time.time() - start_time:.2f}s")
            except Exception as e:
                print(f"  -> Errore su {img_path.name}: {e}")

if __name__ == "__main__":
    run()