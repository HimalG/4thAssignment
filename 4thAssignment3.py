""" (1)  A program to display all prime numbers from 1 to 100."""

def prime_number_in_range(r):
    """This function prints the prime number from 1 to user input value"""
    for num in range(1,r+1):
        if num>1:
            """Number 1 is not considered as prime here"""
            for i in range(2,num//2+1):
                """No need to check to limit, because if a number is not divided by any number other than 1 till it's half, then it won't be divided by others."""
                if num%i==0:
                    """If any number is divided by the number between 2 and half of the number,that is not prime, so get out from the loop"""
                    break        
            else:
                print(num, end=" ")

def main():
    num=int(input("Enter the limit : "))
    print("The prime numbers from 1 to {} are : ".format(num))
    prime_number_in_range(num)

if __name__=="__main__":
    main()

print("\n")

""" (2) To print out whether the user entered string is a palindrome or not.""" 
def pallindrome(s):
    """This function prints out whether the user entered string is a palindrome or not""" 
    rev=s[::-1]
    """This slicing method reverses the string and the reversed value is stored in 'rev' variable"""
    if rev==s:
        print("The string is palindrome.")
    else:
        print("The string is not palindrome.")

def main():
    _str=input("Enter a string : ")
    pallindrome(_str)

if __name__=="__main__":
    main()

print()    
    


""" (3) A dictionary that has a key value pair of letters and the number of occurrences of that letter in a string.""" 
def dict_letters_with_count(s):
    """This function creates a dictionary having letter and their occurrences as key value pair"""
    d={}
    """Creates an empty dictionary"""
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    print("The desired result is : ",str(d))
    """Prints the string present in d"""

def main():
    _string=input("Enter a string : ")
    dict_letters_with_count(_string)

if __name__=="__main__":
    main()
