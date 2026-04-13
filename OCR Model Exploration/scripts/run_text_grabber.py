import tkinter as tk
from PIL import ImageGrab
import pytesseract
import pyperclip
import keyboard
import sys

# ==============================================================================
# CONFIGURAZIONE TESSERACT
# Se sei su Windows, DEVI specificare il percorso dell'eseguibile di Tesseract.
# Rimuovi il commento dalla riga sottostante e verifica il percorso:
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\eliseo.gagliardi\AppData\Local\Programs\Tesseract-OCR'
# ==============================================================================

class TextGrabberApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw() # Nasconde la finestra principale (app in background)
        
        # Configura la scorciatoia globale (puoi personalizzarla)
        self.hotkey = 'ctrl+shift+e'
        try:
            keyboard.add_hotkey(self.hotkey, self.trigger_overlay)
            print("=====================================================")
            print(" Text Grabber avviato in background.")
            print(f" Premi {self.hotkey.upper()} per selezionare lo schermo.")
            print(" Tieni premuto 'ESC' durante la selezione per annullare.")
            print("=====================================================")
        except Exception as e:
            print(f"Errore nell'assegnazione dell'hotkey (esegui come amministratore su Linux/Mac): {e}")
            sys.exit(1)
        
        self.overlay = None

    def trigger_overlay(self):
        # Assicura che l'overlay venga creato nel thread principale della UI
        self.root.after(0, self.create_overlay)

    def create_overlay(self):
        # Evita di aprire overlay multipli se l'utente preme la combo più volte
        if self.overlay is not None and self.overlay.winfo_exists():
            return 

        self.overlay = tk.Toplevel(self.root)
        self.overlay.attributes('-alpha', 0.3)      # Trasparenza per scurire lo schermo
        self.overlay.attributes('-fullscreen', True)# Modalità a tutto schermo
        self.overlay.attributes('-topmost', True)   # Sempre in primo piano
        self.overlay.config(cursor="cross")

        self.canvas = tk.Canvas(self.overlay, cursor="cross", bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Binding degli eventi del mouse e della tastiera
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        self.overlay.bind("<Escape>", lambda e: self.overlay.destroy())

        self.start_x = None
        self.start_y = None
        self.rect = None

    def on_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        # Disegna un rettangolo tratteggiato
        self.rect = self.canvas.create_rectangle(
            self.start_x, self.start_y, 1, 1, 
            outline='white', width=2, fill='gray50', stipple='gray50'
        )

    def on_drag(self, event):
        self.canvas.coords(self.rect, self.start_x, self.start_y, event.x, event.y)

    def on_release(self, event):
        x1 = min(self.start_x, event.x)
        y1 = min(self.start_y, event.y)
        x2 = max(self.start_x, event.x)
        y2 = max(self.start_y, event.y)
        
        # Chiudi l'overlay immediatamente per non catturarlo nello screenshot
        self.overlay.destroy()
        
        # Procedi solo se è stata selezionata un'area valida (non un singolo click)
        if (x2 - x1 > 10) and (y2 - y1 > 10):
            # Ritarda la cattura di 100ms per permettere all'overlay di sparire completamente
            self.root.after(100, lambda: self.extract_text(x1, y1, x2, y2))

    def extract_text(self, x1, y1, x2, y2):
        print("\nCattura ed elaborazione OCR in corso...")
        try:
            # 1. Cattura Schermo
            img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
            
            # 2. Estrazione Testo (ita+eng per supporto multilingua standard)
            text = pytesseract.image_to_string(img, lang='ita+eng').strip()
            
            # 3. Copia negli appunti
            if text:
                pyperclip.copy(text)
                print("✅ Testo copiato con successo!")
                print("-" * 30)
                print(text)
                print("-" * 30)
            else:
                print("⚠️ Nessun testo rilevato in quest'area.")
                
        except pytesseract.TesseractNotFoundError:
            print("❌ ERRORE: Tesseract OCR non trovato. Verifica il percorso in pytesseract.tesseract_cmd.")
        except Exception as e:
            print(f"❌ Errore imprevisto durante l'OCR: {e}")

    def run(self):
        # Avvia il loop dell'interfaccia grafica
        self.root.mainloop()

if __name__ == '__main__':
    app = TextGrabberApp()
    app.run()
