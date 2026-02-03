import flet as ft

def property_card(title, price, location, rooms, size, image_url):
    return ft.Card(
        shadow_color=ft.Colors.ON_SURFACE_VARIANT,
        content=ft.Container(
            width=300,
            padding=10,
            content=ft.Column(
                controls=[
                    ft.Image(src=image_url, width=300, height=200, fit="cover"),
                    ft.Text(title, size=18, weight="bold"),
                    ft.Text(f"Fiyat: {price}", size=16, color=ft.Colors.GREEN),
                    ft.Text(f"Konum: {location}", size=14),
                    ft.Text(f"Oda Sayısı: {rooms}", size=14),
                    ft.Text(f"Büyüklük: {size} m²", size=14),
                ],
                spacing=10, 
            )
        ),
    )