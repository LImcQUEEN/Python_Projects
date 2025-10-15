summer_fruits = {"apple", "banana", "orange"}
winter_fruits = {"cherry", "avocado", "strawberry", "apple"}
dry_fruits = ("hazelnut", "almond")
fruits = summer_fruits.union(winter_fruits, dry_fruits)
for x in fruits:
    print(x)