from player import Player
from match import Match
from round import Round
from tournament import Tournament


player1 = Player("Berbour", "Abdel", "MAi", "M", "2", "red")
player2 = Player("Bruce", "lee", "juin", "M", "1", "red")
player3 = Player("Batman", "john", "juillet", "M", "3", "red")
player4 = Player("Spiderman", "max", "aout", "M", "4", "red")


player1.save()
player2.save()
player3.save()
player4.save()


match1 = Match(player1, 5, player2, 2)

tmatch1 = match1.match_name()  #tuple
print(tmatch1)

match2 = Match(player3, 2, player4, 7)

round_n1 = Round("Round numero 1", "18-09-2022 12:05:27", 
                 "18-09-2022 15:10:20", [match1, match2])

print(player4.player_name)
print(player4.player_first_name)


tournoi1 = Tournament("tournoi du lion", "Mars", "18-09-2022", "19-09-2022", "blitz", "un super tournoi")tr
print(tournoi1.tournament_name)

tournoi1.save()


print("")
print("")
print("")


tuple = ("lion", "loup", "tigre", "chat")

for i in tuple:
    print(i)
    print(len(i))
    print(i[0])
    print(i[-1])

