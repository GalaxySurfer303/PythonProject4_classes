'''
class Player():
    #points = 0

def show_points(self):
    print(f'Player has {self.points}')


def player_points_earned(self, other):
    print(f'Tyle powinno być {self.points}, oraz {other}')


player = Player()
#player.points = '0'
#player.points = player.points + 1
player.show_points()
player.player_points_earned('dupa')
'''


'''
---------------------------------------------
obiekt, funkcje, arg, wiedza
---------------------------------------------
class User():
    def cheer(self, player_number):
        print(f'Cześć jestem graczem nr. {player_number} i mam na imię {self.name}')

    def cheer_two(self, player_number, player_level ):
        print(f'Cześć {self.name} o numerze gracza {player_number} twoj poziom zaawansowania to: {player_level} ')

user = User()
user.name = 'TurboPączek'
user.cheer('7')
user.cheer_two('7', 'Advanced')
'''
'''
class Samochod:
    def __init__(self, marka, model, rok):
        self.marka = marka  # Inicjalizowanie atrybutu 'marka'
        self.model = model  # Inicjalizowanie atrybutu 'model'
        self.rok = rok      # Inicjalizowanie atrybutu 'rok'

    def pokaz_informacje(self):
        print(f'Samochód: {self.marka} {self.model}, rok produkcji: {self.rok}')

# Tworzenie obiektu klasy Samochod
moje_auto = Samochod('BMW', 'X5', 2020)

# Wywołanie metody pokazującej informacje o samochodzie
moje_auto.pokaz_informacje()


List1: list[str] = ['skull', 'bone', 'parrot', 'captain_hat', 'hack_arm', 'wood_leg', 'single_eye_cover', 'gold', 'pistol', 'chest', 'ship', 'skull_flag']

#print(List1)

List1.append('gold')

print(List1)

remove_from_list = List1.pop()
#print(remove_from_list)
#print(List1)

#print(List1[10])

list_elements = (List1[3], List1[4])
list_elements1 = (List1[7], List1[9])

print(f'\n{list_elements} + {list_elements1}')
'''


FruitList1: list[str] = ['apple', 'orange', 'lemon', 'grapefruit', 'banana',
                         'passion_fruit', 'kivi', 'dragon_fruit', 'figa',
                         'cranberies', 'bluberies', 'jack_fruit', 'mandarine',
                         'melon', 'watermelon', 'papaya', 'pomegranate',
                         'raspberries', 'berries', 'camu_camu', 'pear']

print(FruitList1[::2])  #wyswietla co 2 pozycje
print(FruitList1[::-2]) #co drugie od konca

print(FruitList1[-1])
print(FruitList1[20])
print(FruitList1[-2])
