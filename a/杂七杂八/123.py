with open("y.png","rb") as  file:
   with open("copy.png","wb") as ta:
        ta.write(file.read())