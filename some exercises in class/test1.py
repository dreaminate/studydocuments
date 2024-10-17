# print("{a}+{b}={c}".format(a=1,b=2,c=3))# 左对齐，填充空格，宽度为10
# print("{:<10}".format("left"))

# # 右对齐，填充空格，宽度为10
# print("{:>10}".format("right"))

# # 居中对齐，填充空格，宽度为10
# print("{:^10}".format("center"))

# # 使用*填充，宽度为10，居中对齐
# print("{:*^10}".format("Kimi"))
# my_list=["打游戏","看电影","看书","学习","睡觉","打游戏"," ","打游戏"," ","打游戏",                 " ","打游戏"," "]

# my_list_2=[range(1,10)]
# my_list_3=list(range(1,10))
# my_list_2.append(my_list_3)
# print(my_list_2)
bok_name="Python 编程从入门到实践"
print(bok_name.removeprefix("thon"))