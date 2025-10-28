import random
import string

BOLD = '\033[1m'
END = '\033[0m'

print(BOLD + "WELCOME TO PASSWORD GENERATOR \n\n" + END) #welcome note in bold

#instead of manually entering the list i have imported lists from predefined libraries
letters = list(string.ascii_letters)
nums = list(string.digits)
symb = list(string.punctuation)

password =[] #a list to contain the elements of password

length = int(input("Enter how long you need your password to be:\n "))
l = int(input("Enter how many letters do you want in your password:\n "))
s = int(input("Enter how many symbols do you want in your password:\n "))
n = int(input("Enter how many numbers do you want in your password:\n "))



remaining = length - (l+s+n)    #calculating the difference if any, (refer to line 51-56)

def generator(length,l,n,s,password):    #the main pard of the code
    if l>0 and s>0 and n>0:
        if (l+s+n) <= length:
            for j in range(1, l+1):
                password.append(random.choice(letters)) #appends password list from the list containing alphabets (letters)
            for k in range(1, s+1):
                password.append(random.choice(symb))  #appends password list from the list containing symbols (symb)
            for x in range(1, n+1):
                password.append(random.choice(nums))  #appends password list from the list containing numbers (nums)
    else:
        print("\n Give atleat 1 of each attribute(letters, numbers, symbols) for security purpouses ")    

    random.shuffle(password)    #for better security, using random function to shuffel eveything in the password list

    for z in password:
        print(BOLD + z + END, end="")    #printing final output in bold and without " [] "

if (l+s+n) > length:    #if given sum of l,s,n exceeds length is not valid 
    print("ERROR: number of attributes entered is exceeding the length ")

elif (l+s+n) < length:  #if given sum of l,s,n is less than length, below lines will add more length at a random variable
    print("ERROR: entered attributes are less than length")
    c = input("do you want to automatically fill up the space? enter yes or no: ")  #requesting user authority
    c = c.lower()   #lowerizing text for conditonal function
    if c == "yes":
        length += remaining
        rand = random.choice(["l","s","n"])   #choosing random from a list  to extend the "remaining", to a particular attribute(l/s/n)
        if rand == "l":
            l+=remaining
        elif rand == "s":
            s+=remaining
        else:
            n+=remaining
        
        print(f"new lengths of l s n  are as following: {l, s, n}") #printing just for reference
        generator(length,l,n,s,password)    #runs the generator when sum of l,s,n is equal to length
        
    if c == "no":   #to end the program if authority denied
        print("re run the program")

else:   #if given length and attributes match
    generator(length,l,n,s,password)


