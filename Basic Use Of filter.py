names = ['Fred', 'Wilma', 'Barney']
def long_name(name):
 return len(name) > 5
print(filter(long_name, names)
)
print(list(filter(long_name, names)) )