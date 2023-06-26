from talon import Module, ui

mod = Module()

def on_focus(win):
    print("on_focus", win)

ui.register("win_focus", on_focus)