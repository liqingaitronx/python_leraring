import os
file_name = "sturdentdemo.txt"
def main():
    while True:
        menu()
        choice = int(input("请选择一个功能："))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice == 0:
                answer = input("您确认要退出系统?y/n")
                if answer == "y" or answer == "Y":
                    print("程序退出")
                    break
                else:
                    continue
            elif choice == 1:
                inster()
            elif choice == 2:
                serch()
            elif choice == 3:
                delect()
            elif choice == 4:
                update()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()
def menu():
    print("=======学生管理系统=====")
    print("--------功能菜单====")
    print("--------1、学生录入==")
    print("--------2、学生查找==")
    print("--------3、删除======")
    print("--------4、修改======")
    print("--------5、排序======")
    print("--------6、统计======")
    print("--------7、显示======")
    print("--------0、退出系统====")
def inster():
    student_list = [] # 用户新增多少个列表
    while True:

        id = input("请输入ID（如1001）")
        if not  id:
            break
        name = input("请输入姓名")
        if not name:
            break
        try:
            english = int(input("请输入英语成绩"))
            python = int(input("请输入""python成绩"))
            java = int(input("请输入java成绩"))
        except:
            print("请输入有效数字")
            continue
        student = {"id":id, "name":name, "english":english, "python":python, "java":java}
        student_list.append(student)
        ansewer = input("你是否要继续添加？y/n")
        if ansewer == "y":
            continue
        else:
            break
    save(student_list)
    print("学生录入完成")
def save(lst):
    try:
        stu_txt = open(file_name,"a",encoding="utf-8")
    except:
        stu_txt = open(file_name,"w",encoding="utf-8")
    for item in lst:
        stu_txt.write(str(item)+"\n")
        stu_txt.close()
def serch():
    student_query = []
    while True:
        id = " "
        name = " "
        if os.path.exists(file_name):
            model = input("ID查找请输入1,姓名查找请输入2")
            if model == "1":
                id = input("请输入你要查找的id")
            elif model == "2":
                name = input("请输入要查找的姓名")
            else:
                print("你输入格式有误")
            serch()
            with open(file_name,"r",encoding="utf-8") as  rfile:
                student = rfile.readlines()
                for item in student:
                    d = dict(eval(item))
                    if id != " " :
                        if d["id"] == id :
                            student_query.append(d)
                        elif name != " " :
                            if d["name"] == name:
                                student_query.append(d)
                student_show(student_query)
                student_query.clear()
                ansewer = input("你是否要继续添加？y/n")
                if ansewer == "y":
                    continue
                else:
                    break
        else:
            print("没有学生信息")
            return



def student_show(student_list):
   if student_list == 0 :
       print("无学生信息")
       return
   format_title = '{:^6}\t{:^10}\t{:^8}\t{:^9}\t{:^10}\t{:^8}\t'
   print(format_title.format("id","姓名","english","python","java","zong"))
   format_date = '{:^6}\t{:^10}\t{:^8}\t{:^9}\t{:^10}\t{:^8}\t'
   for item in student_list:
    print(format_date.format(item.get("id"),
                             item.get("name"),
                             item.get("english"),
                             item.get("python"),
                             item.get("java"),
                             int(item.get("english")) +int(item.get("python"))+int(item.get("java"))
          ))








def delect():
    while True:
        stu_id = input("请输入学生ID")
        if stu_id != " ":
            if os.path.exists(file_name): # 读取文件是否存在
                with open(file_name,"r",encoding="utf-8") as rfile: # 存在即读取
                    stu_old = rfile.readlines() # 只读模式，readline自动分析称列表，以列表模式输出
            else:
                stu_old = []
            flag = False #标记是否有删除
            if stu_old: #文件存在，用只写的方式
                with open(file_name,"w",encoding="utf-8") as wfile:
                    d = {}
                    for item in stu_old:
                        d = dict(eval(item)) #将字符串转为字典
                        if d["id"]!= stu_id: #用户输入不等于
                            wfile.write(str(d)+"\n")
                        else:
                            flag =True
                    if flag:
                        print(f"id{stu_id}的信息已经删除")
                    else:
                        print(f"id{stu_id}没有找到")
            else:
                print("无学生信息")
                break
            show()
            ansewer = input("你是否要继续删除？y/n")
            if ansewer == "y":
                continue
            else:
                break
        else:
            print("请输入正确的字符")


def update():
   # show()
    try:
        if os.path.exists(file_name):
            with open(file_name,"r",encoding="utf-8") as rfile:
                student_old= rfile.readlines()
        else:
            return
        student_id = input("请输入要修改的学生id")
        with open(file_name,"w",encoding="utf-8")as wfile:
            for item in student_old:
                d = dict(eval(item))
                if d["id"] == student_id:
                    print("找到信息，可以修改")
                    while True:
                        try:
                            d["name"] = input("请输入name")
                            d["english"] = input("请输入english成绩")
                            d["python"] = input("请输入python成绩")
                            d["java"] = input("请输入java成绩")
                        except:
                            print("你输入的信息有错误")
                        else:
                            break
                    wfile.write(str(d)+"\n")
                    print("修改成功")
            else:
                wfile.write(str(d) + "\n")
        ansewer = input("你是否要继续修改？y/n")
        if ansewer == "y":
          update()
    except:
        print("请输入正确id")







def sort():
    pass
def total():
    pass
def show():
    pass
    # f = open(file_name,"rb")
    # byte = f.readlines()
    # print(byte)
main()