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




# # reverse the dictionary

# d={"a":10,"b":20,"c":30}

# lst=(list(d.items()))
# lst.reverse()

# d1={}

# for key,value in lst:
#     d1[key]=value
# print(d1)





# #fetch unique elements from list 

# lst=[1,2,3,4,1,2,4]

# # print(list(set(lst)))

# lst1=[]

# for i in lst:
#     if i not in lst1:
#         lst1.append(i)
# print(lst1)





# # fetch the integer type values from the list

# lst=[1,"as", True,52,"asas"]

# lst1=[]

# for i in lst:
#     if type(i) is int:
#         lst1.append(i)
# print(lst1)






# #write a count of char repeting more time in string

# st=input("Enter the string :")

# d={}.fromkeys(set(st),0)

# for i in st:
#     d[i]=d[i]+1

# print(d)




# # fetch all pallindrom word into the list

# lst=["python","nen","cource","madam"]

# pallindroms=[]

# for i in lst:
#     if i==i[-1::-1]:
#         pallindroms.append(i)
# print(pallindroms)





# # reversce the words into the given string

# st=input("Enter the string :")

# st1=st.split()

# print(" ".join(st1[-1::-1]))




# # revercse the each char into the words

# st=input("enter the string :")

# st1=st.split()

# newlst=[]

# for i in st1:
#     newlst.append(i[-1::-1])

# print(" ".join(newlst))




# #fetch the longest word and shortest word

# st="aadi aaditya bandhane"

# print([i for i in st.split() if len(i)== max([len(i) for i in st.split()])])
# print([i for i in st.split() if len(i)== min([len(i) for i in st.split()])])




# # find the index number of occured into the string

# st=" aaditya bandhane"

# char=input("enter the character :")

# for i in range(0,len(st)):
#     if st[i]== char:
#         print(i)




# # find the missing numbers from the list

# lst=[1,2,8,5,6,7,10,11,14]

# maxnum=max(lst)
# minnum=min(lst)

# missnums=[]

# for i in range(minnum,maxnum+1):
#     if i not in lst:
#         missnums.append(i)
# print(missnums)




# # ATM machine 

# print("Welcome to State bank of India")
# p=int(input("Enter your 4 digit pin number: "))
# m = 25000

# if(p == 1234):
#     print("1-Withdraw")
#     print("2-Balance Enquiry")
#     print("3-Fast Cash")
#     c = int(input("Please choose transactions: "))
#     if (c == 1):
#         w=int(input("Enter withdraw amount: "))
#         if (w < m and w%100 == 0):
#             print("Please take your amount:", w)
#         else:
#             print("Invalid cash")

#     elif(c==2):
#         print("Your available amount : ",m)
#     elif (c == 3):
#         print("1->5,000")
#         print("2->10,000")
#         print("3->15,000")
#         print("4->20,000")
#         f = int(input("Enter fast cash option: "))
#         if (f == 1 and 5000 < m):
#             print("please take cash 5000")
#         elif (f == 2 and 10000 < m):
#             print("please take cash 10000")
#         elif (f == 3 and 15000 < m):
#             print("please take cash 15000")
#         elif (f == 4 and 20000 < m):
#             print("please take cash 20000")
#         else:
#             print("Invalid fast cash option")
#     else:
#         print("Wrong choice")
# else:
#     print("Wrong pin number")





# # fetch the non-repeated element in the list

# lst=[1,2,2,3,4,5,4,5]
# lst1=[]
# for i in lst:
#     if lst.count(i)==1:
#         lst1.append(i)
# print(lst1)




# fetch the elements which have duplicates in the list

# lst=[1,2,3,4,2,1,4,5]

# print(list({i for i in lst if lst.count(i)>=2}))



# # fetch the elements which have duplicates in the list

# lst = [1, 2, 3, 4, 2, 1, 4, 5]
# duplicates = set()

# for i in lst:
#     count = lst.count(i)
#     if count >= 2:
#         duplicates.add(i)

# duplicates_list = list(duplicates)

# print(duplicates_list)



# fetch the highest value into the list without using built-in function

# lst=[10,2,45,780,77]

# print(max(lst))

# lst.sort()
# print(lst[-1])

# maxval=0

# for i in lst:
#     if i > maxval:
#         maxval=i
# print(maxval)






# fetch the secound highest value into the list without using built-in function

# lst=[10,2,45,780,77]

# maxval=0

# for i in lst:
#     if i > maxval:
#         maxval=i
# print(maxval)

# secmaxval=0

# for j in lst:
#     if j > secmaxval and j < maxval:
#         secmaxval=j
# print(secmaxval)




# # fetch the repeated words  in the string

# st="aaditya bandhane aadi developer aadi"

# st1=st.split()

# reapeted=set()

# for i in st1:
#     if st1.count(i)>1:
#         reapeted.add(i)

# reapeted_words=list(reapeted)
# print(reapeted_words)




# # write the program to display more repeated words

# st="AAdi bandhane aaditi bandhane and bandhanepada "

# st1=st.split()
# s=set(st1)

# d={}.fromkeys(s,0)

# for i in st1:
#     if i in d:
#         d[i]=d[i]+1
# print(d)

# for i in d:
#     if d[i]==max(d.values()):
#         print(i)