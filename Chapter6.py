if __name__ == "__main__":
    nut_mix = {'brown': 'almonds', 'white': 'cashew'}

    new_mix = nut_mix['white']
    print(f"\nYou just ate 10 {new_mix} nuts")

    life = {'gamer': 'toxic'}
    print(f"\nThis person is very {life['gamer']}.")

    life['gamer'] = 'calm'
    print(f"\tThe person is now pretty {life['gamer']}.")

    color = {'rice': 'white', 'corn': 'yellow'}
    print(color)

    del color['rice']
    print(color)

    favorite_food = {
        'viv': 'chicken',
        'dad': 'burger',
    }
    for name, food in favorite_food.items():
        print(f"{name.title()}'s favorite food is {food.title()}.")

    favorite_food = {
        'viv': 'chicken',
        'dad': 'burger',
    }

if 'mom' not in favorite_food.keys():
    print("\n\tMom, what's your favorite food?")
    

sandwich = {
    'bread': 'white',
    'lettuce': ['romaine', 'butter crunch']
    }

print(f"You ordered a {sandwich['bread']}-bread sandwich with the following greens:")
for green in sandwich['lettuce']:
    print(f'\t{green}')