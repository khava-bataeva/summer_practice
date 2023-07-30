import itertools

s = input("Введите список: ")
my_list = list(s)
permutations = list(itertools.permutations(my_list))

print([''.join(permutation) for permutation in permutations])
