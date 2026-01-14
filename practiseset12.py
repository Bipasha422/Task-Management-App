f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("twinkle is present")
    f.close()