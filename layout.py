import flet as ft
from flet.controls.types import CrossAxisAlignment

def main(page: ft.Page):
    page.title = "Colunas"
    page.bgcolor = "red"
    page.add(
        ft.Container(
            expand=True,
            content=ft.Column(
                controls=[
                    ft.Text("Topo da Tela"),
                    ft.Button(content="Botão do Meio"),
                    ft.Text("Base da Tela")
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )
    )


ft.run(main)
