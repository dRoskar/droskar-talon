from talon import Module, Context

mod = Module()
mod.list("tis_registers", desc="TIS registers")

ctx_default = Context ()
ctx_default.lists["user.tis_registers"] = {
    "ack": "acc",
    "up": "up",
    "down": "down",
    "left": "left",
    "right": "right",
    "nill": "nil",
    "any": "any",
    "last": "last"
}
