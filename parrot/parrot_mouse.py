from talon import Module, actions, ctrl, noise

import time
import threading

mod = Module()
dragging = False
cluck_active = False

@mod.action_class
class Actions:
    def toggle_drag():
        """Toggle mouse drag on and off."""
        global dragging
        dragging = not dragging
        if dragging:
            ctrl.mouse_click(button=0, down=True)
        else:
            ctrl.mouse_click(button=0, up=True)
    
    def mouse_click(button: int = 0):
        """Click the mouse button."""
        ctrl.mouse_click(button=button, hold=16000)

    def cluck():
        """Detect a cluck, And mark it as active for a hundred milliseconds """
        global cluck_active
        cluck_active = True
        print("cluck active")
        def cluck_inactive():
            global cluck_active
            time.sleep(0.1)
            cluck_active = False
            print("cluck inactive")
        threading.Thread(target=cluck_inactive).start()

def on_pop(_active):
    global cluck_active
    if not cluck_active:
        time.sleep(0.01)
        ctrl.mouse_click(button=0, hold=16000)
    else:
        print("Mouse button not clicked due to cluck being active")

noise.register("pop", on_pop)