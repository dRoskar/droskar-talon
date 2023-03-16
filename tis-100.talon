os: windows
app.exe: tis100.exe
-
move <user.number_string> {user.tis_registers}:
    insert("mov {number_string}, {tis_registers}")
    key(enter)
    
move {user.tis_registers} {user.tis_registers}:
    insert("mov {tis_registers_1}, {tis_registers_2}")
    key(enter)
    
add (<user.number_string> | {user.tis_registers}):
    insert("add {number_string or tis_registers}")
    key(enter)

sub (<user.number_string> | {user.tis_registers}):
    insert("sub {number_string or tis_registers}")
    key(enter)

nag:
    insert("neg")
    key(enter)

save:
    insert("sav")
    key(enter)

swap:
    insert("swp")
    key(enter)

nope:
    insert("nop")
    key(enter)
 
jump <user.text>: 
    insert("jmp {text}")
    key(enter)

zero <user.text>: 
    insert("jez {text}")
    key(enter)

not zero <user.text>: 
    insert("jnz {text}")
    key(enter)

greater <user.text>: 
    insert("jgz {text}")
    key(enter)

less <user.text>: 
    insert("jlz {text}")
    key(enter)

relative {user.tis_registers}: 
    insert("jro {tis_registers}")
    key(enter)

clear line: 
    key(backspace)
    key(end)
    key(shift-home)
    key(delete)
 
prod:
    key(home)
    insert("  ")
 
# node navigation
node up:
    key(ctrl-up)

node down:
    key(ctrl-down)

node left:
    key(ctrl-left)

node right:
    key(ctrl-right)

run program:
    key(f5)

documentation:
    key(f1)

hard exit:
    key(alt-f4)

settings():
    key_wait = 18
