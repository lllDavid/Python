from collections import OrderedDict

od = OrderedDict()

od['tim'] = 1
od['daniel'] = 2
od['mark'] = 3

od.move_to_end('daniel')

od.move_to_end('tim', last=False)

last_item = od.popitem()

first_item = od.popitem(last=False)

for key, value in od.items():
    print(key, value)

print("Popped last item:", last_item)
print("Popped first item:", first_item)