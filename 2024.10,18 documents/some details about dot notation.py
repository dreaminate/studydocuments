'''
EXTEND()方法
'''
list1=[1,2,3,4,5,6,7,8,9,10]
list2=[]
list2.extend(11)                 #extend()中，参数必须是可迭代对象,且必须是一个，如【】''（）{}等
print(list2)
'''会报错 因为extend()方法只接受一个可迭代对象作为参数  而11是一个整数  不是可迭代对象。
   如果想要将11添加到list1 可以使用append()方法
   但是extend，可以迭代string，list，tuple，dict，set等等'''


'''
APPEND()方法
'''



