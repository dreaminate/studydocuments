classinfo={"english":32,"math":64,"chengxusheji":40}
search_count=0
while search_count<=3:
    search_name=input("Please input the name of the course:")
    search_count+=1
    if search_name in classinfo:
        print(f"The score of {search_name} is {classinfo[search_name]}")
    if search_name not in classinfo:
        print("The course is not in the dictionary.")
        continue
    if search_count==3:
        print("You have searched all objects.")
        break
if search_count>3:
    print("You have tried too many times.")







































































