#import requests

# my_list = ["fish", "fun", 7, "taco"]
# #print(my_list)
# my_list.append("burrito")
# print(my_list)
# del my_list[2]
# print(my_list)

# print("Hello \
# What is shaking and baking?")
# print("\a")
# print("\tHermit")
# print("time oh yeah!")

# f = 5
# g = 6
# t = (f*g)
# print(t)

# def fishsticks(stuff):
#     pie = "You love the fishy {}?".format(stuff)
#     return pie

# ask = input("What is your favorite food?")
# ask1 = input()
# food = fishsticks(ask)

# print(food)
# print(len(ask1))

# #Write your function here
# def double_index(lst, index):
#   if index < len(lst):
#   	lst[index] = lst[index] * 2
#   return lst

# #Uncomment the line below when your function is done
# print(double_index([3, 8, -10, 12], 6))


def remove_middle(lst, start, end):
    st = lst[:start]
    en = lst[end + 1:]
    return st + en
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

#Write your function here
def more_than_n(lst, item, n):
  if lst.count(item) > n:
  	return True
  else:
    return False

#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

def more_frequent_item(lst, item1, item2):
  item1_count = lst.count(item1)
  item2_count = lst.count(item2)
  
  if item1_count < item2_count:
    return item2
  else:
    return item1
  
#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
"""
#Write your function here
def more_frequent_item(lst, item1, item2):
  if lst.count(item1) < lst.count(item2):
    return item2
  else:
    return item1
  
#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
"""
#Write your function here
def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return sum / 2
  else:
    return lst[int(len(lst)/2)]

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))

def append_sum(lst):
  i = 0
  while i < 6:
    i = i + 1
    lst.append(lst[-1] + lst[-2])
  return lst


#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))

#Write your function here
def larger_list(lst1, lst2):
  if len(lst2) > len(lst1):
    return lst2[-1]
  else:
    return lst1[-1]

#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10,]))

#Write your function here
def combine_sort(lst1, lst2):
  return sorted(lst1 + lst2)

#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

#Write your function here
def append_size(lst):
  to_append = list(range(1, len(lst)+1))
  lst = lst + to_append
  return lst

#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))

#Write your function here
def every_three_nums(start):
    return list(range(start, 101, 3))

#Uncomment the line below when your function is done
print(every_three_nums(91))

students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
#print(students_period_A)
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]
#print(students_period_B)

for student in students_period_A:
  students_period_B.append(student)
  print(student)
  
#print(students_period_B)

items_on_sale = ["blue_shirt", "striped_socks", "knit_dress", "red_headband", "dinosaur_onesie"]

print("Checking the sale list!")
for item in items_on_sale:
  print(item)
  if item == "knit_dress":
    break
print("End of search!")

dog_breeds_available_for_adoption = ['french_bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmation'

for dog in dog_breeds_available_for_adoption:
  print(dog)
  if dog == dog_breed_I_want:
    print("They have the dog I want!")
    break

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
  if age < 21:
    continue
  print(age)

  sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  print(location)
  for elements in location:
  	scoops_sold += elements
print(scoops_sold)

words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", "@matchamom", "follow", "#updog"]
usernames = []

for word in words:
  if word[0] == '@':
    usernames.append(word)













