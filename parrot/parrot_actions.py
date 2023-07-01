from talon import Module, actions, ctrl, noise, cron

import time
import threading

mod = Module()
dragging = False
cluck_active = False
cron_job = None

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

    def noise_copy_paste():
        """Paste the selected text, on double noise, copy it."""
        #actions.key("ctrl-c")
        global cron_job
        if cron_job:
            actions.key("ctrl-c")
            actions.key("ctrl-shift-alt-win-q")
            print("double noise")
            
            cron.cancel(cron_job)
            cron_job = None
        else:
            cron_job = cron.after("500ms", on_after)

def on_after():
    global cron_job
    cron_job = None
    actions.key("ctrl-v")
    print("single noise")
    
# def on_pop(_active):
#     global cluck_active
#     if not cluck_active:
#         time.sleep(0.01)
#         ctrl.mouse_click(button=0, hold=16000)
#     else:
#         print("Mouse button not clicked due to cluck being active")

# noise.register("pop", on_pop)