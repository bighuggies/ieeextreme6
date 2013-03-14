#!/usr/bin/env python

# In a forest, there were 'x' bunnies, 50% male, and 50% female, all adults. Bunnies doubles every 15 days, 10% of the baby rabbits dies at birth. They mature after 30 days, 30% leave the forest, and rest becomes rabbits. In every 30 days , 25% dies off due to flu. If every bunny dies off, the bunny world ends.

# All bunnies are initially adults

# Every 15 days:
#   Adult rabbits each have two babies
#   10% of babies die

# Every 30 days:
#   30% of babies leave the forest
#   Babies become adults
#   25% of adults die of flu

#To be clear, the adult population doubles yeah? IE the amount of new babies is equal to 90% of the current number of adults? Yes

# Just the adult rabbits die off. Say, if the total population is 100, and we have 100 rabbits, the population after the flu would be 75.

# Rabbits multiplies and then suffers flu.

# Only mature rabbits double.


babies = 0
kids = 0
adults = int(raw_input())

for day in xrange(1, 366):
    if day % 30 == 0:
        # Get the flu
        adults = int(adults * .75)

        # Graduate the kids, 30% leave the forest
        adults += int(kids * 0.7)
        kids = 0

    if day % 15 == 0:
        kids = babies
        babies = int((adults * 2) * 0.9)


print((babies, kids, adults, babies + kids + adults))
