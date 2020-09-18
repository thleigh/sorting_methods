def is_prime(n):
    if n > 2:
        for i in range(2, n):
            if n % i == 0: 
                print("is not a prime")
                return False
            else:
                print("is a prime")
                return True
    else:
        print("Is not a prime")
        return False

is_prime(int(input("Enter a number: ")))