import random
a = int(input("Please enter the range of the number:"))
right_number = random.randint(1, a)
guess_number = random.randint(1, a)
count = 0   
success_num = 0
Expected_value = 0
Expected_individual_value = 0
while success_num <= 1000000000:
   
    while guess_number != right_number:
        
        count += 1
        guess_number = random.randint(1, a)
        print("The guess number is:", guess_number)
        print("The right number is:", right_number)
    if guess_number == right_number:
        success_num += 1
        count += 1
        if count == 0:
            continue
        guess_number = random.randint(1, a)
Expected_individual_value = success_num / count
print("The expected individual value is:", Expected_individual_value)
        

     
