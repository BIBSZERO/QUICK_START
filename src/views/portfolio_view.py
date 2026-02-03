import flet as ft
from src.components.property_card import property_card

def portfolio_view():
    data = [
        {
            "id": "XYZ001",
            "title": "Kuzeykent Modern 3+1",
            "price": "3.500.000",
            "location": "Kastamonu, Kuzeykent",
            "rooms": "3+1",
            "size": "145",
            "image_url": "https://picsum.photos/id/1/300/200"
        } for i in range(15)
    ]
    
    portfolio_view = ft.Row(
        wrap=True,
        spacing=20,
        run_spacing=20,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    for item in data:
        card = property_card(
            title=item["title"],
            price=item["price"],
            location=item["location"],
            rooms=item["rooms"],
            size=item["size"],
            image_url=item["image_url"]
        )
        portfolio_view.controls.append(card)
    
    return ft.Column(
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls = [
            ft.Text("🏠 Emlak Portföyü", size=30, weight="bold"),
            ft.Divider(height=10, color="transparent"),
            portfolio_view,
            ft.Divider(height=50, color="transparent"),
        ]
    )