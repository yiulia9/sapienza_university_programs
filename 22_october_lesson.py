#write a function that converts a string number into an int WITHOUT using int(string)
num = {
    "1":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9
}

#solution from the professor

#def solution():
#    num=0
#    for ch in str:
#        return

#my take until time ran out, fixed it later

def string_to_int(s):
    sum=0
    i=1
    for c in s:
        if c.isalpha() or c==" ":
            print(f"\nthe character \"{c}\" is a letter")
        else:
            number= (num.get(c))*10**((len(s)-i))
            sum+=number
            i+=1
    return sum


#if __name__=="__main__":
#    s=input("Tell me a number and I will turn it into an int for some unknown reasons, idk I have to do it man:\n")
#    print(string_to_int(s))

#convert an int into a string

strings = {
    1:"1",
    2:"2",
    3:"3",
    4:"4",
    5:"5",
    6:"6",
    7:"7",
    8:"8",
    9:"9"
}

#solution from the professor

#def solution_2(integer):
#    converted_str=""
#    while integer != 0:
#        converted_str += strings.get(integer%10)
#        integer //=10
#    return converted_str[::-1]

#my take until time ran out

def int_to_string(x):
    numchar=0
    str_num=[]
    sum_percent=1
    if x==str:
        print("that is already a string")
    for el in str_num:
        while numchar!=el:
            numchar=x%10**sum_percent
            str_num.append(numchar)
            sum_percent+=1
            
        
    

        
    

if __name__=="__main__":
    x=int(input("gimme an int number pls\n"))
    int_to_string(x)

#write a function that takes the elements from a list with sublists and puts them in a normal list
#example [1,[2, 3], [4, [5]], 6] -> [1, 2, 3, 4, 5, 6]

#my take before time ran out

#badlist=[1,[2,[4,[5],6],7],8]
#good_list=[]
#def better_list(bad_list):
#    for el in bad_list:
#        while type(el) == type(badlist):
#            better_list(el)
#        else:
#            good_list.append(el)
#    return good_list

         
#if __name__=="__main__":
#    bad_list=badlist
#    print(better_list())

#create a function that converts a string into a tuple list with the single words and the frequency in which they appear
#use the function isalnum() to test the chararcters and exclude alphanumeric ones

#tuple_list=[]

#def string_to_tuple(x):
#    for el in x:
#        while el==" ":
#            words= x[0:el]
#            counter = (words, len(words))
            

#if __name__=="__main__":
#    x=input("tell me a story\n")
#    string_to_tuple(x)