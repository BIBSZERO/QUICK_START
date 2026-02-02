import json
import os

DB_FILE = "properties.json" # Verinin fiziksel dosya adı

def load_from_db():
    """Disk üzerindeki JSON dosyasını okur ve Python listesine çevirir."""
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, 'r', encoding='utf-8') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            # Dosya bozuksa veya boşsa hata almamak için boş liste dön
            return []

def save_to_db(data_list):
    """Python listesini alır ve JSON formatında diske kaydeder."""
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4)