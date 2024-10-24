n=int(input("请输入一个自然数："))
number_list=[]
for x in range (1,n+1):
    multiple=x
    for y in range (1,x):
        multiple=multiple*y
    print(f"{x}!={multiple}")
    number_list.append(multiple)
sum_number=sum(number_list)
print(f"1!+2!+3!+...+{n}!={sum_number}")
































































