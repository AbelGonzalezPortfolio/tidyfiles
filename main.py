import multiprocessing

multiprocessing.set_start_method("spawn", force=True)

from nicegui import ui, app

from app.screens.home import Home

home_screen = Home().screen
app.on_startup(home_screen)
ui.run(native=True, window_size=(800, 600), fullscreen=False)
