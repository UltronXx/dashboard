import flet as ft
from flet import (
    ElevatedButton,
    FilePicker,
    FilePickerResultEvent,
    Page,
    Container,
    Column,
    Row,
    Text,
    Icons,
)


def main(page: Page):

    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    def pick_files(e: FilePickerResultEvent):
        picked_files = e.files
        # print("\n".join(map(lambda file: f"file name: {file.name}", picked_files)))
        print(picked_files)

    selected_files = Text()
    file_picker_dialog = FilePicker(on_result=pick_files)

    page.overlay.extend([file_picker_dialog])

    choose_button = Container(
        height=40,
        width=150,
        bgcolor="blue",
        alignment=ft.alignment.center,
        border_radius=8,
        content=Text(value="Choose", color="white"),
        on_click=lambda _: file_picker_dialog.pick_files(
            allow_multiple=True
        )
    )

    page.add(
        Container(
            height=400,
            margin=ft.margin.only(left=30, top=0, right=30, bottom=0),
            bgcolor="#f5f5f7",
            border_radius=32,
            alignment=ft.alignment.center,
            content=Container(
                height=400,
                margin=20,
                border_radius=12,
                # bgcolor="green",
                border=ft.border.all(width=2, color="#cecece"),
                alignment=ft.alignment.center,
                content=Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                    controls=[
                        Text(value="\"Drag files here or Choose\"", color="#aaaaaa"),
                        choose_button,
                    ]
                )
            ),
        ),
        Container(height=12),
        selected_files
    )


ft.app(target=main)
