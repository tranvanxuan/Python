my_list = ['red', 'blue', 'green']

# Get the last item with brute force using len
last_item = my_list[len(my_list)-1]

# Get the last item using negative 
# indices *preferred & quickest method*
last_item = my_list[-1]

# Get the last item using iterable unpacking
*_, last_item = my_list
print(last_item)

# remove the last item from the list using pop fuction
last_item = my_list.pop()