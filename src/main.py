import flet as ft
from flet import (
    Page,
    Container,
    Row,
    Column,
    Text,
    Image,
    MainAxisAlignment,
    CrossAxisAlignment,
    alignment,
    padding,
    app
)


from pathlib import Path
assets = f"{Path(__file__).parent}/src/assets"

def main(page: Page) -> None:
    page.title = "Dashboard"

    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    page.window.height = 850
    page.window.width = 450

    page.theme_mode = "light"
    page.bgcolor = "#EBECF1"

    page.fonts = {
        "bold": "fonts/MonaSans-Bold.ttf",
        "regular": "fonts/MonaSans-Regular.ttf",
        "medium": "fonts/MonaSans-Medium.ttf",
        "semi bold": "fonts/MonaSans-SemiBold.ttf",
    }


    def highlight(e: ft.ControlEvent) -> None:
        # Change UI
        _text_color = e.control.content.controls[1]
        _text_color.color = "#f5f5f7" if _text_color.color == "#1D1D1D" else "#1D1D1D"

        _bgcolor = e.control
        _bgcolor.bgcolor = "#1D1D1D" if e.control.bgcolor == "#FAFAFA" else "#FAFAFA"

        _color = e.control.content.controls[0]
        _color.color = "#f5f5f7" if _color.color == "#1D1D1D" else "#1D1D1D"

        # Update UI
        general.update()
        tools.update()
        personal.update()

    general_icons = {
        "Dashboard": "menu.svg",
        "My Subscription": "star.svg",
        "Add Credit Card": "card.svg",
        "Receipts": "printer.svg"
    }

    tools_icons = {
        "Set Up Devices": "device.svg",
        "DNS Settings": "settings.svg"
    }

    personal_icons = {
        "Change Password": "lock.svg",
        "Sign Out": "exit.svg"
    }

    general = Column(controls=[], spacing=5)
    for name, icon in general_icons.items():
        general.controls.append(
            Container(
                height=52,
                bgcolor="#FAFAFA",
                border_radius=10,
                padding=padding.only(left=15),
                content=Row(
                    spacing=15,
                    controls=[
                        Image(src=f"icons/{icon}", scale=1, color="#1D1D1D"),
                        Text(value=f"{name}", font_family="medium", color="#1D1D1D")
                    ]
                ),
                on_hover=lambda e: highlight(e)
            ),
        )

    tools = Column(controls=[], spacing=5)
    for name, icon in tools_icons.items():
        tools.controls.append(
            Container(
                height=52,
                bgcolor="#FAFAFA",
                border_radius=10,
                padding=padding.only(left=15),
                content=Row(
                    spacing=15,
                    controls=[
                        Image(src=f"icons/{icon}", scale=1, color="#1D1D1D"),
                        Text(value=f"{name}", font_family="medium", color="#1D1D1D")
                    ]
                ),
                on_hover=lambda e: highlight(e)
            )
        )

    personal = Column(controls=[], spacing=5)
    for name, icon in personal_icons.items():
        personal.controls.append(
            Container(
                height=52,
                bgcolor="#FAFAFA",
                border_radius=10,
                padding=padding.only(left=15),
                content=Row(
                    spacing=15,
                    controls=[
                        Image(
                            src=f"icons/{icon}", scale=1,
                            color="red800" if name == "Sign Out" else "#1D1D1D"
                        ),
                        Text(
                            value=f"{name}", font_family="medium",
                            color="red800" if name == "Sign Out" else "#1D1D1D"
                        )
                    ]
                ),
                on_hover=lambda e: highlight(e)
            )
        )

    page.add(
        Container(
            height=620,
            width=270,
            content=Container(
                padding=padding.only(left=20, top=20, right=20, bottom=20),
                bgcolor="white",
                border_radius=15,
                content=Column(
                            alignment=MainAxisAlignment.SPACE_EVENLY,
                            controls=[
                                # General
                                Container(
                                    content=Column(
                                        controls=[
                                            Text(
                                                value="General",
                                                font_family="medium",
                                                color="#B8B8BB"
                                            ),
                                            general,
                                        ]
                                    )
                                ),
                                Container(
                                    content=Column(
                                        controls=[
                                            Text(
                                                value="Tools",
                                                font_family="medium",
                                                color="#B8B8BB"
                                            ),
                                            tools,
                                        ]
                                    )
                                ),
                                Container(
                                    content=Column(
                                        controls=[
                                            Text(
                                                value="Personal",
                                                font_family="medium",
                                                color="#B8B8BB"
                                            ),
                                            personal,
                                        ]
                                    )
                                ),
                            ]
                        )
            )
        )
    )
    page.update()


if __name__ == '__main__':
    app(target=main, assets_dir=assets)