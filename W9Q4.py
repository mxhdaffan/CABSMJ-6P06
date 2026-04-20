from operator import itemgetter

n = int(input("Enter the number of candidates: "))
election = {}

for i in range(n):
    name = input(f"\nEnter name of candidate {i+1}: ") 
    votes = int(input(f"Enter no. of votes of candidate {i+1}: "))

    election[name] = votes

print("Original List -> ", election)

asc = dict(sorted(election.items(), key=itemgetter(1)))
desc = dict(sorted(election.items(), key=itemgetter(1), reverse=True))

print("\nAscending List ->", asc)
print("Descending List ->", desc)

winner = list(desc.keys())[0]
loser = list(asc.keys())[0]
print("Winner = ", winner)
print("Loser = ", loser)