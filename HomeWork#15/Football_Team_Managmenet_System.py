

class FootballTeam:
    
    def __init__(self, team_name,coach):
        self.team_name = team_name
        self.coach = coach
        self.players =[]
        

    def adding(self,name,position,number,age,nat):
        self.gamer ={
            "Name":name,
            "Position": position,
            "Number": number,
            "Age": age,
            "Nationality": nat
         }
        if self.gamer not in self.players:
            self.players.append(self.gamer)
        else:
            print("That player is already in list")
        return self.players
    
    def remove(self,num):
        for i in self.players:
            if i["Number"] == num:
                self.players.remove(i)
            else:
                print("There is no player by that number")
        return self.players
    
    def update(self,number,key,value):
        for j in self.players:
            if j["Number"] == number:
                j[key]= value

        return self.players
    
    def team_info(self):
        print(f"Football club: {team.team_name}\nCoach: {team.coach}")
        for g in self.players:
         print(f"{g['Name']} ({g['Position']}), #{g['Number']}, {g['Age']} years old, {g['Nationality']}")
    
    def footballer(self,number):
        for k in self.players:
            if k["Number"]== number:
                return f"Name:{k['Name']}\nPosition:{k["Position"]}\nAge:{k["Age"]}\nNationality:{k["Nationality"]}"
            else:
                print("There is no player by that number")
   

    
team = FootballTeam('Paris Saint-Germain FC','Louis Enrique')
player1=team.adding('Khvicha Kvaratskhelia','Forward',7,24,'Georgian')
player2=team.adding('Ousmane Dembele','Forward',8,28,'French')
player3=team.adding('Desire Doue','Forward',14,20,'French')
player4=team.adding('Fabian Ruiz','Midfielder',9,29,'Spanish')
player5=team.adding('Vitinha','Midfielder',17,25,'Portuguese')
player6=team.adding('Achraf Hakimi','Defender',2,27,'Moroccan')
player7=team.adding('Nuno Mendes','Defender',25,23,'Portuguese')
player8=team.adding('Marquinhos','Defender',5,31,'Brazilian')
player9=team.adding('Ilia Zabarnyi','Defender',6,23,'Ukrainian')
player10=team.adding('Lee Kang-in','Midfielder',19,24,'Korean')
player11=team.adding('Lucas Chevalier','Goalkeeper',30,23,'French')
player12=team.adding('Bradley Barcola','Forward',29,23,'French')

print(team.players)

rem= team.remove(29)

print()

print(team.players)

print()

upd=team.update(7,'goals',15)

print()

print(team.players)

print()

print(team.team_info())

print()

select=team.footballer(7)

print(select)








    

    





      