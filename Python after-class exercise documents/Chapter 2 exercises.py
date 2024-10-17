'''练习2.3'''
#2-3 个性化消息：将用户的姓名存到一个变量中，并向该用户显示一条消息。显示的消息应非常简单，如“Hello Eric, would you like to learn some Python today?”。
username_2_3="Eric"
print(f"hello {username_2_3}, would you like to learn some Python today?")

'''练习2.4'''
#2-4 调整名字的大小写：将一个人名存储到一个变量中，再以小写、大写和首字母大写的方式显示这个人名。
username_2_4="Wzhanyi"
username_2_3_using_1=username_2_4.lower()
username_2_4_using_2=username_2_4.upper()
username_2_4_using_3=username_2_4.title()
print(username_2_3_using_1,username_2_4_using_2,username_2_4_using_3)

'''练习2.5'''
#2-5 名言：找一句名言，将这个名言存储到一个变量中，然后以“名言作者的名字”加上名言的方式显示。
liberty_2_5="Albert Einstein"
message_2_5="A person who never made a mistake never tried anything new."
print(f"{liberty_2_5} once said,\"{message_2_5}\"")

'''练习2.6'''
#2-6 名言2：重复练习2-5，但将名人的姓名存储在变量famous_person 中，再创建消息，并将其存储在变量message 中，然后打印这条消息。
famous_name_2_6="Albert Einstein"
# message_2_6=f"{famous_name_2_6} once said,\"A person who never made a mistake never tried anything new.\""    #用f-string的方式，一般就会打出空格，就不会出现连在一起的情况。
message_2_6=famous_name_2_6+" once said,\"A person who never made a mistake never tried anything new.\""        #加法是直接拼在一起， once前面要有一个空格，否则会连在一起 ，就会变成Albert Einsteinonce said
print(message_2_6)

'''练习2.7'''
#2-7 剔除人名中的空白：存储一个人名，并在其开头和末尾都包含一些空白字符。务必至少使用字符组合"\t" 和"\n" 各一次。打印这个人名，以显示其开头和末尾的空白。然后分别使用剔除函数lstrip() 、rstrip() 和strip() ，并将结果打印出来。   
name_2_7="   \n\tAlbert Einstein\n\n\t"
print(name_2_7)
print(name_2_7.lstrip())            #name_2_7.lstrip()是去掉左边的空格，但是name_2_7中间的空格是不能去掉的
print(name_2_7.rstrip())            #name_2_7.rstrip()是去掉右边的空格，但是name_2_7中间的空格是不能去掉的
print(name_2_7.strip())             #name_2_7.strip()是去掉两边的空格，但是name_2_7中间的空格是不能去掉的
print(name_2_7.lstrip().rstrip())   #name_2_7.lstrip().rstrip()和name_2_7.strip()是一样的

'''练习2.8'''
#2-8 删除后缀：存储名字，并将其存储在一个变量中。使用方法 .removesuffix() 来删除这个人名中的后缀，并打印删除后缀的结果。
filename='python_notes.txt'
print(f"filename is :{filename.removesuffix(".txt")}")

'''练习2.9'''
#2-9 数字8：编写4个表达式，它们分别使用加法、减法、乘法和除法运算，但结果都是数字8。为使用print 语句来显示结果，务必将这些表达式用括号括起来，以显示你没有忘记运算顺序。
a=int(16/2)
b=4+4
c=10-2
d=int(2*4.0)
print("\t", a, "\t", b, "\t", c, "\t", d)

'''练习2.10'''
#2-10 最喜欢的数字：将你最喜欢的数字存储在一个变量中，再使用这个变量创建一条消息，指出你最喜欢的数字，然后将这条消息打印出来。
favorite_number_2_10=7
message_2_10=f"My favorite number is {favorite_number_2_10}."
print(message_2_10)

'''练习2.11'''
#2-11 添加注释：选择你编写的两个程序，在每个程序中都至少添加一条注释。如果程序太简单，实在没有什么需要说明的，就在程序文件开头加上你的姓名和当前日期，并对程序做简短的描述。
'''this is my simple program.today is 2024.10.16.
my name is wangzhanyi.
my roommate wangyuxi is playing games who noisy me when i programmed.'''

'''练习2.12'''  
#2-12 Python之禅：在Python终端会话中执行命令import this，并粗略地浏览一下其他的指导原则。
import this


'''That is all for chapter 2 exercises.'''

