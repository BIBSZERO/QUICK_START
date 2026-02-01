import flet as ft

def property_card(title, price, location, rooms, size, image_url):
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Image(
                    # 1. Görsel Alanı
                    ft.Image(
                        src=image_url,
                        width=300,
                        height=200,
                        fit="cover",
                        border_radius=ft.border_radius.only(top_left=15, top_right=15),
                    ),
                    # 2.Bilgi Alanı
                    ft.Container(
                        padding=15,
                        content=ft.Column(
                            controls=[
                                ft.Text(title, weight="bold", size=18),
                                ft.Row(
                                    [
                                        ft.Icon(ft.Icons.LOCATION_ON, size=16, color=ft.Colors.RED_400),
                                        ft.Text(location, size=14, color=ft.Colors.GREY_400)
                                    ]
                                ),
                                ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                                ft.Row(
                                [
                                    ft.Text(f"🛏️ {rooms}", size=12),
                                    ft.Text(f"📏 {size} m²", size=12),
                                ],
                                #alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                ),
                                ft.Text(
                                    f"{price} ₺", 
                                    size=20, 
                                    weight="bold", 
                                    color=ft.Colors.GREEN_400
                                ),
                            ],
                            spacing=5
                        ),
                    ),
                ),
            ],
        ),
        width=300,
        bgcolor=ft.Colors.SURFACE_CONTAINER_LOW,
        border_radius=15,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=10,
            color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
        ),
    )