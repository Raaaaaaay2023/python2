#11
# n=int(input())
# coins=input()
# heads=coins.count("H")
# tails=coins.count("T")
# print(abs(n//2-max(heads,tails)))

#2
# s=int(input("Please enter the sum of theese two numbers"))
# p=int(input("please enter the product of the two numbers"))
# for x in range(1,1001):
#     if p%x==0 and p//x+x==s:
#         y=p//x
#         print(x,y)
#         break
# else:
#     print("no solution")

#3
# n=int(input("Please enter a number n "))
# power = 1
# while power <= n:
#     print(power)
#     power *= 2
n = int(input())
i = 0
while 2 ** i <= n:
    print(2 ** i)
    i += 1
