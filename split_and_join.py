str = "Welcome to Python"
print(str.split())

csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'


friends_list = (','.join(','.join(csv.split(';')).split(':'))).split(',')
print(friends_list)
print('replace', csv.replace(';',',').replace(':',',').split(','))