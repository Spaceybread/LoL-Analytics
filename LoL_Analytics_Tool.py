team1 = "lol"
team2 = "analytics"
team1 = input("Enter the first team's name:  ")
team2 = input("Enter the second team's name:  ")

plyed1 = input("How many games has {} played?  ".format(team1))
won1 = input("How many games has {} won?  ".format(team1))
kills1 = input("How many kills took place in this team's last match?  ")
killed1 = input("How many of them were executed by this team:  ")
gold1 = input("How much gold did this team acquire?  ")


kills1a = input("How many kills took place in this team's 2nd last match?  ")
killed1a = input("How many of them were executed by this team in the aforementioned match:  ")
gold1a = input("How much gold did this team acquire in the aforementioned match?  ")


p1 = int(plyed1)
w1 = int(won1)
k1 = (int(kills1)+int(kills1a))/2
kd1 = (int(killed1)+int(killed1a))/2
g1 = (int(gold1)+int(gold1a))/1000

winch1 = (w1/p1)*100
killpart1 = (kd1/k1)*100


winchance1 = winch1 + killpart1 + g1

plyed2 = input("How many games has {} played?  ".format(team2))
won2 = input("How many games has {} won?  ".format(team2))
kills2 = input("How many kills took place in this team's last match?  ")
killed2 = input("How many of them were executed by this team:  ")
gold2 = input("How much gold did this team acquire?  ")


kills2a = input("How many kills took place in this team's 2nd last match?  ")
killed2a = input("How many of them were executed by this team in the aforementioned match:  ")
gold2a = input("How much gold did this team acquire in the aforementioned match?  ")


p2 = int(plyed2)
w2 = int(won2)
k2 = (int(kills2)+int(kills2a))/2
kd2 = (int(killed2)+int(killed2a))/2
g2 = (int(gold2)+int(gold2a))/1000

winch2 = (w2/p2)*100
killpart2 = (kd2/k2)*100


winchance2 = winch2 + killpart2 + g2

skrm = input("Have these teams fought before (y/n)?  ")
if skrm == "y":
    won = input("Who won the last match? (1/2)  ")
    if won == "1":
        winchance1 = winchance1 + 12.5
    else:
        winchance2 = winchance2 + 12.5
else:
    print("")
if (winchance1 > winchance2):
    print("{} may win".format(team1))
    print(winchance1)
    print(winchance2)
else:
    print("{} may win".format(team2)) 
    print(winchance1)
    print(winchance2)

