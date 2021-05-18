import json

with open('test.txt', 'r+') as data:
    data.seek(0)
    backup = json.load(data)
    print(backup)
    
player = {
        'hp': 12,
        'inv': ['x','y'],
        'location': 'stairwell'
        }

with open('test.txt', 'w') as data:
    data.seek(0)
    json.dump(player, data, indent=4)
    

    


