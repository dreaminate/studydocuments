
import gmpy2
yinzi=[]
count_1=0

guess_number=pow(int(input("请输入一个数字：")),int(input("幂："))) 
sqrt_number = gmpy2.isqrt(guess_number)
for i in range(2,guess_number):
        if guess_number%i==0:
            count_1+=1
            if count_1>=1:
                yinzi.append(i)
                
                
            for i in yinzi:
                if gmpy2.is_prime(i) is False:
                    yinzi.remove(i)
                    count_1-=1
                    print(f"不是素数，有{count_1}个prime因子，分别是{yinzi}")      
                    