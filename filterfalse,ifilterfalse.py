from itertools import filterfalse
# Usage without function (None):
print(list(filterfalse(None, [1, 0, 2, [], '', 'a'])) )

#with function
names = ['Fred', 'Wilma', 'Barney']
def long_name(name):
 return len(name) > 5
print(list(filterfalse(long_name, names)))
