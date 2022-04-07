
people = 0
num_dogs = 0
hot_dogs = 10
buns = 8
leftover_buns = 0
leftover_dogs = 0


people = int(input("How many people are attending the cookout?: "))
num_dogs = int(input("How many hot dogs per person?: "))
total_dogs = people * num_dogs

package_dogs = 1
while hot_dogs < total_dogs:
    hot_dogs += 10
    package_dogs += 1


package_buns = 1
while buns < total_dogs:
    buns += 8
    package_buns += 1

leftover_buns = buns - total_dogs
leftover_dogs = hot_dogs - total_dogs

print(f'The minimum number of packages for hot dogs is {package_dogs}')
print(f'The minimum number of packages for hot dog buns is {package_buns}')
print(f'The number of hot dogs that will be left over is {leftover_dogs}')
print(f'The number of hot dog buns that will be left over is {leftover_buns}')