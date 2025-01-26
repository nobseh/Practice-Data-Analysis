fhand = open("mbox-short.txt")

for line in fhand:
    line = line.rstrip()
    if line.find("@uct") == -1: continue
    print(line)

