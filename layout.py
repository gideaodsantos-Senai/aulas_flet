import flet as ft
import datetime


def main(page: ft.Page):
    page.title = "iPhone Pro Home"
    page.bgcolor = "black"
    page.padding = 0
    page.spacing = 0
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    # ==============================
    # STATUS BAR COM HORA DINÂMICA
    # ==============================

    clock_text = ft.Text(color="white", size=16, weight="bold")

    def update_clock():
        now = datetime.datetime.now()
        clock_text.value = now.strftime("%H:%M")
        page.update()

    page.timer_interval = 1000
    page.on_timer = lambda e: update_clock()
    update_clock()

    status_bar = ft.Container(
        padding=ft.padding.symmetric(horizontal=20, vertical=10),
        content=ft.Row(
            alignment="space_between",
            controls=[
                clock_text,
                ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.SIGNAL_CELLULAR_4_BAR,
                                color="white", size=16),
                        ft.Icon(ft.Icons.WIFI, color="white", size=16),
                        ft.Icon(ft.Icons.BATTERY_FULL, color="white", size=16),
                    ],
                    spacing=5
                )
            ]
        )
    )

    # ==============================
    # FUNÇÃO DE ÍCONE COM ANIMAÇÃO
    # ==============================

    def app_icon(icon, label, color):
        container = ft.Container(
            width=70,
            height=70,
            bgcolor=color,
            border_radius=22,
            alignment=ft.Alignment(0, 0),
            animate_scale=200,
            content=ft.Icon(icon, color="white", size=32),
        )

        def on_click(e):
            container.scale = 0.85
            page.update()
            container.scale = 1
            page.update()

        container.on_click = on_click

        return ft.Column(
            controls=[
                container,
                ft.Text(label, size=12, color="white", text_align="center")
            ],
            horizontal_alignment="center",
            spacing=6
        )

    # ==============================
    # PÁGINA 1
    # ==============================

    page1 = ft.GridView(
        expand=True,
        max_extent=90,
        spacing=20,
        run_spacing=20,
        controls=[
            app_icon(ft.Icons.CALL, "Telefone", "#34C759"),
            app_icon(ft.Icons.MESSAGE, "Mensagens", "#30D158"),
            app_icon(ft.Icons.CAMERA_ALT, "Câmera", "#5856D6"),
            app_icon(ft.Icons.PHOTO, "Fotos", "#FF2D55"),
            app_icon(ft.Icons.MAP, "Mapas", "#FF9500"),
            app_icon(ft.Icons.MUSIC_NOTE, "Música", "#AF52DE"),
            app_icon(ft.Icons.SETTINGS, "Ajustes", "#8E8E93"),
            app_icon(ft.Icons.PUBLIC, "Safari", "#0A84FF"),
        ]
    )

    # ==============================
    # PÁGINA 2 (Swipe)
    # ==============================

    page2 = ft.GridView(
        expand=True,
        max_extent=90,
        spacing=20,
        run_spacing=20,
        controls=[
            app_icon(ft.Icons.FAVORITE, "Saúde", "#FF375F"),
            app_icon(ft.Icons.SHOPPING_CART, "Store", "#5E5CE6"),
            app_icon(ft.Icons.GAMES, "Jogos", "#FF9F0A"),
            app_icon(ft.Icons.MAIL, "Mail", "#007AFF"),
        ]
    )

    # ==============================
    # SWIPE ENTRE PÁGINAS
    # ==============================

    pages = ft.PageView(
    expand=True,
    children=[page1, page2]
)

    # ==============================
    # DOCK FIXO
    # ==============================

    dock = ft.Container(
        height=90,
        padding=15,
        bgcolor="#1C1C1E",
        border_radius=30,
        content=ft.Row(
            alignment="space_evenly",
            controls=[
                app_icon(ft.Icons.PHONE, "", "#34C759"),
                app_icon(ft.Icons.SMS, "", "#30D158"),
                app_icon(ft.Icons.PUBLIC, "", "#0A84FF"),
                app_icon(ft.Icons.MUSIC_NOTE, "", "#FF2D55"),
            ]
        )
    )

    # ==============================
    # WALLPAPER + ESTRUTURA FINAL
    # ==============================

    page.add(
        ft.Container(
            expand=True,
            image_src="https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
            image_fit=ft.ImageFit.COVER,
            content=ft.Column(
                controls=[
                    status_bar,
                    ft.Container(expand=True, padding=20, content=tabs),
                    dock,
                    ft.Container(height=10)
                ],
                spacing=0
            )
        )
    )

ft.app(target=main)