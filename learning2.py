# def myfunc(string):
#     string= string[0].upper()+string[1:3]+string[3].upper()+string[4:]
#     return string
# print(myfunc("macdonald"))

# def myfunc(sentence):
#     list1=list(sentence.split())
#     for i in sentence:
#         str="  ".join(list1[::-1])
#         return str
# print(myfunc(" i am home"))

# def myfunc(*arg):
#     for i in range(0,len(arg)-1):
#         if arg[i]==3 and arg[i+1]==3:
#             return True
#     return False


# def myfunc(name):
#     str=''
#     for i in range(0,len(name)):
#         str+=name[i]*3
#     return str
#
#
# print(myfunc("hello"))

#
# # def myfunc(a,b,c):
#     if ((a+b+c)<=21):
#         return (a+b+c)
#     elif ((a+b+c)>21 and (a==11 or b==11 or c==11)):
#         if((a+b+c-10)>=21):
#             return (a + b + c - 10)
#
#       else:
#             return "bust"

#
# print(myfunc(9,9,9))

# def myfunc(*arg):
#     return sum(arg)
#     # for i in range(0,len(list)):
#     #     if arg[i]==6:
#     #         return list(sum(arg) - sum(arg[i:arg]))
#     #     else:
#     #         return list(sum(arg))
#
# print(myfunc[1,2,3])



# def myfunc(x):
#     return (100-abs(x)<=10 or 200-abs(x)<=10)
#
#
# print(myfunc(77))
# good one writing  while loop


def myfunc(num):
    total = 0
    add = True
    for i in num:
        while add:
            if i != 6:
                total += i
                break
            else:
                add = False
        while not add:
            if i != 9:
                break
            else:
                add = True
                break
    return total


print(myfunc([1, 2, 3, 4]))


