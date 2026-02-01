import flet as ft

def property_add_form(on_submit_function):
    # Form alanlarını tanımlayalım
    title_input = ft.TextField(label="İlan Başlığı", hint_text="Örn: Kuzeykent'de 3+1 Daire")
    price_input = ft.TextField(label="Fiyat (TL)", keyboard_type=ft.KeyboardType.NUMBER)
    location_input = ft.Dropdown(
        label="Konum",
        options=[
            ft.dropdown.Option("Merkez"),
            ft.dropdown.Option("Kastamonu"),
        ],
    )
    rooms_input = ft.TextField(label="Oda Sayısı", hint_text="3+1")
    size_input = ft.TextField(label="Metrekare (m²)",keyboard_type=ft.KeyboardType.NUMBER)

    def submit_click(e):
        data = {
            "title": title_input.value,
            "price": price_input.value,
            "location": location_input.value,
            "rooms": rooms_input.value,
            "size": size_input.value
        }
        on_submit_function(data)
    
    return ft.Column(
        controls=[
            ft.Text("📝 Yeni İlan Detayları", size=25, weight="bold"),
            title_input,
            price_input,
            location_input,
            ft.Row([rooms_input, size_input], expand=True),
            ft.ElevatedButton(
                "İlanı Kaydet",
                icon=ft.Icons.SAVE,
                on_click=submit_click,
                style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_700, color=ft.Colors.WHITE)
            ),
        ],
        spacing=20,
        scroll=ft.ScrollMode.AUTO
    )