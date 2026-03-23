import flet as ft


def main(page: ft.Page):
    
    def mostrar_mensagem(e):
        page.add(
            ft.Text("Pow! Pow!")
        )

    page.add(
        ft.Text("Free Fire MAX"),
        ft.Image(
            src="images/ff.png",
            width=150,
            height=150
        ),
        ft.Button(
            content="Famoso 3 capa ",
            on_click=mostrar_mensagem
        )
    )


ft.run(main)
