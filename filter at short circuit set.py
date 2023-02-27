car_shop = [('Toyota', 1000), ('rectangular tire', 80), ('Porsche', 5000)]
def find_something_smaller_than(name_value_tuple):
 print('Check {0}, {1}$'.format(*name_value_tuple))
 return name_value_tuple[1] < 100
next(filter(find_something_smaller_than, car_shop))
