f = open("valprep.sh")
lst = []
class_to_int_mapping=dict()
count = 0
for line in f:
    words = line.split()
    if words[0] != "mkdir":
        lst.append(words[1:])
    else:
        class_to_int_mapping[words[2]] = count
        count +=1 
f.close()

f = open("val_map.txt", "w")

for e in lst:
    s = e[0]+" "+str(class_to_int_mapping[e[1][:-1]])+"\n"
    f.write(s)
f.close()
