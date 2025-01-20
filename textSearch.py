
file = open("mbox-short.txt")

for  line in file:
    line = line.rstrip()
    # Skip the line that does not contain "From
    if line.find("From:") >= 0:
        # Print the line that contains "From:"
        print(line)

print("\nDONE!...")