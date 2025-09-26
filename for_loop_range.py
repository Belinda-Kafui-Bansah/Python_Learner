#Sum of the first 100 natural numbers

#Using for loop
total = 0
for num in range(101):
     total = total + num
print (total)

#Using python built-in sum()
total = sum(range (101))
print (total)