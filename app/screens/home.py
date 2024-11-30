from nicegui import ui, native, app
from pathlib import Path

from webview import FOLDER_DIALOG


class Home:

    def __init__(self):
        input_path = None
        output_path = None

    async def choose_file(self):
        """"""
        files = await app.native.main_window.create_file_dialog(
            allow_multiple=False, dialog_type=FOLDER_DIALOG
        )
        if len(files) > 0:
            return files[0]
        else:
            raise ValueError("Folder Selection Canceled")

    async def set_input_path(self, e, selected_input):
        folder_path = await self.choose_file()
        self.input_path = Path(folder_path)
        selected_input.clear()
        with selected_input:
            ui.label(str(self.input_path))
            ui.button(
                "Change",
                icon="folder",
                on_click=lambda e: self.set_input_path(e, selected_input),
            )
        return None

    async def set_output_path(self):
        folder_path = await self.choose_file()
        self.output_path = Path(folder_path)
        ui.label(str(self.output_path))
        return None

    def screen(self):
        ui.label("TidyFiles")
        with ui.label() as selected_input:
            ui.button(
                "Input Folder",
                icon="folder",
                on_click=lambda e: self.set_input_path(e, selected_input),
            )

        ui.button("Output Folder", icon="folder", on_click=self.set_output_path)
