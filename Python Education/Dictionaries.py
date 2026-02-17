#dictionary={key:value}

numbers={'one':1, 'two':2, 'three':3}

status={
    "Mission 1 success": True,
    "Mission 2 success": True,
    "Mission 3 success": True,
    "Mission 4 success": False,
    "Mission 5 success": False,
    "Mission 6 success": True
}
'''
print(status["Mission 1 success"])
print(status["Mission 2 success"])
print(status["Mission 3 success"])
print(status["Mission 4 success"])
print(status["Mission 5 success"])
print(status["Mission 6 success"])
'''
status["Mission 4 success"]= True #Alter the values of key in the dictionaries
#print(status["Mission 4 success"])

status["Mission 7 success"]=False #adds an entirely new key and value to the dictionary
#print(status["Mission 7 success"])

status.update({"Mission 4 success": True}) #updates the value of a key
#print(status.items())
#Note: The update() function can accept dictionaries with multiple items.If an item is new, it will be added to the original dictionary.
status.pop("Mission 5 success")#removes a key and its value
#print(status.items())

#the 'in' function for searching
#print("mission 3 success" in status)

#Dictionaries using for loop
for i in status:
    print(i)

'''
info_keys = status.keys()
info_values = status.values()

print(info_keys)
print(info_values)

search=status.get("Mission 4 success")#one specific item
info=status.items()
print(info)
'''