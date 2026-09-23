import os

if os.path.exists('mbox-short.txt'):
    print("System Ready: File detected.")
    print(f"File Size: {os.path.getsize('mbox-short.txt')} bytes")
else:
    print("Error: File not found.")
    print(f"Current Working Directory: {os.getcwd()}")

fhand = open('mbox-short.txt', 'r')