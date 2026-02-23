import flet as ft


def main(page: ft.Page):

    def mostrar_mensagem(e):
        page.add(
            ft.Text("Eu vou ser o rei dos Piratas")
        )

    page.add(
        ft.Text("Olá, meu nome é Luffy"),
        ft.Image(
            src="images/luffy.png",
            width=150,
            height=150
        ),
        ft.Button(
            content="Clique Aqui",
            on_click=mostrar_mensagem
        )
    )


ft.run(main)
