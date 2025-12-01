def multiple():
    return 2, 3, 5, 7, 11
print(multiple())

things = 'pen', 'tripod', 'water bottle', 'charger', 'phone', 'web cam', 'sunglass'
# print(type(things))
# print(things[0])
# print(things[-2])
# print(things[2:5])

if 'pen' in things:
    print('exists')
# for item in things:
#     print(item)

# things[0] = 'pencil'
# print(things)
#tuples are immutable, we cannot change the values once assigned

mega = ([2, 3, 5], [6,8,9,5])
print(mega[0])
mega[0][1] = 404
print(mega)
#tuple are immutable but if the tuple contains mutable elements like list, we can change the values inside the list
