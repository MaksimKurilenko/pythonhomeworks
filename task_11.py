ip = input("Please enter IP-address:")
parts = ip.split(".")
if len(parts)!= 4:
    print("Invalid IP. IF could only contain 4 parts.")
for part in parts:
    if not part.isdigit():
        print("Invalid IP. IP could only contain digits.")
num = int(part)
if num <0 or num>255:
    print("Invalid IP. IP parts could only be in range 0-255.")
else: print ("Valid IP")
