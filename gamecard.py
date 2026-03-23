import flet as ft

def main(page: ft.Page):
    #  Configurações da Janela
    page.title = "Gamer Card"
    page.bgcolor = "1E1E1E"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Cabeçalho: Avatar (emoji) e Nome do Lado
    cabecelho = ft.Row(
        controls=[
            ft.Text("🥷", size=60),
            ft.Column(
                controls=[
                    ft.Text("SHADOW NINJA", size=24, weight="bold", color="white"),
                    ft.Text("Nivel 42 - Ninja das Somnbras", size=24, color="grey300"),
                ], spacing=2
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

#Status: Barra de HP, MP e XP