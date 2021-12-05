#Name: Shalvika Mishra 
#Date: 09/27/2021
#Video Link:https://youtu.be/7YWh8x3RUYE
#Honor Statement: “I have not given or received any unauthorized assistance on this assignment.”
import os.path
from os import path

datalist = []


def printintro():

    '''This function Greets the user and breify explains about the program'''

    print ("\n******************Welcome  User!************************\n")
    print("\t*******Hello to the stem-leaf plot design**********\t")
    print ("\tThe user would be given an option to choose a file for which he wishes to display stem leaf plot\t")


def readfile(file):
    '''This function reads the file and passes the list to the graph function'''
    datalist.clear()                      #Clearing datalist
    print ("\n*****************\n")
    print("Reading file", file) 
    infile = open(file, "r")
    lineList = infile.readlines()
    for i in range ( 0, len(lineList) ): 
            x = int(lineList[i].strip())
            datalist.append(x)
   
    #print(datalist)
    maxelement=max(datalist) 
    index=maxelement //10   
    #print(index)            #Determining till what range user needs to print stem values
    datalist.clear()                      #Clearing datalist 
    infile = open(file , "r").readlines() #Reading each value of text file and converting it in a list
  
    for i in range(index+1):              
        datalist.append([])               #Creating empty list so that later we can add stems and leafs to it
    
   
    #Appending leaves to the respective stems
    for i in infile:
          filevalue = int(i)
          datalist[filevalue//10].append(filevalue%10)    #Adding stem and leafs in the datalist


def  stemleafgraph():
    '''This function displays the stem and leaf plot'''

    print ("\n*****************\n")
    print("Stem and leaf plot\n")

    if len(datalist) ==0:      #if the datalist is empty then print message no data to display
        print("There is no data to display")
        return
      
    for stem in range(len(datalist)): # Printing the stem-and-leaf plot
                print(stem,end="\t")
                print("|",end="\t")
                datalist[stem].sort()             #Sorting the stem
                for leaf in datalist[stem]:          #Printing Leaf
                   print(leaf,end=" ")              #Print leafs along with space between the leafs 
                print()                             #Leave Blank Line in the output

def userinput():

    '''This function takes user input and accordingly performs the choice of task user has selected'''

    while True :
       
        print("\n**********************User Choices *******************")
        print ("\n")
        print("**Enter 1 if user wants to read files** \n**Enter 2 if user wishes to display stem and leaf plot **\n**Enter 3 if user wishes to exit**")
        
        choice=int(input("Enter your choice \t"))
        
        if choice == 1:
            Filename = input("Enter file name:\t")  #User need to input the filename for which he wants to display stem and leaf plot
            readfile(Filename)        #calling readfilefunction

        if choice ==2 :
            stemleafgraph()             #calling stemleaffunction

        if choice ==3:
            print("\nThanks for sparing time for this code, GoodBye!\n")
            quit()


if __name__ == "__main__":

    '''The main function is executed first in any code.Hence the main function calls the print intro and userinput function'''

    printintro()     #Calling the print/greet user function
    userinput()      #Calling the user input function
    
          
        