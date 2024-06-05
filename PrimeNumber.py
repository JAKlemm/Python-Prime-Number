def prime(number):
    answer = True
    if(number == 1):
        answer = False
    else:
        for x in range(2, number):
            if number % x == 0:
                answer = False
                break
    if(answer):
        print(number," is a prime number")
    else:
        print(number, " is not a prime number")


def main():
    n = int(input("Enter an integer: "))
    list = []
    for x in range(2 ,n + 1):
        list.append(x)
    for x in list:
        prime(x)

main()