def calculater():
    print("Standard Calculater")
    try:
        while True:
            op = input("Enter the operater [+, -, /, *, ** and exit ]")
            if op.lower().strip()=="exit":
                break
            list_op =['+','-','/','*','**' and exit]
            if op not in list_op:
                print("piease enter the correct operation")
                continue
            numbers = []
            while True:
                number= input("please Enter the number or = sign to")
                if number == "=":
                    if len(numbers)<2:
                        print("please enter at least 2 number")
                        continue
                    break
                try:
                    num = float(number)
                    numbers.append(num)
                except ValueError:
                    print("please enter only number")
                    continue
            """ performing different arthimatic operations 
            after perfoming arthimatic
            operation we have to store the result on some Variable"""
            if op == "+":
                result = numbers[0]
                for number in numbers[1:]:
                    result = result + number
                print(" + ".join(map(str, numbers)) + f" = {result}")
            elif op == "-":
                result = numbers[0]
                for number in numbers[1:]:
                    result = result - number
                print(" - ".join(map(str, numbers)) + f" = {result}")
            elif op == "*":
                result = numbers[0]
                for number in numbers[1:]:
                    result = result * number
                print(" *".join(map(str, numbers)) + f" = {result}")   
            elif op == "/":
                result = numbers[0]
                for number in numbers[1:]:
                    try:
                        if number ==0:
                            raise ZeroDivisionError()
                        result = result / number
                    except ZeroDivisionError:
                        print("denominater can not be zero")
                        continue
                print(" *".join(map(str, numbers)) + f" = {result}") 
            elif op == "**":
                result = numbers[0]
                for number in numbers[1:]:
                    result = result * number
                print("**".join(map(str, numbers)) + f" = {result}")   

    except Exception as e:
            print(f"Operation Failed! {e}")
    print("Developed By:Abel K")    
calculater() 