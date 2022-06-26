if __name__ == "__main__":
    kebabs = ['meat', 'vegetable', 'falafel']

    for kebab in kebabs:
        if kebab == 'falafel':
            print(kebab.upper())
        else:
            print(kebab.title())

    liked_food = 'chicken tikka masala'

    if liked_food == 'Pasta':
        print("Ew, that's disgusting")
    else:
        print("sheesh")


    age = 70
    if age >= 50:
        print("\nYou are old, you sad sad soul.")
    else:
        print("\nYou are one young bean!")


    nut_mix = ['almonds', 'walnuts', 'peanuts']

    for nut in nut_mix:
        print(f"\nAdding {nut}.")
    print("\nFinished making your nut bowl. Come again to Nut and Co!")


    nutz_mix = ['walnuts', 'peanuts']

    wanted_nuts = ['kebab nut']

    for wanted_nut in wanted_nuts:
        if wanted_nut in nutz_mix:
            print(f"\nAdding {wanted_nut}.")
        else:
            print(f"\n\nSorry, but we don't have your wanted {wanted_nut}.")

    print("\nWe finished making your nut mix. Come again soon.")


    def measure_age(age):
        if age > 70:
            print("\nOLD")
        elif age < 30:
            print("\nYOUNG")
        else:
            print("\nmeduim")

    measure_age(35)
    measure_age(45)
    measure_age(75)
    measure_age(25)