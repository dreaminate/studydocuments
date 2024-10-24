count_input_1=0
count_input_2=0
while count_input_1<=3 :
    if count_input_1==0:
        input_num_1=input("Please input your password one:")
        count_input_1 += 1
    if input_num_1=="123abc" :
        if count_input_2==0:
            input_num_2=input("密码一正确，请输入密码2：")
            count_input_2 += 1
        while count_input_2<=3 :
            if input_num_2=="asdfjkl" :
                print("验证正确")
            if count_input_2>=3:
                break
            else:
                count_input_2 += 1
                input_num_2=input("密码二错误，请重新输入：")
    if count_input_1>=3 or count_input_2>=3 :
        break
    else:
        input_num_1=input("密码一错误，请重新输入：")
        count_input_1 += 1
if count_input_1>=3 or count_input_2>=3 :
    print("验证失败")
                
        
















































