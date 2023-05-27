os: windows
app.exe: cmd.exe
-
go parrot:
    insert("cd C:\stuff\parrot.py")
    key(enter)
    insert(".venv\Scripts\\activate.bat")
    key(enter)
    insert("python settings.py")
    key(enter)

python version:
    insert("python --version")
    key(enter)