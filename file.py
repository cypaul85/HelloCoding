try:
    file = open("file.txt", mode="a", encoding="UTF-8")
    file.write("Testing is being performed")
    file.close()
except Exception as e:
    print(e)
print("Pls check if the file is closed properly")
print("file.closed: ", file.closed)