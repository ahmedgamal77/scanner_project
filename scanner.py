import re

def ident_detect(identifer):
    if(identifer == '+'):
        return "addation"
    elif(identifer == '-'):
        return "subtracion"
    elif(identifer == '='):
        return "conditional equal"
    elif(identifer == '*'):
        return "multiplication"
    elif(identifer == '/'):
        return "division"
    elif(identifer == '<'):
        return "smaller than"
    elif(identifer == '('):
        return "opening bracket"
    elif(identifer == ')'):
        return "closing bracket"
    elif(identifer == ':='):
        return "assign"
    elif(identifer == ';'):
        return "semi column"
    else:
        return("identifer")


file = open("example.txt", "r")
f = open("output.txt", "w")
file_lines = file.read()

comments = re.findall("\{(.*?)\}",file_lines)
for comment in comments:
    file_lines=file_lines.replace('{'+comment+'}' ," ")



lines = file_lines.splitlines( )

for line in lines :
    for words in line.split():
        reserved_words=re.search("read|if|then|else|end|repeat|until|write",words)
        if reserved_words:
            f.write(str(reserved_words.group()) + " , reserved word \n")
            continue
        
        while(len(words)!=0):
            numbers =  re.search("[0-9]+",words)
            if (numbers)and (numbers.start()==0):
                f.write(str(numbers.group()) + " , number  \n")
                words=words.replace(numbers.group(),"")
            identifers = re.search("^[a-zA-Z]([a-zA-Z]|[0-9]|_)*",words)
            if (identifers )and (identifers.start()==0):
                f.write(str(identifers.group()) + " , identifer  \n")
                words=words.replace(identifers.group(),"")
            special_char = re.search("\+|-|\*|/|=|<|\(|\)|;|:=",words)
            if special_char and (special_char.start()==0):
                f.write(str(special_char.group()) + " , "+  ident_detect(special_char.group())  +"\n")
                words=words.replace(special_char.group(),"")
            

        
            

    

#print(identifers)
