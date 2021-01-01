#!/usr/bin/env python3

from functools import reduce
from itertools import permutations
from operator import or_
import re

puzzle = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""

with open('input21.txt') as f:
    puzzle = f.read()

# Allergens in input rows, list of sets.
all_list = []
# ingredients in input rows, list of sets.
ing_list = []
all_allergens = set()
all_ingredients = set()

if __name__ == '__main__':

    for line in puzzle.split('\n'):
        if line == '':
            continue
        match = re.search(r'(^[a-z ]+)(\(.+\))', line)
        ingredients = match.group(1).strip().split()

        allergens = re.findall(r'(?:\A\(contains |, )([a-z]+)', match.group(2))
        all_list.append(set(allergens))
        ing_list.append(set(ingredients))
        all_allergens = all_allergens.union(set(allergens))
        all_ingredients = all_ingredients.union(set(ingredients))

    # == Match allergen to ingredient ==
    allergen_ingredient = {}
    for agens, ingients in zip(all_list, ing_list):
        for a in agens:
            if a not in allergen_ingredient.keys():
                allergen_ingredient[a] = ingients
            else:
                allergen_ingredient[a] = ingients.intersection(
                    allergen_ingredient[a])

    # == create set of all possibly allergenic ingredients ==
    allergenic_ingredients = reduce(or_, allergen_ingredient.values())
    nonalergenic_ingredients = all_ingredients.difference(
        allergenic_ingredients)

    count = sum(
        (len(nonalergenic_ingredients.intersection(ing)) for ing in ing_list))

    print('Answer part 1: {}'.format(count))

    # Brute force a sollution for part 2.
    alfabetic_allergens = list(all_allergens)
    alfabetic_allergens.sort()
    for order in permutations(allergenic_ingredients):
        if all([
                i[1] in allergen_ingredient[i[0]]
                for i in zip(alfabetic_allergens, order)
        ]):
            break

    print('Answer part 2: {}'.format(','.join(order)))
