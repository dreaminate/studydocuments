count_1=0
count_2=0
while count_1<=3 and count_2 <=3 :
    if count_1==0:
        num_1=input("请输入第一次密码：")
        count_1 += 1
    if num_1=="123abc":
        num_2=input("请输入第二次密码：")
        count_2 += 1
        if num_2=="asdfjkl":
            print("验证成功")
            break
        if num_2!="asdfjkl" :
            if count_2>=3:
                break
            num_1=input("第二次密码错误，请重新输入第一次密码：")
            count_1 += 1
            continue
    if num_1!="123abc":
        if count_1>=3:
            break
        num_1=input("第一次密码错误，请重新输入：")
        count_1 += 1
        continue
if count_1>=3 or count_2>=3:
    print("验证失败")

          
   




    


    








































