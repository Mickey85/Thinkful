
n=int(input("Enter the fizzbuzz counting upto n"))

try:
    i=1
    for i in range(1,n+1):

        if((i%3 == 0) and ( i%5 ==0)):
            print("FizzBuzz")
        elif(i%3 == 0):
            print("Fizz")
        elif(i%5 == 0):
            print("Buzz")
        else:
            print(i)


        i=i+1
except ValueError:
    print("Enter the numeric value")
