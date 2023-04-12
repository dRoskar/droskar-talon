import os

from talon import ctrl, noise
def on_pop(_active):
    ctrl.mouse_click(button=0, hold=16000)


noise.register("pop", on_pop)
