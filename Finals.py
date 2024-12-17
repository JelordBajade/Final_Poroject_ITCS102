def Act_1(y):
    print(f"Hello World")
def Act_2():
    name = input ("jelord")

    print ("Hi" + name )
def Act_3():
    name = input("Please input your name here ---> ")
    fname = input("Please input your fname here ---> ")
    mname = input("Please input your mname here ---> ")
    birthdate = input("Please input your birth date here ---> ")
    birthmonth = input("Please input your birthmonth here ---> ")
    birthyear = input("Please input your birthyear here ---> ")
    maritalstatus = input("Please input your maritalstatus here ---> ")
    religion = input("Please input your religion here ---> ")
    ethnicity = input("Please input your ethnicity here ---> ")
    mobile = input("Please input your mobile here ---> ")
    email = input("Please input your email here ---> ")
    gender = input("Please input your gender here ---> ")
    address = input("Please input your address here ---> ")
    age = input(" Please input your age here ---> ")


    print("\n\n\n\n\tHello, My name is,", name ,"I'm", age ,"yrs old.\n\tI identify as", gender ,"\n\tMy father's name is", fname ,"\n\tMy mother's name is", mname ,"\n\tMy Bithday is in", birthmonth , birthdate , birthyear ,"\n\tI live in", address,"\n\tI am", maritalstatus ,"\n\tI am", ethnicity ,"Citizen\n\tMy mobile number is:", mobile ,"\n\tYou may contact me in my email:", email ,"\n\tThank You!!!\n\n\n")

def Act_4():
    number1 = eval(input("please type number--->"))
    number2 = eval(input("please type number--->"))

    answer	= number1 + number2
    print ("the sum of", number1, "and" , number2, "is" ,answer)
def Act_5():
    x = 5

    print (x)

    x = x + 10

    print (x)

    x = x + 15

    print(x)

    x += 10

    print(x)
def Act_6():
    Fah = eval(input("enter temperature in Fahrenheit : "))
    celsius = (Fah - 32) * 5 / 9

    print (" the comversion of" , Fah , "degrees fahrenheit is" , celsius , "degrees celsius")

    print (F" the comversion of {Fah} degrees fahrenheit is {round(celsius,2)} degrees celsius")

def Act_7():
    gold = 0

    miner = input("Enter Name")

    hasmine = input("Did you mine gold today ?")

    if hasmine.lower() == "yes":
        gold +=1
        print (f"Hi {miner}, today you have a total of {gold} gold ")
    else: 
        print (f"Hi {miner}, today you have a total of {gold} gold ")
def Act_8():
    password = input("please enter your password : ")

    if password.lower() == " mahal ko pa sya ":
        print (" congrats ang rupok mo")
        print ("enjoy using the system")
    elif password == "mahal ko pa sya":
        print (" congrats ang rupok mo")
        print ("enjoy using the system")


    else:
        print ("bawal ang marupok")
    print ("thank you for using the system")

def Act_9():
    age = eval(input(" enter your age : "))
    if age>= 1 and age <= 7 :
        print ("toddler")
    elif age >= 8 and age <= 13:
        print (" pre teen")
    elif age >= 14 and age <= 18:
        print("Teenager")
    elif age <= 21:
        print("Early Adulthood")
    elif age <= 45:
        print("Mid Adulthood")
    elif age <= 59:
        print("Post Adult")
    elif age >= 60 and age <= 100:
        print("Senior")
    else:
        print("INVALID AGE")
def Act_10():
    isDLL= input('Are you a current student of DLL (yes/no):  ')

    if isDLL.lower() == 'yes':
        print('Welcome to the DLL BSIT Scholarship form')
        isCotta= input('Are you from Barangay Cotta (yes/ no):  ')

        if isCotta.lower() == 'yes':
            print('Please fillup the second form')
            isLevel=input('What is your current level right now in DLL\nF - Freshmen\nS - Sophomore\nJ - Junior\nR - Senior\nPlease input your answer')
            if isLevel.lower() == 'f':
                print('Hi Freshmen')
            elif isLevel.lower() == 's':
                print('Hi Sophomore')
            elif isLevel.lower() == 'j':
                print('Hi Junior')
            elif isLevel.lower() == 'r':
                print('Hi Senior')
            else:
                print('Invalid choice')
            isNeeded = input('Do you need this scholarship (yes/no):  ')
        
            if isNeeded.lower() == 'yes':
                print('Scholarship Granted')
            else:
                print('Thanks for stopping by')
        else:
            print('Sorry, this Scholarship grant are only for resident of Cotta')

    else:
        print('Thanks for stopping by')
def Act_11():
    for me in range (1 , 101):
        print(me, 'GOODBYE WORLD')
def Act_12():
    for cycle in range (10,0,-1):
        print(cycle)
def Act_13():
    sum = 1
    num=int(input('Enter a number: '))

    for x in range (num,0,-1):
        sum *= x
    print(f"The factorial of {num} is {sum}")
def Act_14():
    for x in range ( 0, 11,):
        print(x,end =" ")
    for y in range (0, 11):
        print("*",end = " ")
    print("")
def Act_15():
    for x in range ( 0, 11,):
        print(x,end =" ")
    for y in range (0, x):
        print("*",end = " ")
    print("")
def Act_16():
    for x in range (1,11,):
        for y in range (1, x + 1):
            print(" ",end=" ")
        for z in range(11, x, -1):
            print(" * ",end=" ")
        print()
def Act_17():
    col = eval(input("Enter number of columns---> "))


    for x in range (1, 11):
        for y in range (1, col + 1):
            print(f"{x} x {y} = {x*y}" ,end="\t")
        print()
def Act_18():
    tri = eval(input("Enter a number of triangle---> "))

    for x in range (1, 6):
        for r in range (1 , tri + 1):
            for y in range (1 , x + 1):
                print("*", end=" ")
            for z in range (6, x, -1):
                print(" ",end=" ")
        print()
def Act_19():
    tuloy = True
    while tuloy == True:
        name = input("Enter your name: ")
        if name.lower()== "stop":
            print("PROGRAM TERMINATED")
            break
            tuloy = False
        else:
            continue
def Act_20():
    import os

    isContinue = True
    no = 0
    while isContinue == True:
        ask = input("Would you like to add another triangle (yes / no )--> ")

        if ask.lower() == "no":
            print("PROGRAM TERMINATED")
            break
            isContinue = False
        else:
            os.system('cls')
            no += 1
            for x in range (1, 6):
                for r in range (1 , no + 1):
                    for y in range (1 , x + 1):
                        print("*", end=" ")
                    for z in range (6, x, -1):
                        print(" ",end=" ")
                print()
            continue
def Act_21():
    def pang_hi():
        print("HI IT1C")

    def pang_hi_v2(name):
        print(f"Hello {name}")

    def termi():
        print("PROGRAM TERMINATED")

    def activity_2():
        number1 = eval (input("enter a number--->" ))
        number2 = eval (input("enter another number--->" ))
        answer = (number1 + number2)
        print(f"The sum of {number1} and {number2} is {answer}")

    tuloy =  True
    while tuloy == True:
        ask = input("Enter a name---> ")

        if ask.lower() != "stop":
            pang_hi_v2(ask)
            if ask == "2":
                activity_2()
                continue
        else:
            termi()
            break

def Act_22():
    lup = True
    names = []


    while lup == True:
        askName = input("What name would you like to add?> ")
        if askName.lower() == "stop":
            print(names)
            print(f"You have entered {len(names)} names!")
            break
        else:
            names.append(askName)
def Act_23():
    def factorial(factor):
        """This function is for calculating the factorial of a numver that is provided, it will automatically compute the factorial of the provided number."""
        fact = 1
        for x in range(factor, 0, -1):
            fact *= x
            print(fact)
        return fact

    factorial(5)

    help(factorial)
def Act_24():
    # from actvity23 import factorial

    # print(f"the factorial of 7 is {factorial(7)} ")

    pass
def Act_25():
    fruits = ["apples", "banana", "orange"]

    fruits.append("strawberry")

    fruits.insert(1, "guyabano")

    fruitInsert = input("What fruit would you like to add?> ")

    fruits.append(fruitInsert)

    print(fruits)
def CC_1():
    print("\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t *\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\b* * *\n\t\t\t\t\t\t\t\t\t\t\t\t\b\t\t\t\b\b* * * * *\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    * * * * * * *\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b* * * * *\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\b* * *\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t *")
def CC_2():
    name = input("please enter your name ---->")

    print("\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t *\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\b* * *\n\t\t\t\t\t\t\t\t\t\t\t\t\b\t\t\t\b\b\b* * * * *\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b *|" + name + "|*\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b* * * * *\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\b* * *\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t *")
def CC_3():
    print("Dividing Numbers")
    num1 = eval(input("Enter the first number> "))
    num2 = eval(input("Enter the second number> "))


    answer = num1 / num2

    print(f"{num1} divided by {num2} = {answer}")
def CC_4():
    number1 = eval(input("Enter a number: "))

    number2 = eval(input("Enter a number: "))

    answer1 = number1 + number2

    answer2 = number1 - number2

    answer3 = number1 * number2

    answer4 = number1 / number2

    print("The sum of " , number1 , " and " , number2 , " is " , answer1)

    print("The difference of " , number1 , " and " , number2 , " is " , answer2)

    print("The product of " , number1 , " and " , number2 , " is " , answer3)

    print("The quotient of " , number1 , " and " , number2 , " is " , answer4)

def CC_5():
    print("\nWelcome to the Bank of Capistrano")

    name = input("\nPlease enter your name > ")

    print("\nHello," , name , "\b!\n")

    pera = eval(input("How much would you like to deposit? "))

    libo = pera // 1000
    libo2 = pera % 1000
    fiveh = libo2 // 500
    fiveh2 = libo2 % 500
    twoh = fiveh2 // 200
    twoh2 = fiveh2 % 200
    oneh = twoh2 // 100
    oneh2 = twoh2 % 100
    fifty = oneh2 // 50
    fifty2 = oneh2 % 50
    twenty = fifty2 // 20
    twenty2 = fifty2 % 20
    ten = twenty2 // 10
    ten2 = twenty2 % 10
    five = ten2 // 5
    five2 = ten2 % 5
    one = five2 // 1

    print("\n\t\t\tThe breakdown of your deposit is:")
    print("\t\t\t _______________________________")
    print("\t\t\t|\tValue\t |\tAmount\t|")
    print("\t\t\t|________________|______________|")
    print("\t\t\t|\t\t |\t\t|")
    print("\t\t\t|\t" , libo ,"\t | \t1,000\t|")
    print("\t\t\t|\t" , fiveh ,"\t | \t500\t|")
    print("\t\t\t|\t" , twoh ,"\t | \t200\t|")
    print("\t\t\t|\t" , oneh ,"\t | \t100\t|")
    print("\t\t\t|\t" , fifty ,"\t | \t50\t|")
    print("\t\t\t|\t" , twenty ,"\t | \t20\t|")
    print("\t\t\t|\t" , ten ,"\t | \t10\t|")
    print("\t\t\t|\t" , five ,"\t |\t5\t|")
    print("\t\t\t|\t" , one ,"\t |\t1\t|")
    print("\t\t\t|________________|______________|")

def CC_6():
        name = input("Enter your name: ")
        prelim = eval(input("Enter your Prelim grade: "))
        midterm = eval(input("Enter your Midterm grade: "))
        semifinal = eval(input("Enter your Semifinals grade: "))
        quiz = eval(input("Enter your quiz grade: "))
        finals = eval(input("Enter your Finals grade: "))
        project = eval(input("Enter your project grade: "))

        FG = (prelim * .15) + (midterm * .15) + (semifinal * .15) + (finals * .15) + (quiz * .15) + (project * .25)

        if FG > 100:
            print(f"Result:" , FG)
            print(f"your grade is too high {name}!")
        elif FG >= 75:
            print(f"Result:" , FG)
            print("congrats you passed")
        else:
            print("Result:" , FG)
            print("You failed, study more.")
def CC_7():
    A = input("DID YOU BUY A MEAT GOOD/s (yes/no)? ")
    if A.upper() == "YES":
        print('\nTHIS ARE THE LIST OF AVAILABLE MEAT GOODS')
        print('===========================================')
        print('Pork ------- 300php/kilo')
        print('Chicken ---- 250php/kilo')
        print('Beef ------- 400php/kilo')
        print('Rabbit ----- 250php/kilo')
        print('Tocino ----- 100php/kilo')
        print('Bacon ------ 120php/kilo')
        print('Bologna -----100php/kilo')
        quan1= eval(input("\nHow many kilos of Pork meat you want to buy? "))
        pork=quan1 * 300

        quan2= eval(input("\nHow many kilos of Chicken meat you want to buy? "))
        chicken=quan2 * 250

        quan3= eval(input("\nHow many kilos of Beef meat you want to buy? "))
        beef=quan3 * 400

        quan4= eval(input("\nHow many kilos of Rabbit meat you want to buy? "))
        rabbit=quan4 * 250

        quan5= eval(input("\nHow many kilos of Tocino meat you want to buy? "))
        tocino=quan5 * 100

        quan6= eval(input("\nHow many kilos of Bacon meat you want to buy? "))
        bacon=quan6 * 120

        quan7= eval(input("\nHow many kilos of Bologna meat you want to buy? "))
        bologna=quan7 * 100

        total= pork+chicken+beef+rabbit+tocino+bacon+bologna
        tax=(pork*0.123) or (chicken*0.123) or (beef*0.123) or (rabbit*0.123) or (tocino*0.123) or (bacon*0.123) or (bologna*0.123)
        total_and_tax= (total + tax)
        print()
        age = input("Are you a Senior Citizen(yes/no)? ")
        if age.lower() =='yes':
            disc=round(total*0.052)
            print(f"Hi, customer, you purhased a \n{quan1}kilo of Pork meat\n{quan2}kilo of Chicken meat\n{quan3}kilo of Beef meat\n{quan4}kilo of Rabbit meat\n{quan5}kilo of Tocino meat\n{quan6}kilo of Bacon meat\n{quan7}kilo of Bologna meat\nwith the total price of {total}php plus a 12.3% tax ({tax}php) and with a discount of 5.2% ({disc}php)")
        
        else:
            disc=0
            print(f"Hi, customer, you purhased a \n{quan1}kilo of Pork meat\n{quan2}kilo of Chicken meat\n{quan3}kilo of Beef meat\n{quan4}kilo of Rabbit meat\n{quan5}kilo of Tocino meat\n{quan6}kilo of Bacon meat\n{quan7}kilo of Bologna meat with the total price of {total}php plus a 12.3% tax(",tax,")")
        print()
        E = float(input("Amount Given: "))
        print()
        if E>= total_and_tax:
            change = round(E - total_and_tax + disc)
            print('=================RECEIPT===================')
            print('Qty.    Description           Amount')
            print(f'{quan1}x ----- PORK MEAT.........{pork}php')
            print(f'{quan2}x ----- CHICKEN MEAT......{chicken}php')
            print(f'{quan3}x ----- BEEF MEAT.........{beef}php ')
            print(f'{quan4}x ----- RABBIT MEAT.......{rabbit}php')
            print(f'{quan5}x ----- TOCINO MEAT.......{tocino}php')
            print(f'{quan6}x ----- BACON MEAT........{bacon}php')
            print(f'{quan7}x ----- BOLOGNA MEAT......{bologna}php')
            print()
            print(f'SUBTOTAL...................{total}php')
            print(f'TAX(12.3%).................{tax}php')
            print(f'TOTAL......................{total_and_tax}php')
            print(f'PAY AMOUNT.................{E}php')
            print(f'DISCOUNT(5.2%).............{disc}php') 
            print(f'CHANGE.....................{change}php')
            print()
            print("==THANK YOU COME AGAIN!!==")
        else:
            E< total_and_tax
            print("Insufficient Amount")
    else :
        print("Thankyou for stopping by!")
def CC_8():
    even = 0
    odd = 0
    sum = 0
    for x in range(1, 11):
        num = int(input(f"Enter {x} : "))
        sum += num 
        if num % 2 ==0 :
            odd += num 
        else :  
    
            even += num

    print(f"the sum of all number given is {sum}")
    print (f" the given number is {odd}")
    print(f"the given number is {even}")
def CC_9():
    for x in range(1,11) :
        for y in range(1, x + 1):
            print (" ", end = " ")
        for z in range (11, x, -1):
            print("*",end=" ")
        print()
def CC_10():
    for x in range(11,0,-1) :
        for y in range(1, x + 1):
            print (" ", end = " ")
        for z in range (11, x, -1):
            print("*",end=" ")
        for d in range (11, x, -1):
            print("*",end=" ")
        print()


    for x in range(1,11) :
        for y in range(1, x + 1):
            print (" ", end = " ")
        for z in range (11, x, -1):
            print("*",end=" ")
        for d in range (11, x, -1):
            print("*",end=" ")
        print()


def CC_11():
    for x in range(6,0, -1) :
        for y in range(1, x + 1):
            print (" ", end = " ")
        for z in range (7, x, -1):
            print("*",end=" ")
        for d in range (6, x, -1):
            print("*",end=" ")
        print()


    for x in range(0,7) : 
        for y in range(1, x +1):
            print (" ", end = " ")
        for z in range (7, x, -1):
            print("*",end= " ")
        for d in range (6, x, -1):
            print("*",end =" ")
        print()
def CC_12():
    for x in range (1,5):
        for y in range (5,x,-1):
            print( " ", end = " ")
        for z  in range (1, x + 1):
            print("*", end = " ")
        for w in range (1, x + 1):
            print("*", end = " ")
        print()

    for x in range (0,4):
        for y in range (4,0,-1):
            print( " ", end = " ")
        for z  in range (2,4):
            print("*", end = " ")
        for w in range (4,0,-1):
            print(" ", end = " ")
        print()
def CC_13():
    for x in range(1,7):
        for y in range(6,x,-1):
            print(" ", end = " ")
        for z in range (x, 1, -1):
            print(y, end = " ")
        for a in range (1,x + 1):
            print(a, end = " ")
        print()

    for x in range(5,0,-1):
        for y in range(6,x,-1):
            print(" ", end = " ")
        for z in range (x,1,-1):
            print(y, end = " ")
        for a in range (1,x + 1):
            print(a, end = " ")
        print()
def CC_14():
    tuloy = True
    a = 0
    while tuloy == True:
        number = eval(input("Enter a number--->  "))
        if number == 0:
            print("Program Terminated")
            print(f"The total of the number you enter is {a}")
            break

        else:
            a += number
            continue
def CC_15():
    import os

    isContinue = True
    no = 0
    while isContinue == True:
        ask = input("Would you like to add another triangle (yes / no )--> ")

        if ask.lower() == "no":
            print("PROGRAM TERMINATED")
            break
            isContinue = False
        elif ask.lower() == "yes":
            os.system('cls')
            no += 1
            for x in range (1, 6):
                for r in range (1 , no + 1):
                    for y in range (1 , x + 1):
                        print("*", end=" ")
                    for z in range (6, x, -1):
                        print(" ",end=" ")
                print()
        else:
            print("INVALID ANSWER it's only (yes/no)")
            continue
def CC_16():
    def denomination(amount):
        print("\nDenomination Breakdown:")
        a = amount // 1000
        b = amount % 1000

        c = b // 500
        d = b % 500

        e = d // 200
        f = d % 200

        g = f // 100
        h = f % 100

        i = h // 50
        j = h % 50

        k = j // 20
        l = j % 20

        m = l // 10
        n = l % 10

        o = n // 5
        p = n % 5

        q = p // 1

        print("1000---", a)
        print("500----", c)
        print("200----", e)
        print("100----", g)
        print("50-----", i)
        print("20-----", k)
        print("10-----", m)
        print("5------", o)
        print("1------", q)


    accounts = {}

    def create_account():
        u = input("Enter a username: ")
        if u in accounts:
            print("Account already exists!")
        else:
            accounts[u] = 0
            print(f"Account created successfully for {u}.")


    def deposit():
        u = input("Enter your username: ")
        if u in accounts:
            try:
                amt = int(input("Enter amount to deposit: "))
                if amt > 0:
                    accounts[u] += amt
                    print(f"Deposited {amt} successfully. New balance: {accounts[u]}")
                    denomination(amt)
                else:
                    print("Amount must be positive!")
            except ValueError:
                print("Invalid input! Please enter a whole number.")
        else:
            print("Account not found!")


    def withdrawal():
        u = input("Enter your username: ")
        if u in accounts:
            try:
                amt = int(input("Enter amount to withdraw (whole numbers only): "))
                if 0 < amt <= accounts[u]:
                    accounts[u] -= amt
                    print(f"Withdrawn {amt} successfully. Remaining balance: {accounts[u]}")
                    denomination(amt)
                else:
                    print("Insufficient funds or invalid amount!")
            except ValueError:
                print("Invalid input! Please enter a whole number.")
        else:
            print("Account not found!")


    def check_balance():
        u = input("Enter your username: ")
        if u in accounts:
            print(f"Your balance: {accounts[u]}")
        else:
            print("Account not found!")


    def options():
        while True:
            print("\nBanking System")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Check Balance")
            print("5. Exit")
            choice = input("Choose an option (1-5): ")

            if choice == '1':
                create_account()
            elif choice == '2':
                deposit()
            elif choice == '3':
                withdrawal()
            elif choice == '4':
                check_balance()
            elif choice == '5':
                print("Thank you for using the Banking System!")
            break
        else:
            print("Invalid option. Please try again.")

    options()

def menu():
    tuloy = True
    while tuloy == True:
        print("\n\t\t\t\t\t_______________________________________________________\n")
        print("\t\t\t\t\t\t\tWelcome to my program! ")
        print("\n\t\t\t\t\t_______________________________________________________\n")
        print("\n\t\t\t\t\t_______________________| Activities |__________________\n")
        print("\t\t\t\t\t|| 1 - Act 1                       14 - Act 14 ||")
        print("\t\t\t\t\t|| 2 - Act 2                       15 - Act 15 ||")
        print("\t\t\t\t\t|| 3 - Act 3                       16 - Act 16 ||")
        print("\t\t\t\t\t|| 4 - Act 4                       17 - Act 17 ||")
        print("\t\t\t\t\t|| 5 - Act 5                       18 - Act 18 ||")
        print("\t\t\t\t\t|| 6 - Act 6                       19 - Act 19 ||")
        print("\t\t\t\t\t|| 7 - Act 7                       20 - Act 20 ||")
        print("\t\t\t\t\t|| 8 - Act 8                       21 - Act 21 ||")
        print("\t\t\t\t\t|| 9 - Act 9                       22 - Act 22 ||")
        print("\t\t\t\t\t|| 10 - Act 10                     23 - Act 23 ||")
        print("\t\t\t\t\t|| 11 - Act 11                     24 - Act 24 ||")
        print("\t\t\t\t\t|| 12 - Act 12                     25 - Act 25 ||")
        print("\n\t\t\t\t\t___________________________________________________________\n\n")


        print("\n\t\t\t\t\t_____________________| Code Challenges |_____________________\n")
        print("\t\t\t\t\t|| CC_1 - Code Challenge 1               CC_9 - Code Challenge 9   ||")
        print("\t\t\t\t\t|| CC_2 - Code Challenge 2               CC_10 - Code Challenge 10 ||")
        print("\t\t\t\t\t|| CC_3 - Code Challenge 3               CC_11 - Code Challenge 11 ||")
        print("\t\t\t\t\t|| CC_4 - Code Challenge 4               CC_12 - Code Challenge 12 ||")
        print("\t\t\t\t\t|| CC_5 - Code Challenge 5               CC_13 - Code Challenge 13 ||")
        print("\t\t\t\t\t|| CC_6 - Code Challenge 6               CC_14 - Code Challenge 14 ||")
        print("\t\t\t\t\t|| CC_7 - Code Challenge 7               CC_15 - Code Challenge 15 ||")
        print("\t\t\t\t\t|| CC_8 - Code Challenge 8               CC_16 - Code Challenge 16 ||")
        print("\n\n\t\t\t\t\t\t\t\t\t\t\t0 - Exit")
        print("\n\t\t\t\t\t___________________________________________________________\n\n")

        bro = input ("Enter a number:")
        if bro == "Exit" or bro == "0":
            break
        elif bro != "Exit":
            if bro == "1":
                y = input("Enter your name here:")
                Act_1 (y)
                continue
            elif bro == "2":
                Act_2()
                continue
            elif bro == "3":
                Act_3()
                continue
            elif bro == "4":
                Act_4()
                continue
            elif bro == "5":
                Act_5()
                continue
            elif bro == "6":
                Act_6()
                continue
            elif bro == "7":
                Act_7()
                continue
            elif bro == "8":
                Act_8()
                continue
            elif bro == "9":
                Act_9()
                continue
            elif bro == "10":
                Act_10()
                continue
            elif bro == "11":
                Act_11()
                continue
            elif bro == "12":
                Act_12()
                continue
            elif bro == "13":
                Act_13()
                continue
            elif bro == "14":
                Act_14()
                continue
            elif bro == "15":
                Act_15()
                continue
            elif bro == "16":
                Act_16()
                continue
            elif bro == "17":
                Act_17()
                continue
            elif bro == "18":
                Act_18()
                continue
            elif bro == "19":
                Act_19()
                continue
            elif bro == "20":
                Act_20()
                continue
            elif bro == "21":
                Act_21()
                continue
            elif bro == "22":
                Act_22()
                continue
            elif bro == "23":
                Act_23()
                continue
            elif bro == "24":
                Act_24()
                continue
            elif bro == "25":
                Act_25()
                continue
            elif bro == "CC_1":
                CC_1()
                continue
            elif bro == "CC_2":
                CC_2()
                continue
            elif bro == "CC_3":
                CC_3()
                continue
            elif bro == "CC_4":
                CC_4()
                continue
            elif bro == "CC_5":
                CC_5()
                continue
            elif bro == "CC_6":
                CC_6()
                continue
            elif bro == "CC_7":
                CC_7()
                continue
            elif bro == "CC_8":
                CC_8()
                continue
            elif bro == "CC_9":
                CC_9()
                continue
            elif bro == "CC_10":
                CC_10()
                continue
            elif bro == "CC_11":
                CC_11()
                continue
            elif bro == "CC_12":
                CC_12()
                continue
            elif bro == "CC_13":
                CC_13()
                continue
            elif bro == "CC_14":
                CC_14()
                continue
            elif bro == "CC_15":
                CC_15()
                continue
            elif bro == "CC_16":
                CC_16()
                continue

menu ()