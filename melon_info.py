"""Print out all the melons in our inventory."""


from melons import melons


# def print_melon(name, price, seedless):
#     """Print each melon with corresponding attribute information."""

#     have_or_have_not = 'do not have'
#     if name['is_seedless']:
#         have_or_have_not = 'have'

#     print(f'{name}s {have_or_have_not} seeds and are ${price}')

def print_all_melons(melons):
    # for key, value
    for melon_name, attributes in melons.items():
        print('melon_name: ', melon_name)
        print('attributes: ', attributes)
        print(melon_name.upper())
        for attribute, value in attributes.items():
            print(f'{attribute}: {value}')
        print('===================================')

print_all_melons(melons)


# for melon in melons:
#     print_melon(melon, melon['price'], melon['is_seedless'])
