"""1. A list with the sum of all elements in that list."""
def sum_of_list(l):
   """This function takes a list as parameter and prints the sum of items present in the list."""
   sum=0
   for item in l:
      sum=sum+item
   print(" The sum of items in list is :",sum)

def main():
   lst=[1,2,3,4,5,6]
   print("The list is : ",lst)
   sum_of_list(lst)
   
if __name__=="__main__":
   main()

print()   

"""2. A list containing the common elements from two lists."""
def common_element_in_list(l1,l2):
   """This function takes two lists as parameters and genarates a new list that contains common elements from both lists without using if-else statement."""
   set1=set(l1)
   set2=set(l2)
   set3=set1&set2
   l3=list(set3)
   print("The list containing common elements between {} and {} is {}".format(l1,l2,l3))

def main():
   list1=[1,2,3,4,4,5]
   list2=[2,4,4,6,8]
   list3=[1,3,5,7,9]
   """Add other lists as per necessity"""
   print("The first list is : ",list1)
   print("The second list is : ",list2)
   print("The third list is : ",list3)
   common_element_in_list(list1,list2)
   """Call the function with the desired lists as arguments"""
   common_element_in_list(list1,list3)

if __name__=="__main__":
   main()

print()   

"""3. A code to ask an input from the user which is a string and display the string along with its length."""
def display_string_and_length():
   """This function takes the user input string and displays the length without using len() function."""
   S=input("Enter a string :")
   print("The input string is :",S)
   counter=0
   for i in S:
      counter+=1
   print("The length of the string is : ",counter)

def main():
   display_string_and_length()

if __name__=="__main__":
   main()   
