os: windows
app.exe: ConEmu64.exe
-
terraform init:
    insert("tfi")
    key(enter)

terraform plan:
    insert("tfp")
    key(enter)

terraform apply:
    insert("tfaa")
    key(enter)
