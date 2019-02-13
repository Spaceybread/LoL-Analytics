team1 = input("Enter the first team's name:  ")
team2 = input("Enter the second team's name:  ")

plyed1 = input("How many games has {} played?  ".format(team1))
won1 = input("How many games has {} won?  ".format(team1))
kills1 = input("How many kills took place in this team's last match?  ")
killed1 = input("How many of them were executed by this team:  ")
gold1 = input("How much gold did this team acquire?  ")

p1 = int(plyed1)
w1 = int(won1)
k1 = int(kills1)
kd1 = int(killed1)
g1 = (int(gold1))/1000

winch1 = (w1/p1)*100
killpart1 = (kd1/k1)*100

winchance1 = winch1 + killpart1 + g1

plyed2 = input("How many games has {} played?  ".format(team2))
won2 = input("How many games has {} won?  ".format(team2))
kills2 = input("How many kills took place in this team's last match?  ")
killed2 = input("How many of them were executed by this team:  ")
gold2 = input("How much gold did this team acquire?  ")

p2 = int(plyed2)
w2 = int(won2)
k2 = int(kills2)
kd2 = int(killed2)
g2 = (int(gold2))/1000

winch2 = (w2/p2)*100
killpart2 = (kd2/k2)*100

winchance2 = winch2 + killpart2 + g2

if (winchance1 > winchance2):
    print("{} may win".format(team1))
else:
    print("{} may win".format(team2))
