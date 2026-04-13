import base64
import requests
import json
from pathlib import Path
import time

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
RESULTS_DIR = BASE_DIR / "results" / "model_3_visionllm"

# URL di default delle API locali di Ollama
OLLAMA_URL = "http://localhost:11434/api/generate"
# Assicurati di aver fatto 'ollama pull llava' prima di lanciare lo script
MODEL_NAME = "llava" 

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def run():
    print(f"Avvio elaborazione con Vision LLM ({MODEL_NAME} via Ollama)...")
    
    for img_path in DATA_DIR.rglob("*"):
        if img_path.suffix.lower() in ['.png', '.jpg', '.jpeg']:
            print(f"Elaborazione: {img_path.name}")
            
            relative_path = img_path.relative_to(DATA_DIR)
            result_file_path = RESULTS_DIR / relative_path.with_suffix('.txt')
            result_file_path.parent.mkdir(parents=True, exist_ok=True)
            
            start_time = time.time()
            try:
                base64_image = encode_image_to_base64(img_path)
                
                # Prepariamo il payload per l'LLM
                payload = {
                    "model": MODEL_NAME,
                    "prompt": "Extract all the text from this image. Output ONLY the extracted text, without any introductory or conversational remarks. Keep the original formatting as much as possible.",
                    "images": [base64_image],
                    "stream": False
                }
                
                response = requests.post(OLLAMA_URL, json=payload)
                response.raise_for_status() # Verifica che la richiesta sia andata a buon fine
                
                result_json = response.json()
                extracted_text = result_json.get("response", "")
                
                # Salvataggio risultati
                with open(result_file_path, "w", encoding="utf-8") as f:
                    f.write(extracted_text.strip())
                    
                print(f"  -> Completato in {time.time() - start_time:.2f}s")
            except Exception as e:
                print(f"  -> Errore su {img_path.name}: {e}")

if __name__ == "__main__":
    run()