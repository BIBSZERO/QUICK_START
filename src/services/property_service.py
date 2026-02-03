import uuid
from src.database import load_from_db, save_to_db

class PropertiesService:
    def __init__(self):
        self.properties = load_from_db()
        print(f"--- 🏠 Servis Hazır: {len(self.properties)} ilan yüklendi. ---")
    
    def get_all_properties(self):
        return self.properties
    
    def add_property(self,data):
        try:
            data["id"] = str(uuid.uuid4().hex[:6]).upper()
            self.properties.append(data)
            save_to_db(self.properties)
            return True, f"İlan #{data['id']} başarıyla eklendi."
        except Exception as e:
            return False, f"Hata oluştu:{str(e)}"
        
    def delete_property_by_id(self, prop_id):
        original_count = len(self.properties)
        self.properties = [p for p in self.properties if str(p.get("id")) != str(prop_id)]
        if len(self.properties) < original_count:
            save_to_db(self.properties)
            return True, "İlan silindi."
        return False, "İlan bulunamadı."
    
    def search_properties(self, query):
        query = query.lower()
        return [
            p for p in self.properties
            if query in p.get("title", "").lower() or query in p.get("location", "").lower()
        ]