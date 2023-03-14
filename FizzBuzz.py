# solving famous problem fizzbuzz with if else
def FizzBuzz(n):
    result = []
    if n <= 0:
        print("Number is not valid!")
    else:    
        for i in range(1,n+1):
            if (i % 3 == 0):
                result.append("Fizz")
            elif (i % 5 == 0):
                result.append("Buzz")
            elif (i % 3 == 0 and i % 5 == 0):
                result.append("FizzBuzz")
            else:
                result.append(str(i))
    return result

      

if __name__ == "__main__":
    n1 = int(input("Enter the number:\n"))
    print(FizzBuzz(n1))
 