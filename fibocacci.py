def main():
    print("This program calculates the nth Fibocacci value.")
    print()

    n = int(input("Enter the Value of n: ")) # JA
    curr, prev = 1, 1 # JA: You have to initialize both
    for i in range(n - 2): # JA
        curr, prev = curr+prev, curr

    print()
    print("The nth Fibocacci number is", curr)

main()
    


    
    


    
