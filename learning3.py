# def volume(rad):
#     return (4/3)*3.14*(rad**3)
# print(volume(2))

#
# def myfunc(num,low,high):
#     if num<low:
#         return False
#     else:
#         if num>high:
#             return False
#         else:
#             return True
#
#
# print(myfunc(1,1,10))

#
# def myfunc(sentence):
#     uppercount=0
#     lowercount=0
#     for i in range(0,len(sentence)):
#         if sentence[i] .isupper():
#             uppercount+=1
#         else:
#             if sentence[i] .islower():
#                 lowercount+=1
#     return (f"No of Upper case characters: {uppercount} \n No of lower case: {lowercount}")
# print(myfunc('Hello Mr. Rogers, how are you this fine Tuesday?'))

# def myfunc(list1):
#     list2=set(list1)
#     return (list2)
#
# print(myfunc([1,1,1,1,2,2,3,3,3,3,4,5]))


# def myfunc(string):
#     return string[::-1] == string
#
#
# print(myfunc("helleh"))

# import string
# def ispangram(str1, alphabet=string.ascii_lowercase):
#     list2=list(alphabet)
#     list2.append(1)
#     print(list2)
#     for i in range(0,len(str1)):
#         for j in range(0,len(list2)-1):
#             while (str1[i] == list2[j]):
#                 list2.pop(j)
#         print(list2)
#     return len(list2)==1
#
# print(ispangram("The quick brown fox jumps over the lazy dog"))


