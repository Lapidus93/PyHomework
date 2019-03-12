import json
from dateutil import parser

###Инициализирую классы все три класса

#Класс команды
class Team(object):
    
    def __init__(self,id,name,players):
       
        self.id = id
        self.name = name
        self.players = players
        

    def present(self):
        players = []
        for pl in players_obj:
            if pl.team == self.id:
                players.append(pl)
        print(self.id, 'Команда:',self.name)
        print('Игроки:')
        for i in players:
            print(i.id,i.name)

            
#Класс игроки
class Player(object):
    
    def __init__(self,id,name,team):

        self.id = id
        self.name = name
        self.team = team

#Метод представления игрока

    def present(self):
        team_name = 0
        for team in teams_obj:
            if team.id == self.team:
                team_name = team.name

        print('id:', self.id,'Имя:',self.name, 'играет в команде', team_name)
        

#Класс матчи
class Match(object):
    
    def __init__(self,id,date,location,result,team1,team2):
       
        self.id = id
        self.date = date
        self.location = location
        self.result =result
        self.team1 =team1
        self.team2 = team2

    #Метод отображает матч в читабельном виде
    def present(self):
        team1 = 0
        team2 = 0
        for tm in teams_obj:
            if tm.id == self.team1:
                team1 = tm.name
            if tm.id == self.team2:
                team2 = tm.name

        print('Матч №:',self.id)
        print('Был сыгран', self.date,'На стадионе', self.location)
        print('c результатом', team1, self.result, team2)

    def present_players(self):
        team_1players = 0
        team_1name = 0
        team_2players = 0
        team_2name = 0

        for tm in teams_obj:
            if tm.id == self.team1:
                team_1name = tm.name
                team_1players = tm.players
            if tm.id == self.team2:
                team_2name = tm.name
                team_2players = tm.players

        print('За', team_1name,'играли:')
        for i in team_1players:
            for pl in players_obj:
                if i == pl.id:
                    print(pl.id,pl.name)

        print('За', team_2name,'играли:')
        print('')
        for i in team_2players:
            for pl in players_obj:
                if i == pl.id:
                    print(pl.id,pl.name)
            
                    
## Выгрузка игроков из файла и преобразование их в объект players
spis_players = []
with open('players.txt') as text:
    js = text.readlines()
    for i in js:
        pl = json.loads(i)
        spis_players.append(pl)

players_obj = []
for i in spis_players:
    pl_obj = Player(i['id'],i['name'],i['team'])
    players_obj.append(pl_obj)
    
# Выгрузка команд из файла и преобразование их в объект Teams
teams_list = []
with open('teams.txt') as text:
    js = text.readlines()
    for i in js:
        pl = json.loads(i)
        teams_list.append(pl)

teams_obj = []
for i in teams_list:
    tm_obj = Team(i['id'],i['name'],i['players'])
    teams_obj.append(tm_obj)

    
# Выгрузка матчей из файла и преобразование их в объект Matches
spis_matches = []
with open('matches.txt') as text:
    js = text.readlines()
    for i in js:
        mt = json.loads(i)
        spis_matches.append(mt)

matches_obj = []
for i in spis_matches:
    mt_obj = Match(i['id'],parser.parse(i['date']),i['location'],i['result'],i['team1'],i['team2'])
    matches_obj.append(mt_obj)

# Функция сохранения команды.
def save_teams():
    with open('teams.txt', 'w') as text:
        for team in teams_obj:
            team_dic = {'id':team.id,'name':team.name,'players':team.players}
            js = json.dumps(team_dic)
            text.write(js)
            text.write('\n')

            
while True:

    print('''

    Доброе пожаловать в "FIFA RB MANAGER" 2020

    ГЛАВНОЕ МЕНЮ

    1. Перейти в "Создание объектов"
    2. Поиск Матчей
    3. Поиск Команд
    4. Поиск Игроков
    5. Выход из FIFA менеджера

    ''')

    action = input()
    if action == '1':
        while True:

            print('''
            CОЗДАНИЕ ОБЪЕКТОВ

            1. Создать команду
            2. Создать игрока
            3. Выйти в главное меню

            ''')
            action2 = input()
            if action2 == '1':
                print('СОЗДАТЬ КОМАНДУ')
                while True:
                    team_name = input('Введите название команды или "выход", чтобы выйти')
                    if team_name == 'выход':
                        break
                    else:
                        new_team_id = teams_obj[-1].id + 1
                        new_team = Team(new_team_id,team_name,[])
                        teams_obj.append(new_team)
                        print('Команда {} создана'.format(team_name))
                        break
               
            if action2 == '2':

                print('СОЗДАТЬ ИГРОКА')
                while True:
                    player_name = input('Введите имя игрока или "выход", чтобы выйти')
                    if player_name == 'выход':
                        break
                    else:
                        new_player_id = players_obj[-1].id + 1
                        teams_id = int(input('Введите № команды игрока'))
                        new_player = Player(new_player_id,player_name,teams_id)
                        players_obj.append(new_player)
                        for tm in teams_obj:
                            if tm.id == new_player.team:
                                tm.players.append(new_player.id)

                        break
                
                
                
            if action2 == '3':
                break

    elif action == '2':

        while True:

            print('''
            МАТЧИ (ПОИСК)

            1. Поиск по id матча
            2. Поиск матча по датам
            3. Поиск матча по стадиону
            4. Поиск матча имени команды
            5. Показать все матчи
            6. Выйти в главное меню

            ''')
            action2 = input()
            if action2 == '1':
                print('ПОИСК ПО ID МАТЧА')
                while True:
                    id_matcha = input('Введите id матча или "выход", чтобы выйти в главное меню')
                    if id_matcha == 'выход':
                        break
                    else:
                        for match in matches_obj:
                            if match.id == int(id_matcha):
                                match.present_players()
       
            if action2 == '2':
                print('ПОИСК МАТЧА ПО ДАТАМ')
                while True:
                    print('''
                    1. Искать матч по дате
                    2. Искать матч в диапазоне дат
                    3. Выйти в главное меню
                    ''')
                    act2 = input()
                    if act2 == '1':
                        while True:
                            mes = input('Введите номер месяца или "выход", чтобы выйти')
                            if mes == 'выход':
                                break
                            else:
                                dat = parser.parse("2018-{}-{} 19:00:00".format(mes,input('введи день')))
                                for i in matches_obj:
                                    if i.date == dat:
                                        i.present()
                                        i.present_players()

                    if act2 == '2':
                        while True:
                            check = input('Нажмите "Enter", чтобы продолжить и "выход", чтобы выйти')
                            if check == 'выход':
                                break
                            else:
                                dat1 = parser.parse("2018-{}-{} 19:00:00".format(input('введи месяц начала диапазона'),input('введи день начала диапазона')))
                                dat2 = parser.parse("2018-{}-{} 19:00:00".format(input('введи месяц конца диапазона'),input('введи день начала диапазона')))
                                for i in matches_obj:
                                    if  dat1 < i.date < dat2:
                                        i.present()

                    if act2 == '3':
                        break

                                
                                

            if action2 == '3':
                print('ПОИСК ПО СТАДИОНУ')
                while True:
                    stadion = input('Введите название стадиона или "выход", чтобы выйти в главное меню')
                    if stadion == 'выход':
                        break
                    else:
                        for i in matches_obj:
                            if i.location == stadion:
                                i.present()

            if action2 == '4':
                print('ПОИСК ПО ИМЕНИ КОМАНДЫ')
                while True:
                    komanda = input('Введите название команды или "выход", чтобы выйти в главное меню')
                    if komanda == 'выход':
                        break
                    else:
                        for tm in teams_obj:
                            if komanda == tm.name:
                                for match in matches_obj:
                                    if tm.id == match.team1:
                                        match.present()
                                    elif tm.id == match.team2:
                                        match.present()

            if action2 == '5':
                for i in matches_obj:
                    i.present()
                                        
            if action2 == '6':
                break


                
    elif action == '3':

        while True:

            print('''
            КОМАНДЫ

            1. Показать все команды 
            2. Поиск по id команды
            3. Поиск по названию команды
            4. Поиск команды по игроку
            5. Выход в главное меню

            ''')
            action2 = input()

            if action2 == '1':
                for i in teams_obj:
                    print(i.id,i.name)

            if action2 == '2':
                print('ПОИСК ПО ID КОМАНДЫ')
                while True:
                    id_team = input('Введите id команды или "выход", чтобы выйти в главное меню')
                    if id_team == 'выход':
                        break
                    else:
                        team = 0
                        for team in teams_obj:
                            if team.id == int(id_team):
                                team.present()

            if action2 == '3':
                print('ПОИСК ПО НАЗВАНИЮ КОМАНДЫ')
                while True:
                    komanda = input('Введите название команды или "выход", чтобы выйти в главное меню')
                    if komanda == 'выход':
                        break
                    else:
                        for tm in teams_obj:
                            if komanda == tm.name:
                                tm.present()
                                
            if action2 == '4':
                print('ПОИСК КОМАНДЫ ПО ИГРОКУ')
                while True:
                    id_player = input('Введите номер игрока или "выход", чтобы выйти в главное меню')
                    if id_player == 'выход':
                        break
                    else:
                        for team in teams_obj:
                            if int(id_player) in team.players:
                                print(team.id, team.name)
                
                
            if action2 == '5':
                break


    elif action == '4':

        while True:

            print('''
            ИГРОКИ (ПОИСК)

            1. Показать всех игроков
            2. Поиск игрока по id
            3. Поиск по имени игрока
            4. Поиск игроков по названию команды
            5. Поиск игроков по номеру матча
            6. Выйти в главное меню

            ''')
            action2 = input()
            if action2 == '1':
                print('ПОКАЗАТЬ ВСЕХ ИГРОКОВ')
                for pl in players_obj:
                    pl.present()

            if action2 == '2':
                print('ПОИСК ИГРОКА ПО ID')
                while True:
                    id_player = input('Введите id номер игрока или "выход", чтобы выйти в главное меню')
                    if id_player == 'выход':
                        break
                    else:
                        for pl in players_obj:
                            if int(id_player) == pl.id:
                                pl.present()

            if action2 == '3':
                print('ПОИСК ИГРОКА ПО ЕГО ИМЕНИ')
                while True:
                    player_name = input('Введите имя игрока или "выход", чтобы выйти в главное меню')
                    if player_name == 'выход':
                        break
                    else:
                        for pl in players_obj:
                            if player_name in pl.name:
                                pl.present()
                                
            if action2 == '4':
                print('ПОИСК ИГРОКОВ ПО НАЗВАНИЮ КОМАНДЫ')
                while True:
                    komanda = input('Введите название команды или "выход", чтобы выйти в главное меню')
                    if komanda == 'выход':
                        break
                    else:
                        for tm in teams_obj:
                            if komanda == tm.name:
                                tm.present()

            if action2 == '5':
                print('ПОИСК ИГРОКОВ ПО ID МАТЧА')
                while True:
                    id_matcha = input('Введите id матча или "выход", чтобы выйти в главное меню')
                    if id_matcha == 'выход':
                        break
                    else:
                        for match in matches_obj:
                            if match.id == int(id_matcha):
                                match.present_players()

                                
                                
            if action2 == '6':
                break
                
    elif action == '5':
        break

with open('teams.txt', 'w') as text:
    for team in teams_obj:
        team_dic = {'id':team.id,'name':team.name,'players':team.players}
        js = json.dumps(team_dic)
        text.write(js)
        text.write('\n')

with open('players.txt', 'w') as text:
    for pl in players_obj:
        player_dic = {'id':pl.id,'name':pl.name,'team':pl.team}
        js = json.dumps(player_dic)
        text.write(js)
        text.write('\n')

        
print('FIFA менеджер закрыт')