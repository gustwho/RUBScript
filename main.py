from parser import RUBScriptParser as rsp
import sys

if len(sys.argv) < 3:
    print("Yknow, you need 2 arguments.")
    print("['folder'/'file'] [path]\n\n")
else:
    path = " ".join(sys.argv[2:])
    if sys.argv[1] == "folder":
        with open("output/folder_output.txt","w+") as f:
            f.write(rsp.parse_folder(path))
    elif sys.argv[1] == "file":
        with open("output/output.txt","w+") as f:
            with open(path,"r") as g:
                f.write(rsp.parse(g.read()))
    else:
        print("1: 'folder'/'file'")