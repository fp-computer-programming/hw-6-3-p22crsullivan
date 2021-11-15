# Author: CRS 11/15/21
lst = list(input("Please enter a list of numbers or letters separated by spaces."))
answer = input("Would you like the middle or end of the input?")
if answer == "end":
    lst.reverse()
    print(lst[0])
elif answer == "middle":
    lst.reverse()
    lst.remove(lst[0])
    lst.reverse()
    lst.remove(lst[0])
    print(lst)
