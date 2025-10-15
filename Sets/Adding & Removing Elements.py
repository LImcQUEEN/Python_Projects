newSet = {"apple", "banana", "cherry"}
veggies = {"carrot", "tomato", "potato"}
newSet.update(veggies)
#   veggies.remove("tomato")  # If item doesn't exist an error pop
#   veggies.discard("mango")  # no error if item not present
veggies.pop()
print(veggies)