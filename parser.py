import re
import os

def list_rindex(li, x):
    for i in reversed(range(len(li))):
        if li[i] == x:
            return i
    raise ValueError("{} is not in list".format(x))

def seperation(script):
    lines = script.split('\n')
    parsed_lines = []
    for line in lines:
        line = line.strip()
        if line:
            matches = re.findall(r'(define|if|!|\|\||&&|\(|\)|[a-zA-Z0-9_]+)', line)
            parsed_lines.append(matches)
    return parsed_lines

#ubscript = """
#define Switch isUp
#define Switch isDown
#define Raycast hitDetection
#define Node canGoUp
#define Display display
#
#if (isUp&&hitDetection) then
#    canGoUp()
#    display(1,0,0,0)
#else
#    display(0,0,0,0)
#    if (isDown) then
#        display(0,1,0,0)
#    end
#end
#"""
class RUBScriptParser:
    def parse_folder(src):
        glarbed_together = [] # wtf is glarbed
        for path, subdirs, files in os.walk(src):
            for name in files:
                if name.endswith(".ubscript") or name.endswith(".ubs") or name.endswith(".rbs"):
                    with open(os.path.join(path, name),"r") as f:
                        glarbed_together.append(f.read())

        return RUBScriptParser.parse("\n\n".join(glarbed_together))

    def parse(script: str):
        parsed_lines = seperation(script)
        current_id = 1
        variables = {}
        object_types = [
            "Switch","Node","Raycast","Display"
        ]
        final = []
        inheritedifs = []

        for line in parsed_lines:
            #print(inheritedifs)
            #print(line)
            match line[0]:
                case "define":
                    if line[1] in object_types:
                        namespace = f"{line[1]}{current_id}"
                        if not line[2] in variables.keys():
                            variables[line[2]] = namespace
                            current_id += 1
                        else:
                            raise Exception(f"Variable name {line[2]} is already used.\nPlease use object.input() instead.")
                    else:
                        raise Exception(f"{line[1]} is not a valid object.")
                
                case "if":
                    ifstatement = line[line.index("("):list_rindex(line,")")]
                    generated = []
                    queue = []
                    queue2 = []
                    for i in ifstatement:
                        if i in variables.keys():
                            generated.append(variables[i])
                            if len(queue2) > 0:
                                generated.append(queue2[0])
                                queue2.pop(0)

                        if len(queue) > 0:
                            generated.append(queue[0])
                            queue.pop(0)

                        if i == "&&":
                            queue.append("-> AND")
                        elif i == "||":
                            queue.append("-> OR")
                        elif i == "!":
                            raise Exception(f"Not (or ! symbol) in if statements hasn't been implemented. Please use if else instead.")
                        
                    generated.append("->")
                

                    final.append("\n\n" + " ".join(generated))
                    inheritedifs.append(" ".join(generated))
                
                case "else":
                    inheritedifs[0] += " NOT ->"
                case "end":
                    inheritedifs.pop(0)
            
                case _:
                    generated = []
                    if line[0] in variables.keys() and line[1] == "(":
                        if line[-1] == ")":
                            args = line[2:-1]
                            if len(args) > 0:
                                generated.append("[" + ",".join(args) + "]")
                            generated.append(variables[line[0]])

                        else:
                            raise Exception(f"Missing ) in {line[0]}")
                    else:
                        raise Exception(f"I don't know what {line[0]} is.")
                    
                    final.append("\n" + " ".join(inheritedifs) + " " + "".join(generated))

        return " ".join(final).replace("  "," ")
        

#parsed_ubscript = parse_ubscript(ubscript)
#
#
#complex_text = generate_ub(parsed_ubscript)
#print(complex_text)