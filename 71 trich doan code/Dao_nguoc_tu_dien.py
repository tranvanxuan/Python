from collections import defaultdict
my_dict = {
    'Izuku Midoriya': 'One for All',
    'Katsuki Bakugo': 'Explosion',
    'All Might': 'One for All',
    'Ochaco Uraraka': 'Zero Gravity'
}
print(my_dict)
print('-----------------------------------------')
# invert a dictionary with map and reversed
my_inverted_dict = dict(map(reversed, my_dict.items()))
print(my_inverted_dict)

# with Zip
print('----------------------------')
my_dic_zip = dict(zip(my_dict.values(), my_dict.keys()))
print(my_dic_zip)

# Invert a Dictionary with a Comprehension
print('----------------------------------')
my_inverted_dict = {value: key for key, value in my_dict.items()}
print(my_inverted_dict)

print('------------------with Defaultdict----')
# with Defaultdict
my_inverted_dict = defaultdict(list)
{my_inverted_dict[v].append(k) for k, v in my_dict.items()}
print(my_inverted_dict)

print('------------a For Loop')
# with a for loop
my_inverted_dict = dict()

for key, value in my_dict.items():
    my_inverted_dict.setdefault(value, list()).append(key)
print(my_inverted_dict)
