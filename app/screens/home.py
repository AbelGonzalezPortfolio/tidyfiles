from nicegui import ui, native, app
from pathlib import Path

from webview import FOLDER_DIALOG


class Home:

    def __init__(self):
        self.paths = {"input": "", "output": ""}

    async def choose_file(self):
        """"""
        files = await app.native.main_window.create_file_dialog(
            allow_multiple=False, dialog_type=FOLDER_DIALOG
        )
        if len(files) > 0:
            return files[0]
        else:
            raise ValueError("Folder Selection Canceled")

    async def set_path(self, target, select_ui):
        path = Path(await self.choose_file())
        self.paths[target] = path

        select_ui.clear()
        with select_ui:
            ui.label(str(path))

        print(self.paths)

    def screen(self):
        ui.label("TidyFiles")

        with ui.button(
            icon="folder",
            on_click=lambda: self.set_path("input", input_select_ui),
        ) as input_select_ui:
            ui.label("Select Input Folder")

        with ui.button(
            icon="folder", on_click=lambda: self.set_path("output", output_select_ui)
        ) as output_select_ui:
            ui.label("select Output Folder")
