winter_fruits = {"apple", "orange", "grape"}
summer_fruits = {"walnut", "berry", "apple"}
#   all_fruits = summer_fruits.union(winter_fruits)
#   summer_fruits.update(winter_fruits)
#   print(all_fruits)
#   print(summer_fruits)
#   Both union and update exclude duplicate items
#   Update change the original set
#   winter_fruits.intersection_update(summer_fruits)
#   print(winter_fruits)
#   intersection_update only keep the common value in original sets
temp = winter_fruits.difference(summer_fruits)
print(temp)
temp2 = winter_fruits.symmetric_difference(summer_fruits)
print(temp2)
winter_fruits.symmetric_difference_update(summer_fruits)
print(winter_fruits)