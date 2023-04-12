from talon import Module, actions, ctrl

mod = Module()
dragging = False

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
