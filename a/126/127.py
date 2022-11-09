import  os
lst = os.listdir(os.getcwd())
for i in lst:
    if i.endswith(".py"):
        print(i)
