comeback = ['no u', 'bruh', 'sheesh']
message = f"When he said to me that i am bad, I said to him {comeback[0].title()}."

print(message)

fruits = ['strawberries', 'apples', 'orange,', 'peach']

fruits.append('pear')
fruits.insert(2, 'papaya')

print(fruits)

electronics = ['mouse', 'keyboard', 'laptop', 'desktop', 'headphones']
electronics.sort()
print(electronics)

electronics = ['mouse', 'keyboard', 'laptop', 'desktop', 'headphones']
electronics.sort(reverse=True)
print(electronics)


electronics = ['mouse', 'keyboard', 'laptop', 'desktop', 'headphones']
x = len(electronics)
print(x)


# Chapter 4


vegetables = ['brussel', 'spinach', 'tomato']
for vegetable in vegetables:
    print(f"{vegetable.title()} tastes bad!")

mult = []
for value in range(1, 102):
    kebab = value ** 2
    mult.append(kebab)

print(mult)

minecrafters = ['Wyndsor', 'Vivaan', 'Bar', 'Isaac', 'Jaemin', 'Taejin']

print("These are the best minecraft players in the entire world:")
for minecrafter in minecrafters[:1]:
    print(minecrafters)


measures = (30, 19)
for measure in measures:
    print(measure)


measures = (30, 19)
print("\nOld measures:")
for measure in measures:
    print(measure)

measures = (200, 50)
print("\nModified measures:")
for measure in measures:
        print(measure)


def switch_a_list(electronics):
    electronics.sort(reverse=True)
    return electronics

if __name__ == "__main__":
    print(switch_a_list(['mouse', 'keyboard', 'laptop', 'desktop', 'headphones']))




