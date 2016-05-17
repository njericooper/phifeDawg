##------------------------------------------------------------------
## Name: 
## Date: 2/17/16
## Description: Problem 30 page 163
##-------------------------------------------------------------------
first = input("Enter first name: ")
last = input("Enter last name: ")
salary = int (input("Enter current salary: "))
name = first + last

if salary < 40000 :
    newSalary = (salary*.05) + salary
print("New salary for ", first, last, ": ", newSalary)    

if salary > 40000:
    newSalary = ((salary*.02) + salary + 2000)
    print("New salary for", name,": ", newSalary)

##-------------------------------------------------------------------
## Define main
def main():
          
##-------------------------------------------------------------------          
## Define getFirstName
def getFirstName() :
          first = input("Enter first name: ")
          return first
          
##-------------------------------------------------------------------
## Define getLastName          
def getLastName() :
         last = input("Enter last name: ")
         return last

##-------------------------------------------------------------------          
## Define getCurrentSalary
def getCurrentSalary() :
         currentSalary = input("Enter current salary: ")
         return currentSalary

##-------------------------------------------------------------------          
## Define calculateNewSalary
def calculateNewSalary() :
          if salary < 40000:
    newSalary = (salary*.05) + salary
print("New salary for ", first, last, ": ", newSalary)    

else:
    newSalary = (salary*.02) + salary + 2000)
    print("New salary for", name,": ", newSalary)
    return result 
          
##-------------------------------------------------------------------
## Define display result
def displayResult() :
          print(result)
             
##-------------------------------------------------------------------
## Define call main

main()          
          
