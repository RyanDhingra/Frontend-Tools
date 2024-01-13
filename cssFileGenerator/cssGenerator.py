lines = []
classes = []
ids = []
names = []

with open("react.txt", "r") as f:
    lines = f.readlines()
    f.close()

for line in lines:
    words = line.split(" ")
    for word in words:
        if "className=" in word:
            if word[10] != "{":
                name = word[11:-1]

                clean_name = ""
                for letter in name:
                    if letter != ">" and letter != "'" and letter != '"':
                        clean_name += letter
                    else:
                        break
                clean_name = clean_name.replace(">", "")
                clean_name = clean_name.replace("'", "")
                classes.append(clean_name)
        elif "id=" in word:
            name = word[4:-1]
            ids.append(name)
            print(name)
    
no_dups = []

for name in classes:
    if name not in no_dups:
        no_dups.append(name)
    
classes = no_dups

with open("cssFile.css", "w") as cssFile:
    for c in classes:
        cssFile.write("." + c + " {")
        cssFile.write('\n')
        cssFile.write('\n')
        cssFile.write("}")
        cssFile.write('\n')
        cssFile.write('\n')
    for id in ids:
        cssFile.write("#" + id + " {")
        cssFile.write('\n')
        cssFile.write('\n')
        cssFile.write("}")
        cssFile.write('\n')
        cssFile.write('\n')
    cssFile.close()