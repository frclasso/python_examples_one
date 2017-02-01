#!/usr/bin/python


#%%
def print_phrase():
    phrase = "Now is the time"
    print (phrase)

print_phrase()
#%%
"""
Exercise 2
"""
#%%
def favorite_sport(favorite):
    sport = "favorite"
    print("Your" ,favorite, " sport is",sport)


favorite_sport()
#%%

"""Exercise 3 """
#%%
def username(yourname):
    print("Your name is ",yourname)


username()
#%%

""" Exercise 4 """
#%%
def compare_numbers(x,y):
    if x == y:
        print("they are equal")
    else
        print(x, "and", y, 'are not equal')

compare_numbers(2,3)
#%%

""" Exercise 5 """
#%%
def count_by_5():
    """ Count from 5 to 100 in steps of 5 """
    """ 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100 """
    print ('Counting from 5 through 100 in steps of 5')
    ct = 5
    while ct <= 100:
        print(ct, end = " ")
        ct = ct + 5


count_by_5()

#%%