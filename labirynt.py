import time
print("░Labirynt░")

rooms = {
    'Start': {'rooms': ['Room_1'], 'items':[]},
    'Room_1': {'rooms': ['Start', 'Room_2', 'Room_3'], 'items':[]},
    'Room_2': {'rooms': ['Room_1', 'Room_4'], 'items':[]},
    'Room_3': {'rooms': ['Room_1', 'Room_5'], 'items':[]},
    'Room_4': {'rooms': ["Room_2", 'Room_6', 'Room_7'], 'items': []},
    'Room_5': {'rooms': [], 'items':[]},
    'Room_6':{'rooms': ["Room_4", "Room_8", "Room_9"],'items':["shotgun"]},
    'Room_7':{'rooms': ['Room_4','Room_10',"Room_9"], 'items':[]},
    'Room_8':{'rooms': ["Room_6","Room_11","Room_12"], 'items':[]},
    'Room_9':{'rooms': ["Room_6", "Room_13", "Room_14"], 'items':[]},
    'Room_10':{'rooms': ["Room_7", "Room_12", "Room_13"], 'items':[]},
    'Room_11':{'rooms': ["Room_8", "Room_13", "Room_14"], 'items':[]},
    'Room_12':{'rooms': ["Room_10","Room_13", "Room_14" ], 'items':[]},
    'Room_13':{'rooms': [], 'items':[]},
    'Room_14':{'rooms': ["Room_9",'Room_11','Room_12','Exit'], 'items':["key"], "enemy":["monster"]},
    'Exit':{'rooms': [], 'items':["prize"]}
}
room = 'Start'
prize = True
monster = True
shotgun = False
key = False
while True:
    print('============================')
    print('Jesteś w pokoju', room)
    for near_room in rooms[room]['rooms']:
        print('Możesz iść do pokoju', near_room)
        
    new_room = input('Który pokój wybierzesz? ')
    if new_room not in rooms[room]['rooms']:
        print('Nie możesz przemeścić się do takie pokuju od razu')
        time.sleep(2)
        continue
    
    if new_room == 'Exit' and prize:
        print('Dostałeś "Puchar za przejście labiryntu"')
        time.sleep(2)
        break
    if new_room == "Room_5" and "Room_13":
        print("Trafiłeś płupkę")
        break
    
    
    room = new_room
    if 'key' in rooms[room]['items']:
        key=True
        print('Znalazłeś klucz')
        rooms[room]['items'].remove('key')
        time.sleep(2)
        continue
    if new_room == 'Room_14' and monter and not shotgun:
        print('Przed tobą stoi straszny stwór, nie daje przejścia, jak go stąt zabrać? Wiem! Shotgunem! ')
        time.sleep(2)
        continue
    if new_room == 'Room_14' and monter and shotgun:
        monsterr=False
        print("Zabiłeś potwora i....")
        time.sleep(1)
    if 'shotgun' in rooms[room]['items']:
        shotgun=True
        print('Znalazłeś shotgun')
        rooms[room]['items'].remove('shotgun')
        time.sleep(2)
        continue
