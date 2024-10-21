'''练习4.1'''
my_fruits_4_1=['apple pizza','banana','orange pizza','grape pizza','peach']
for fruit in my_fruits_4_1:
    if 'pizza' in fruit:
        print(fruit)
print("I really love pizza!")

'''练习4.2'''
my_common_animals_4_2=["cocordile","lion","tiger","elephant","giraffe"]
comments_4_2=["The cocordile is a dangerous animal.",
              "The lion is the king of the jungle.",
              "The tiger is a fierce animal.",
              "The elephant is a large animal.",
              "The giraffe is a tall animal."]
for i in range(len(my_common_animals_4_2)):
    print(f"{my_common_animals_4_2[i]}"+":"+f"{comments_4_2[i]}",end="\n\n")
print("Any of these animals are interesting!")

'''练习4.3'''
number_list_4_3=list(range(1,21))
for i in number_list_4_3:
    print(i)
i=0
number_larger_list_4_3=list(range(1,1000001))
# for i in number_larger_list_4_3:
#     # print(i) 
print(f'the maximum num is {max(number_larger_list_4_3)}')
print(f'the minimum num is {min(number_larger_list_4_3)}')
print(f"All the numbers in the lis add up to {sum(number_larger_list_4_3)}")
    
'''练习4.4'''
my_number_list_4_4=list(range(1,20,2))
print(my_number_list_4_4)
for i in my_number_list_4_4:
    print(i)

'''练习4.5'''
my_number_list_4_5=list(range(3,31,3))
for i in my_number_list_4_5:
    print(i)


'''练习4.6'''
my_number_list_4_6=[x**3 for x in range(1,11)]  #用list（）也是可以的
for i in my_number_list_4_6:
    print(i)

'''练习4.7'''
print(f"The first three items in the list are:{my_number_list_4_6[0:3]}")
print(f"The last three items in the list are:{my_number_list_4_6[-3:]}")
print(f"Three items from the middle of the list are:{my_number_list_4_6[3:6]}")

'''练习4.8'''   
my_friends_pizzas_4_8=my_fruits_4_1[:]
my_fruits_4_1.append('pear')
my_friends_pizzas_4_8.append("gali pizza")
print(my_friends_pizzas_4_8)
print("\n",my_fruits_4_1)

'''练习4.9'''
my_foods_tuple=("laziji","hotpot","gongbaojiding","qiangchaobaicai","kaoyu")
for food in my_foods_tuple:
    print(food)
my_foods_tuple=("laziji","hotpot","gongbaojiding","qiangchaobaicai","kaoyu","zhajiangmian")
for food in my_foods_tuple:
    print(food)








