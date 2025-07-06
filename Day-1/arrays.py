# Stock Prices for 5 days
# price Day 1
# price Day 2

expense_list = [2200,2350,2600,2000,2190]
# extra money spent in february compared to January
feb_extra = expense_list[1] - expense_list[0]
print(feb_extra)
first_quarter_expense = expense_list[0] + expense_list[1] + expense_list[2]
print(first_quarter_expense)
for i in expense_list:
    if i == 2000:
        print(expense_list.index(i))

# add  june's expense on expense list
june = 1980
expense_list.append(june)
print(expense_list)

# refund of 200 in April
expense_list.remove(expense_list[3])
print(expense_list)
expense_list.insert(3, 2130)
print(expense_list)
new_April_expense = expense_list[3] - 200
expense_list.remove(expense_list[3])

expense_list.insert(3, new_April_expense)
print(expense_list)


# 2
heros = ['spider man','thor','hulk','iron man','captain america']
# length of the superheroes
print(len(heros))
heros.append('black panther')
print(heros)
heros.remove(heros[5])
heros.insert(3,'black panther')
print(heros)
heros[1:3] = ['doctor strange']
print(heros)
# sort in alphabetical order
hero = heros.sort()
print(expense_list)
print(heros)


# list of all odd numbers btwn 1 and max num from input
num = int(input("Please enter your number:\n"))
odd_list= []
for i in range(num):
    if i%2 != 0:
        odd_list.append(i)
        print(odd_list)
