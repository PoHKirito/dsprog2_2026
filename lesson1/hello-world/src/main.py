import flet as ft


def main(page: ft.Page):
    page.title = "Hello World"
    counter = ft.Text("0", size=50, data=0)

    def change_count(event):
        counter.data += event.control.data
        counter.value = str(counter.data)

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, key="increment", data=1, on_click=change_count,
    )
    page.add(ft.SafeArea(
        expand=True,
        content=ft.Container(
            alignment=ft.Alignment.CENTER,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("Hello World", size=24),
                    counter,
                    ft.IconButton(
                        icon=ft.Icons.REMOVE, key="decrement", data=-1,
                        tooltip="−1", on_click=change_count,
                    ),
                ],
            ),
        ),
    ))


if __name__ == "__main__":
    ft.run(main)
