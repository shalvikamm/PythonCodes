
#Name : Shalvika Mishra
#Date : October 02,2021
#Honor Statement:“I have not given or received any unauthorized assistance on this assignment.”
#Video Link : https://youtu.be/NPMwbZCmoVU



def getWelcome():
    
    '''This function greets the user and tells about the functionality of the code'''
    
    print("**************Welcome to the Happy/Sad and Prime/Non Prime Code******************")
    print("\n")
  

def UserInput():
    
    '''This function takes user input and converts the string into number'''
    num=int(input("Please enter positive integer : "))
    return num


def getSumDigits(num):
    
    '''This function finds the sum of digits of a number'''
    '''As the number is non iterable hence changing the number into str(num) to print sum of each digit'''
    
    sum=0
    for digit in str(num): 
        sum = sum + (int(digit)) ** 2     #Squaring digits of the number and accumulating in a sum 
    return sum


def Check_Happy_Number(num):
        '''Check if the number is happy''' 
        '''A number is said to be a happy number if sum of its digits are 1'''
        
        if num == 1:
            return True 
        
        storedlist=[num]   #storing the first number in a list       
        
        while num!=1 :
            
            num=getSumDigits(num) #finding sum if digits of number and replacing that sum with the number
            #print(num) #for checking and explaining code in video 
            
            if num in storedlist: # if number already exists in the storedList it is a sad number
                return False
            
            storedlist.append(num)
            #print (storedlist) #printing this just to explain the logic, when does my code stop,for checking and explaining code in video 
            
        return True

        
def Check_Prime_Number(num):  
    
    '''This function checks whether the given number is prime or not'''
    '''1 is not a prime number'''
    '''Number is prime if it has any other factor except 1 and itself'''
    
    if num ==1:    #1 is not a prime number
        return False 
    
    for i in range(2,num): # hence starting the check from 2 till the number 
        if num %i == 0:      #If number if divisible by any number except itself it is non prime
            return False 
        else :
            return True


def result(Happy_Number,Prime_Number):
    
    '''This function just take results of  function Check_Happy_Number and Check_Prime_Number and tells whether the number is happy/sad ,prime/nonprime'''
    
    if Happy_Number and Prime_Number:
            print("\n") 
            print("******************Happy Prime*****************")  
            print("\n")         
    
    elif Happy_Number and not Prime_Number:
           print("\n") 
           print ("**************Happy Non Prime****************")
           print("\n")
    
    elif Prime_Number and not Happy_Number  :
        print("\n") 
        print("******************Sad prime**********************")  
        print("\n")         
    
    else:
        print("\n") 
        print ('*****************Sad Non-prime******************')
        print("\n")
                

if __name__ == "__main__":

    '''Main function is calling the multiple functions written in the program'''
    
    while True :
        
        getWelcome() #Greeting User
        print("\n") 
        print ("Enter 1 to continue and 2 to exit") 
        choice=int(input()) #Taking user choice 
        if (choice ==1):
            n=UserInput()   #calling the getInput function
            a=Check_Happy_Number(n)   #Calling the function which checks whether number is Happy or Sad .
            b=Check_Prime_Number(n)   #Calling the function which checks whether number is Prime or Non Prime.
            result(a,b)
                  
        else:
           break