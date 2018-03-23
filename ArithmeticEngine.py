# cmpt120 - Lab #6
# Matthew Lanci
# 3/19/18
###
def showIntro():
       print("Welcome to the Arithmetic Engine!")
       print("=================================\n")
       print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'")
       
  
def doLoop():
    while True:
       cmd = input("What do you want to perform? ").lower()
       if cmd == 'quit':
              break             
       try:              
              num1 = int(input("Enter the first number: "))
              num2 = int(input("Enter the second number: "))
              if cmd == 'div':
                     num1 // num2
       except ValueError:
              print("Use only numbers")
              continue
       except:
              print("Cannot divide by zero")
              continue
       if cmd == "add":
            result = num1 + num2
       elif cmd == "sub":
            result = num1 - num2
       elif cmd == "mult":
            result = num1 * num2
       elif cmd == "div":
           result = num1 // num2
       print("The result is " + str(result) + ".\n")

def showOutro():
       print("\nThanks for using the Arithmetic Engine...")
       print("\nCome Back Soon")

def main():
       showIntro()
       doLoop()
       showOutro()
main()
        
    
    

