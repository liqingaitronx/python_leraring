

"""
# 伪代码
模拟进入火车站
    - 安检 是否有危险品
        - 如果没有危险品 -> 可以进入火车站
            - 判断车票 是否有车票
                - 如果有车票 -> 可以上火车
                - 如果没有火车站 -> 请买火车票
        - 如果有危险品 -> 不可以进入火车站
        
"""

# 定义一个变量 判断是否有危险品 True 就代表没有危险品
flag = True
# 定义一个变量 判断是否有火车票 如果为1 代表有火车票 其他认为没有火车票
chePiao = 11
# 判断是否有危险品
if flag:
    print("没有危险品 可以进入火车站")
    # 判断有没有火车票
    if chePiao == 1:
        print("可以上火车")
    else:
        print("没有火车票 请买票")
else:
    print("有危险品 不许进入火车站")



