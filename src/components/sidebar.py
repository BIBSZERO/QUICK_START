import flet as ft

def show_sidebar(on_change_function, logout_function):
    # Ana menü yapısı
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=200,
        group_alignment=-1.0, # Öğeleri en tepeye yaslar
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.DASHBOARD_OUTLINED,
                selected_icon=ft.icons.DASHBOARD,
                label="Özet",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.HOME_WORK_OUTLINED,
                selected_icon=ft.icons.HOME_WORK,
                label="Portföy",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.ADD_CIRCLE_OUTLINE,
                selected_icon=ft.icons.ADD_CIRCLE,
                label="İlan Ekle",
            ),
        ],
        on_change=on_change_function,
        expand=True, 
    )

    # Rail'i bir Column içine alarak en alta buton ekliyoruz
    return ft.Container(
        content=ft.Column(
            controls=[
                rail, # Üstteki menüler
                ft.Container( # Çıkış butonu alt alanı
                    content=ft.IconButton(
                        icon=ft.icons.LOGOUT_ROUNDED,
                        icon_color=ft.colors.RED_400,
                        icon_size=35,
                        tooltip="Güvenli Çıkış",
                        on_click=logout_function
                    ),
                    padding=ft.padding.only(bottom=20),
                    alignment=ft.alignment.center
                ),
            ],
            expand=True,
        ),
        width=110,
        bgcolor=ft.colors.SURFACE_CONTAINER_HIGHEST, # Renk hatası düzeltildi
    )