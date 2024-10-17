#开始之前先看看这个
'''.append() .extend() .insert() .remove() .pop() .clear() .index() .count() .sort() .reverse()'''




'''练习3.1'''
#3-1 姓名：将一些朋友的姓名存储在一个列表中，并将其命名为names。依次访问该列表中的每个元素，从而将每个朋友的姓名都打印出来。
nameslist_3_1=["wangzhanyi","liuhaoyi","duanlianheng","jiangjie","wangyi",]
for i in range(5):
    print(nameslist_3_1[i],end="\t")    
i=0# 重置i的值

'''练习3.2'''
#3-2 问候语：继续使用练习3.1中的列表，但不打印每个朋友的姓名，而为每人打印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
for i in range(5):
    greetings_message_3_2=f"hello {nameslist_3_1[i]},how is it going?"
    print(greetings_message_3_2,end="\n")
i=0# 重置i的值

'''练习3.3'''
#3-3 自己的列表：想想你喜欢的通勤方式，如骑摩托车或者开汽车，并创建一个包含多种通勤方式的列表。根据该列表打印一系列有关这些通勤方式的宣言。
my_favourite_commute=["motorcycle","car","bicycle","bus","subway","plane","train"]
for i in range(7):
    commute_message_3_3=f"I would like to own a {my_favourite_commute[i]}."
    print(commute_message_3_3,end="\n")
i=0# 重置i的值
print(f"{my_favourite_commute[0:5:2]}")#打印列表中的第1、3、5个元素

'''练习3.4'''
#3-4 嘉宾名单：如果你可以邀请任何人一起共进晚餐，你会邀请哪些人？请创建一个列表，其中包含至少3个你想邀请的人；然后使用这个列表打印消息，邀请这些人来与你共进晚餐。
guests_3_4_1=["wangzhanyi","liuhaoyi","duanlianheng","jiangjie","wangyi",]
wondering_guest_1,wondering_guest_2,wondering_guest_3=guests_3_4_1.pop(2),guests_3_4_1.pop(2),guests_3_4_1.pop(2)
#注意是动态删除，所以每次删除一个元素后，后面的元素的索引会自动前移，这里是2，2，2，而不是2，3，4，所以慎用用for循环，否则会漏删
#所以用pop()方法删除元素时，要注意索引的变化，要小心，这里的pop中是索引，不是元素。
#wondering_guest_1,wondering_guest_2,wondering_guest_3=guests_3_4_1.pop(2),guests_3_4_1.pop(3),guests_3_4_1.pop(4)这样是错误的，因为pop()中的索引是动态的，所以要小心。

'''练习3.5'''          
# 删除列表中的某一特定元素 
'''方法一'''
x_1=[1,12,34,5,6,1,2,2,1,3,4,1,5,5,1]                         
for item_x_1 in x_1:
    if item_x_1==1:
        x_1.remove(item_x_1)
print(x_1)
#方法一的问题是，删除了第一个1之后，之后的元素索引自动前移，所以可能会漏删，比如删除了第一个1之后，第二个1的索引变成了第一个1的索引，所以第二个1就不会被删除。会有漏网之鱼
'''方法一的输出结果是[12, 34, 5, 6, 2, 2, 3, 4, 5, 5]'''
'''方法一注释所描述的特殊情况如下'''

x_1_0=["打游戏","打游戏""打游戏","打游戏","吃饭","睡觉","你好","上课","看电视","打游戏""打游戏","打游戏""打游戏"]
for item_x_1_0 in x_1_0:
    if item_x_1_0=="打游戏"or item_x_1_0=="打游戏""打游戏":
        x_1_0.remove(item_x_1_0)
print(x_1_0)

'''方法一的输出结果是['打游戏', '打游戏', '吃饭', '睡觉', '你好', '上课', '看电视', '打游戏""打游戏']'''#因此，要连续删除时，用方法一会有问题，要千万小心。


#方法二，复制一个列表，然后删除复制的列表中的元素，这样就不会漏删了
x=[1,2,34,5,6,1,2,2,1,3,4,1,5,5,1]
y=x.copy()
for i in range (len(y)):
    if y[i]==1:
        x.remove(y[i])
print(x)
#方法二避开了方法一的问题，因为y是x的复制，所以y的索引不会随着x的索引的变化而变化，所以不会漏删。有普适性
'''方法二的输出结果是[12, 34, 5, 6, 2, 2, 3, 4, 5, 5]'''

'''用方法二来处理方法一中的特殊情况'''
x_0_2=["打游戏","打游戏""打游戏","打游戏","吃饭","睡觉","你好","上课","看电视","打游戏""打游戏","打游戏""打游戏"]
y_0_2=x_0_2.copy()
for item_y_0_2 in y_0_2:             #这里也可以用for i in range(len(y_0_2)):来代替
    if item_y_0_2=="打游戏"or item_y_0_2=="打游戏""打游戏":
        x_0_2.remove(item_y_0_2)
print(x_0_2)
'''方法二的输出结果是['吃饭', '睡觉', '你好', '上课', '看电视']'''#因此，方法二是有普适性的


'''练习3.6,课堂练习'''
#求列表中的最大值与最小值
class_list_3_6=[1,4,8,2,10,3]

max_class_list_3_6=class_list_3_6[1]
for i in range(len(class_list_3_6)):
    if class_list_3_6[i]>max_class_list_3_6:
        max_class_list_3_6=class_list_3_6[i]
    else:
        continue
print(max_class_list_3_6)

'''练习3.7，课堂练习'''
#分别用for与while循环来求2-10所有整数的平方和
'''for循环'''
figure_3_7=0
for number_3_7 in range(2,11):
    square_3_7=number_3_7**2
    figure_3_7+=square_3_7
print(figure_3_7)
'''while循环'''
figure_3_7_0=0
number_3_7_0=2
while 2<=number_3_7_0<=10:
    square_3_7_0=number_3_7_0**2
    figure_3_7_0+=square_3_7_0
    number_3_7_0+=1
print(figure_3_7_0)