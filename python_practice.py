# # count the total numbers of characters in string..

# st= input("enter the name:")

# count=0

# for i in st:
#     count=count+1
# print(count)




# #count the total numbers of words in the string

# st=input("Enter the string:")
# st1=st.split()
# count=0

# for i in st1:
#     count=count+1
# print(count)




# #count the upper case char in the string...

# st=input("enter the string:")

# count=0

# for i in st:
#     if i.isupper():
#         count=count+1
# print(count)





# #count the number of VoWels in the string

# st=input("Enter the string :")

# count=0

# Vowels="AEIOUaeiou"

# for i in st:
#     if i in Vowels:
#         count=count+1
# print(count)






# # count the special char in to the string

# st=input("Enter the string:")
# count=0
# import string

# lower=string.ascii_letters
# print(lower)

# for i in st:
#     if i not in lower:
#         count=count+1
# print(count)






# #count the occurence of each vowel

# st=input("enter the string:")

# vowel="aeiou"

# d={ }.fromkeys(vowel,0)

# for i in st:
#     if i in d:
#         d[i]=d[i]+1
# print(d)





# # count the occurence of each char in to the string

# st=input("Enter the string:")

# st1=set(st)

# d={ }.fromkeys(st1,0)

# for i in st:
#     if i in d:
#         d[i]=d[i]+1
# print(d)




# #fetch the char if the word have even number of char

# st=input("enter the string:")

# st1=st.split()
# NewList=[]
# for i in st1:
#     if len(i)%2==0:
#         NewList.append(i)
# print(NewList)





# #fetch the word has starts with capital latter

# st=input("Enter the string:")
# st1=st.split()

# NewList=[]

# import string
# lower=string.ascii_uppercase

# for i in st1:
#     if i[0] in lower:
#         NewList.append(i)
# print(NewList)



# #fetch the word is start and end with consonent (not in vowels)

# st=input("enter the string:")
# st1=st.split()

# NewList=[]
# for i in st1:
#     if i[0].lower() not in "aeiou" and i[-1].lower() not in "aeiou":
#         NewList.append(i)
# print(NewList)




# #write a program for fetching vowels in the string

# st=input("Enter the string:")

# v="aeiou"

# allvowels=[]

# for i in st:
#     if i in v:
#         allvowels.append(i)
# print(allvowels)






# #write a program for fetching all consonents in the string

# st=input("Enter the string:")

# v="aeiou"

# allvowels=[]

# for i in st:
#     if i not in v:
#         allvowels.append(i)
# print(allvowels)




# #fetch the first char of the word in sentence

# st=input("Enter string :")
# st1=st.split()

# print([i[0]for i in st1])
    


# #fetch the last char of the word in sentence

# st=input("Enter the string:")

# st1=st.split()

# print([i[-1] for i in st1])



# #fetch the first and last char of the word in sentence

# st=input("Enter the string:")

# st1=st.split()

# print([i[0] + i[-1] for i in st1])



# # fetching specieal char into the string 

# st=input("Enter the string :")

# import string

# string.ascii_letters
# string.digits

# print([ i for i in st if i not in string.ascii_letters and i not in string.digits and i != " "])





# #reverse the given string..

# st=input("Enter the string :")

# # st1=" ".join(reversed(st))
# # print(st1)

# # print(st[-1::-1])

# st1=''
# for i in st:
#     st1=i+st1
# print(st1)




# # write a program to sort the string into the ascending order..

# st=input("Enter the string :")

# st1=" ".join(sorted(st))

# print(st1)


# # decending 

# st=input("Enter the string :")

# st1=" ".join(sorted(st , reverse=True))

# print(st1)



# # reverse the sentence 

# st=input("Enter the string :")

# st1=st.split()
# output=""

# for i in st1:
#     output=i+" " +output
# print(output)




# # swapping the cases into the given string 

# st=input("Enter the string :")

# st1=""

# for i in st:
#     if i.isupper():
#         st1=st1+i.lower()
#     elif i.islower():
#         st1=st1+i.upper()
# print(st1)




# # interchangeing key and value in dictionary

# st={"name":"Aaditya","surename": " bandhane" , "Mobile": 9324631068}

# print({value:key for key,value in st.items()})




# # finding the squeres of all even numbers

# lst=[1,2,3,4,5,6,7,8,9]

# squeres=[]

# for i in lst:
#     if i%2==0:
#         squeres.append(i*i)
# print(squeres)


