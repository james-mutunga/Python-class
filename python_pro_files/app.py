file = open('example.txt', 'r')
#                           ^
#                         means
#                          read

for line in file:
    line = line.strip()
    # This removes the extra spaces towards the end and in the beginning
    print(line)
    if not line.startswith('From '):
    # If the line we have does not start with 'From' then we will continue
        continue
    words = line.split()
    print(words[2])