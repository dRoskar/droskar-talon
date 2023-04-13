import os
import time
import talon
from talon import Context, Module, ui, actions

mod = Module()
mod.list("installed_apps", desc="Installed apps")

ctx_default = Context ()
ctx_default.lists["user.installed_apps"] = {
    "note": "C:\\Program Files (x86)\\Notepad++\\notepad++.exe",
    "source": f"{os.getenv('USERPROFILE')}\\AppData\\Local\\SourceTree\\app-3.4.6\\SourceTree.exe"
}

@mod.action_class
class Actions:
    def app_open(path: str):
        """Open an application by path"""
        ui.launch(path=path)

    def app_focus(path: str):
        """Focus an application by path"""
        app = get_running_app(path)
        switcher_focus_app(app)

def switcher_focus_app(app: ui.App):
    """Focus application and wait until switch is made"""
    app.focus()
    t1 = time.perf_counter()
    while ui.active_app() != app:
        if time.perf_counter() - t1 > 1:
            raise RuntimeError(f"Can't focus app: {app.name}")
        actions.sleep(0.1)

def get_running_app(path: str) -> ui.App:
        """Get the running app with `path`."""
        for application in ui.apps(background=False):
            if os.path.basename(application.exe) == os.path.basename(path):
                return application
        raise RuntimeError(f'App not running: "{path}"')
