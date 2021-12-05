#Python Programming : DSC 430
#Name : Shalvika Mishra
#Date : September 19, 2021
#Honor Statement :  “I have not given or received any unauthorized assistance on this assignment.”
#Video Link: https://youtu.be/QuLmpgDHiLc

print ("*********************************Checking if two numbers are coprime**********************")
print("\n")

def coprime(a,b):
        
    '''This function checks whether the greatest common divisor (GCD)of the two numbers is 1 if the GCD is 1 the two given numbers are coprime.'''
    '''This function is a recursive function'''
            
    if b ==0 :
                if(a==1):
                    
                    print ("**************The given numbers are co prime ****************")
                    return True
                
                else :
                    
                    
                    print ("************************The given numbers are not co prime ****************************************")
                    return False 

    else :

                   return coprime(b, a%b) # Using Euclid's algorithm logic
        
def coprime_test_loop():
    
        '''This function takes user input and calls the coprime function'''
        
        #num 1 and num 2 have local scope 
        #namespace
         
        num1=int(input("\t Enter the first number \t")) #naming numbers as num1 and num2 
        num2=int(input("\t Enter the second number \t"))
        return coprime(num1,num2) 

    
while True :       #Using while loop so that the user can enter choices until he wishes to exit
 
    print(coprime_test_loop()) #calling the coprime_test_loop function
    print ("\n")
    choice=input ("If user wishes to leave program type exit else continue \t" )  #asking for user's choice to continue or exit
    if choice == 'exit':
        break      
    else :
       continue
        