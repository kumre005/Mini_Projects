Your_name = input("Enter your name here : ")
Partners_name = input("Enter your's partner name here : ")

combine_name = Your_name + Partners_name
lower_case_string = combine_name.lower()

t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')

true= t+r+u+e

l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')

love = l+o+v+e

love_score = int(str(true) + str(love))
if love_score >80 or love_score <=100:
    print(f"Your love score is {love_score} & you go together like cock and mentos..!")
elif love_score>=60 and love_score<=80:
    print(f"Your love score is {love_score} & you allright together...!")
else:
    print(f"Your love score is {love_score}. ")
 