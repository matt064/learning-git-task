print("Lista zakupów na dzisiaj")
print()

shopping_dict = {
    "piekarnia" : ['chleb', 'bułki', 'pączek'],
    "warzywniak" : ['marchew', 'seler', 'rukola', 'pomidor'],
}

sum = 0

for sklep, produkty in shopping_dict.items():
    print("Ide do " + sklep.title() + ", kupuję tu następujące rzeczy: "  )
    for produkt in produkty:
        print("\t- " + produkt.title())
        sum += 1

print()
print(f"W sumie kupuję {sum} produktów.")






