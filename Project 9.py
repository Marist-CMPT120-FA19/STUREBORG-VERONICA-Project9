#Veronica Stureborg
#Project 9


def sieve(n):
    ceiling= n+1
    primenumbers= dict()

    for i in range (2, ceiling): primenumbers [i] = True

    for i in primenumbers:
        factors = range(i, ceiling, i)
        for f in factors[1:]:
            primenumbers[f]= False
    return [i for i in primenumbers if primenumbers[i] == True]


def main():
    print("The output of this program is the prime numbers up to number n")
    n=int(input("Enter a number greater than two: "))
    print(sieve(n))

main()
