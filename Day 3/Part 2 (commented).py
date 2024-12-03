#===IMPORT-MODULES===
import re

#===MAIN===
with open("input.txt", "r") as f:
    print(sum( #Sum list of multiplied values
        x for xs in [ #Decrease array dimension by 1
            list(map(
                lambda x: int(x[0])*int(x[1]), x #Multiply pairs of values together
                )) for x in [
                    re.findall("mul\((\d+),(\d+)\)", x) for x in [ #Find all "mul(a, b)"" and return [a, b]
                        x for xs in [ #Decrease array dimension by 1
                            re.split("(?=don?'?t?\(\))", "".join( #Split the text wherever there's a "do()" or "don't()", but keep the "do()" or "don't()"
                                [lines.strip("\n") for lines in f] #Write lines of input into a list removing "\n" characters, then join them into a single string
                                ))
                            ] for x in xs
                        ] if not re.match("don't\(\).*", x) #Exclude strings from line 11 if they begin with "don't"
                    ]
            ] for x in xs
        ))