from talon import app, actions

def disable_speech():
    actions.speech.disable()

app.register("ready", disable_speech)
