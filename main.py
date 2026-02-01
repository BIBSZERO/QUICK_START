import flet as ft
from src.components.sidebar import show_sidebar

def main(page: ft.Page):
    page.title = "NikoCRM v1.0 - Emlak Yönetimi"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.spacing = 0

    # Ana İçerik Alanı
    content_area = ft.Column(expand=True, scroll=ft.ScrollMode.AUTO)

    # Sayfa Değiştirme Fonksiyonu
    def route_change(e):
        index = e.control.selected_index
        content_area.controls.clear()
        
        if index == 0:
            content_area.controls.append(ft.Text("📊 Genel İstatistikler", size=25, weight="bold"))
        elif index == 1:
            content_area.controls.append(ft.Text("🏠 Emlak Portföyü (Kastamonu)", size=25, weight="bold"))
        elif index == 2:
            content_area.controls.append(ft.Text("📝 Yeni İlan Kaydı", size=25, weight="bold"))
            
        page.update()

    # Web Uyumlu Çıkış Fonksiyonu
    def handle_logout(e):
        print("Çıkış yapılıyor...")
        page.launch_url("/") # Sayfayı yenileyerek oturumu sıfırlar

    # Sidebar Kurulumu
    sidebar = show_sidebar(route_change, handle_logout)

    # Sayfa Düzeni
    page.add(
        ft.Row(
            controls=[
                sidebar,
                ft.VerticalDivider(width=1, color=ft.colors.OUTLINE_VARIANT),
                ft.Container(content_area, padding=30, expand=True)
            ],
            expand=True,
        )
    )

    content_area.controls.append(ft.Text("Hoş geldin Buse! NikoCRM hazır.", size=25, weight="bold"))
    page.update()

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER, port=8000)