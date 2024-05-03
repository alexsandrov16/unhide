import subprocess,time,os
import flet as ft

def main(page: ft.Page):
    page.title="unHide"
    page.window_height=400
    page.window_width=380
    page.window_resizable=False
    page.window_maximizable=False
    #page.vertical_alignment=ft.MainAxisAlignment.CENTER

    def handleOptions(device_name,dd):
        for option in dd.options:
            if device_name == option.key:
                return option
        return None
    
    # Obtener unidades
    def getDevices(dd):
        output=subprocess.run('fsutil fsinfo drives',capture_output=True).stdout.decode('utf-8').split()
        for device in output[1:]:
            if handleOptions(device,dd) == None:
                dd.options.append(ft.dropdown.Option(device))
        page.update()

    select=ft.Dropdown(hint_text="Seleccione la unidad a escanear")

    getDevices(select)

    page.add(
        ft.Container(
            margin=10,
            padding=10,
            alignment=ft.alignment.center
        ),
        ft.Container(
            select,
            margin=10,
            padding=10,
            alignment=ft.alignment.center
        ),
        ft.Container(
            ft.Row([
                ft.OutlinedButton(
                    text="Actualizar",
                    icon=ft.icons.REFRESH_ROUNDED,
                    on_click=lambda _:getDevices(select)
                ),
                ft.OutlinedButton(
                    text="Escanear",
                    icon=ft.icons.SEARCH
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY
            )
        ),
    )

ft.app(main,name='MyAPP')