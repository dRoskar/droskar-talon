os: windows
app.exe: ubuntu2004.exe
-
go goose:
    insert("cd")
    key(enter)
    insert("cd ../../mnt/c/stuff/cyg/cyg-recipes-lambda")
    key(enter)
    
go home:
    insert("cd")
    key(enter)
    insert("cd ../../mnt/c/")
    key(enter)
