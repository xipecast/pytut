1. make a python file through 'touch'
2. add the shebang up top.
#!/usr/bin/env python3
3. make it an executable file.
in shell, 'chmod +x <filename>

interestingly enough, I actually didn't have to make it executable beforehand.
But if i need to I will add this step.

Actually I think I wont have to chmod it, if the file is only going to be called LOCALLY, however for just about everying, I'm going to want to call it globally. so

chmod +x /path/to/file

It's important to remember that first backslash before, I got a not a directory msg.


PATH is tricky for me so I am looking into it.

right now I only want to add to path temporarliy.

the 'export' command works, temporarily, the 'unset' command will undo this.
export PATH="/home/boss/repos:$PATH"
export PATH="</path/to/?filename>:$PATH"

it kinda worked as in accepted, and confirmining the new change to the $PATH I see it. but I still cannot call it globally.


for now we will skip this step.

## Strings


