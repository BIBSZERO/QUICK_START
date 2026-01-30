import flet as ft

def main(page: ft.Page):
    # Sayfa genel ayarları
    page.title = "Flet Web Uygulaması"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    
    # Sayfa içeriği
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text("Web Uygulaması Yayında!", size=30, weight=ft.FontWeight.BOLD),
                    ft.Text("Port: 8000 üzerinden çalışıyor", size=16),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=30,
            border_radius=15,
            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST, 
        )
    )

if __name__ == "__main__":
    ft.run(
        main, 
        view=ft.AppView.WEB_BROWSER, 
        port=8000
    )