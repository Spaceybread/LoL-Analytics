
played = input('How many games has this team played?  ')
won = input('How many games has this team won?  ')
p = int(played)
w = int(won)
gold = input('How much gold does this acquire on average?  ')
g = int(gold)
kills = input("How many kills take place on an average in this team's games?  ")
executions = input("How many kills does this team execute?  ")
k = int(kills)
e = int(executions)
barons = input("How many barons are killed in their game on an average?  ")
baron = input("How many barons does this team kill on an average?  ")
bs = int(barons)
b = int(baron)

winscore = ((w/p)*100) + (g/1000) + ((e/k)*100) + ((b/bs)*100)

print("This team has a score of {}".format(winscore))