#9-15 Lottery Analysis
from random import choice
options = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

my_tickets = [ 2, 'a', 5, 'c']

loops = 0
while my_tickets:
    winner = choice(options)
    if winner in my_tickets:
        my_tickets.remove(winner)
        print(f"My ticket: {winner} has won")
    loops += 1

print(f"I need {loops} oportunities to won in all my tickets")