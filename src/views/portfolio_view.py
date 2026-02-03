import flet as ft
from src.components.property_card import property_card

# HATAYI BURADA DÜZELTTİK: Fonksiyon artık page ve api'yi kabul ediyor
def portfolio_view(page, property_api):
    # 1. Verileri ARTIK gerçek servisten (API) çekiyoruz!
    data = property_api.get_all_properties()
    
    # 2. Portföy Izgarası (Row)
    # alignment=CENTER ve horizontal_alignment=CENTER ile tam ortalıyoruz
    portfolio_grid = ft.Row(
        wrap=True,
        spacing=20,
        run_spacing=20,
        alignment=ft.MainAxisAlignment.CENTER, # Kartları kendi içinde ortalar
    )

    # 3. Gerçek verileri döngüye sokuyoruz
    for item in data:
        card = property_card(
            title=item.get("title", "İsimsiz"),
            price=item.get("price", "0"),
            location=item.get("location", "Belirtilmedi"),
            rooms=item.get("rooms", "-"),
            size=item.get("size", "0"),
            image_url=item.get("image_url", "https://picsum.photos/300/200")
        )
        
        # Her kartı 5'li dizilim için uygun bir genişlikle sarıyoruz
        # (Ekran genişliğine göre 250-280px idealdir)
        card_container = ft.Container(
            content=card,
            width=280, 
        )
        
        portfolio_grid.controls.append(card_container)
    
    # 4. Sayfa Düzeni ve Tam Ortalama
    return ft.Column(
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        # Sayfadaki tüm içeriği (başlık ve grid) yatayda ortalar
        horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
        controls=[
            ft.Container(height=20), # Üstten ferahlık
            ft.Text("🏠 Emlak Portföyü", size=32, weight="bold"),
            ft.Divider(height=20, color="transparent"),
            
            # Kartları içeren ana konteyner
            ft.Container(
                content=portfolio_grid,
                padding=10,
                alignment=ft.Alignment.CENTER
            ),
            
            ft.Divider(height=50, color="transparent"),
        ]
    )