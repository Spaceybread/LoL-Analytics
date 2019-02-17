team1 = input("Enter the first team's name:  ")
team2 = input("Enter the second team's name:  ")

plyed1 = input("How many games has {} played?  ".format(team1))
won1 = input("How many games has {} won?  ".format(team1))
kills1 = input("How many kills took place in this team's last match?  ")
killed1 = input("How many of them were executed by this team:  ")
gold1 = input("How much gold did this team acquire?  ")
drakes1 = input("How many dragons were killed in the previous match?  ")
drakeskilled1 = input("How many drakes were executed by {}?  ".format(team1))

p1 = int(plyed1)
w1 = int(won1)
k1 = int(kills1)
kd1 = int(killed1)
g1 = (int(gold1))/1000
d1 = int(drakes1)
dk1 = int(drakeskilled1)


winch1 = (w1/p1)*100
killpart1 = (kd1/k1)*100
dchance1 = (dk1/d1)*100

winchance1 = winch1 + killpart1 + g1 + dchance1

plyed2 = input("How many games has {} played?  ".format(team2))
won2 = input("How many games has {} won?  ".format(team2))
kills2 = input("How many kills took place in this team's last match?  ")
killed2 = input("How many of them were executed by this team:  ")
gold2 = input("How much gold did this team acquire?  ")
drakes2 = input("How many dragons were killed in the previous match?  ")
drakeskilled2 = input("How many drakes were executed by {}?  ".format(team2))

p2 = int(plyed2)
w2 = int(won2)
k2 = int(kills2)
kd2 = int(killed2)
g2 = (int(gold2))/1000
d2 = int(drakes2)
dk2 = int(drakeskilled2)

winch2 = (w2/p2)*100
killpart2 = (kd2/k2)*100
dchance2 = (dk2/d2)*100

winchance2 = winch2 + killpart2 + g2 + dchance2

if (winchance1 > winchance2):
    print("{} may win".format(team1))
else:
    print("{} may win".format(team2))
