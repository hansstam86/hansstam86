from decimal import Decimal, getcontext

def pi(precision):
    getcontext().prec = precision
    pi = Decimal(0)
    maxK = precision + 2
    for k in range(maxK):
        term = Decimal(1)/(16**k) * (Decimal(4)/(8*k+1) - Decimal(2)/(8*k+4) - Decimal(1)/(8*k+5) - Decimal(1)/(8*k+6))
        pi += term
    return pi

def main():
    while True:
        try:
            precision = int(input("Enter the number of decimal places for pi: "))
            if precision < 0 or precision > 10**6:  # limit precision to a reasonable range
                raise ValueError("Number out of range. Please enter a number between 0 and 1,000,000.")
            break
        except ValueError as e:
            print(e)
    print(pi(precision))

if __name__ == '__main__':
    main()