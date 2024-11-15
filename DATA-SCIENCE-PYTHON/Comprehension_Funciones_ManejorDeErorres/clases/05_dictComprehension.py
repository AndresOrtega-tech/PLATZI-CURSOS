dict = {}
for i in range(1,11):
    dict[i] = i*2
print(dict)

dict_v2 = {i:i*2 for i in range(1,11)}
print(dict_v2)


countries = ['col', 'mex', 'bol', 'peru']
population = {}

import random
for n in countries:
    population[n] = random.randint(1, 100)
print(population)

population_v2 = {j:random.randint(1,100) for j in countries}
print(population_v2)


names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]

print(list(zip(names, ages)))

new_dict = {name:age for (name,age) in zip(names,ages)}
print(new_dict)