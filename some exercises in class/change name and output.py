name_1=input("请输入你的名字：")
users_age=int(input("请输入你的年龄："))

name_list=[]
name_calling_list=["小朋友","同学","哥哥","同志"]
name_list.append(name_1)
name_list_contenporary_1=name_list[0]
if  users_age>=22:
    print(f"\t\t\t{name_list_contenporary_1}"+f"{name_calling_list[3]}"+"人生苦短，请用Python，前途无量")
elif 22>users_age>=18:
    print(f"\t\t\t{name_list_contenporary_1}"+f"{name_calling_list[2]}"+"人生苦短，请用Python，前途无量")
elif 18>users_age>=12:
    print(f"\t\t\t{name_list_contenporary_1}"+f"{name_calling_list[1]}"+"人生苦短，请用Python，前途无量")
else:
    print(f"\t\t\t{name_list_contenporary_1}"+f"{name_calling_list[0]}"+"人生苦短，请用Python，前途无量")