def mid_num(num_list):
    num_list.sort()
    if len(num_list)%2==0:
        mid_num=(num_list[int(len(num_list)/2)]+num_list[int(len(num_list)/2)-1])/2
    else:
        mid_num=num_list[int(len(num_list)/2-1)]
    return mid_num
'''当心差一错误'''
    # mid_num=num_list[int(len(num_list)/2)]
    # return mid_num
def add_sorted_list(list1, list2):
    list3 = list1 + list2
    list3.sort()
    return list3
import random
number1_list=[a for a in range(1,21)]
number1_copy=number1_list[:]
number2_list=[b for b in range(1,21)]#这里要是21，那么最后一个元素就是20，而不是19
number2_copy=number2_list.copy()
for i in range(random.randint(2,7),random.randint(15,20)):
    # number1_list.pop()
    # number2_list.pop()
    # number1_list.pop(random.randint(0,len(number1_list)-1))
    # number1_list.remove(random.choice(number1_list))
    number1_list.remove(number1_copy[i])
for x in range(random.randint(2,7),random.randint(15,20)):
    number2_list.remove(number2_copy[x])
integrated_list=add_sorted_list(number1_list,number2_list)
print(integrated_list)
str_my=input("Do you want to remove the duplicate numbers in the list?yes or no:")
if str_my=="yes":
    clear_list=[]
    for m in range(len(integrated_list)):
        if m==0:
            continue
        elif m>=1 and integrated_list[m]==integrated_list[m-1]:
            clear_list.append(integrated_list[m])
    print(clear_list)
    list1=[x for x in integrated_list if x not in clear_list]+clear_list    
    '''这里的clear_list是重复的元素，所以要用clear_list来判断，而不是用integrated_list来判断'''
    '''为了得到没有重复数字的列表'''    
    print(sorted(list1))
    resulted_num=mid_num(list1)
    print(resulted_num)
else:
    resulted_num=mid_num(integrated_list)
    print(resulted_num)        




























