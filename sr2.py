import random #для генерації випадкових значень

ukrainian_cities = {
    "Kyiv": ["Mikhail Bulgakov", "Anna Akhmatova", "Igor Sikorsky", "Kazymyr Malevych"],
    "Lviv": ["Ivan Franko", "Stanisław Lem", "Solomiya Krushelnytska"],
    "Kharkiv": ["Hryhoriy Skovoroda", "Ilya Mechnikov", "Lyudmila Gurchenko"],
    "Odesa": ["Isaac Babel", "Anna German", "Leonid Utyosov"],
    "Dnipro": ["Helena Blavatsky", "Leonid Kuchma", "Yuliia Sanina"],
    "Chernivtsi": ["Paul Celan", "Olha Kobylianska", "Volodymyr Ivasyuk"],
    "Ivano-Frankivsk": ["Vasyl Virastyuk", "Sofia Andrukhovych"],
    "Ternopil": ["Solomiya Pavlychko", "Oleh Lysheha"],
    "Lutsk": ["Lesya Ukrainka"],
    "Poltava": ["Nikolai Gogol", "Ivan Kotliarevsky"],
} #словник з містами України та відомими людьми

def search_by_city(city):
    """Finds famous people by city name."""
    if city in ukrainian_cities:
        print(f"Famous people born in {city}:")
        for person in ukrainian_cities[city]:
            print(f"- {person}")
    else:
        print(f"City '{city}' not found in the dictionary.")
        #функція для пошуку відомих людей за назвою міста
        #якщо місто не знайдено, виводимо повідомлення

def sort_by_name_length():
    """Outputs all famous people, sorted by the length of their names."""
    all_people = []
    for city in ukrainian_cities:
        all_people.extend(ukrainian_cities[city])
#функція для виведення всіх відомих людей, відсортованих за довжиною їхніх імен
    #всі відомі люди з усіх міст
    sorted_people = sorted(all_people, key=len)
    print("\nFamous people, sorted by name length:")
    for person in sorted_people:
        print(f"- {person} ({len(person)} characters)")
#виводимо відомих людей, відсортованих за довжиною їхніх імен
def random_figures(n):
    """Outputs N random famous figures from the entire map."""
    all_people = []
    for city in ukrainian_cities:
        all_people.extend(ukrainian_cities[city])

    if n > len(all_people):
        print(f"Request for {n} figures, but only {len(all_people)} found in total.")
        count = len(all_people)
    else:
        count = n

    random_selection = random.sample(all_people, count)
    print(f"\n{count} random famous figures:")
    for figure in random_selection:
        print(f"- {figure}")

#виводимо N випадкових відомих людей з усієї карти
search_by_city("Kyiv")
search_by_city("Lviv")
search_by_city("Zaporizhzhia")
#виводимо відомих людей за назвою міста
sort_by_name_length()
#виводимо всіх відомих людей, відсортованих за довжиною їхніх імен
random_figures(3)
random_figures(7)
random_figures(20)