Звіт з самостійної роботи №2
Виконала: Бадовська Аріна ТЦР-11
                       ===============================================
                                         ЗАВДАННЯ
                       ===============================================

«Іменний словник українських міст»

Згенеруйте словник, де ключі — назви українських міст, а значення — список найвідоміших людей, що там народились. Реалізуйте пошук по місту, сортування по довжині імен, а також функцію, яка виводить N випадкових постатей з усієї мапи.

                       ===============================================
				                                ПРОЦЕС РОБОТИ
                       ===============================================

1. Створюємо словник, де ключі є назви міст України;
2. Створюємо функцію:
	- приймає на вхід назву міста;
	- перевіряє чи є словником;
	- якщо місто знайдено = виводить відомих людей, якщо ні = виводить помилку
3. Створюємо функцію:
	- Приймає на вхід число n - кількість випадкових постатей, які потрібно вивести.
	- Створює список усі_люди, як і в попередній функції.
	- Перевіряє, чи запитувана кількість n не перевищує загальну кількість відомих людей.
	- Використовує random.sample() для вибору n випадкових унікальних елементів зі списку усі_люди.
	- Виводить список випадкових постатей.

4. Виводимо значення.
                       ===============================================
				                                РЕЗУЛЬТАТ КОДУ
                       ===============================================
Famous people born in Kyiv:
- Mikhail Bulgakov
- Anna Akhmatova
- Igor Sikorsky
- Kazymyr Malevych
Famous people born in Lviv:
- Ivan Franko
- Stanisław Lem
- Solomiya Krushelnytska
City 'Zaporizhzhia' not found in the dictionary.

Famous people, sorted by name length:
- Paul Celan (10 characters)
- Ivan Franko (11 characters)
- Isaac Babel (11 characters)
- Anna German (11 characters)
- Oleh Lysheha (12 characters)
- Igor Sikorsky (13 characters)
- Stanisław Lem (13 characters)
- Leonid Kuchma (13 characters)
- Yuliia Sanina (13 characters)
- Nikolai Gogol (13 characters)
- Anna Akhmatova (14 characters)
- Ilya Mechnikov (14 characters)
- Leonid Utyosov (14 characters)
- Lesya Ukrainka (14 characters)
- Vasyl Virastyuk (15 characters)
- Mikhail Bulgakov (16 characters)
- Kazymyr Malevych (16 characters)
- Helena Blavatsky (16 characters)
- Olha Kobylianska (16 characters)
- Volodymyr Ivasyuk (17 characters)
- Ivan Kotliarevsky (17 characters)
- Hryhoriy Skovoroda (18 characters)
- Lyudmila Gurchenko (18 characters)
- Sofia Andrukhovych (18 characters)
- Solomiya Pavlychko (18 characters)
- Solomiya Krushelnytska (22 characters)

3 random famous figures:
- Ivan Kotliarevsky
- Ilya Mechnikov
- Nikolai Gogol

7 random famous figures:
- Kazymyr Malevych
- Olha Kobylianska
- Nikolai Gogol
- Oleh Lysheha
- Lesya Ukrainka
- Yuliia Sanina
- Leonid Utyosov

20 random famous figures:
- Vasyl Virastyuk
- Volodymyr Ivasyuk
- Helena Blavatsky
- Lesya Ukrainka
- Stanisław Lem
- Solomiya Krushelnytska
- Solomiya Pavlychko
- Kazymyr Malevych
- Oleh Lysheha
- Paul Celan
- Lyudmila Gurchenko
- Isaac Babel
- Ivan Franko
- Anna Akhmatova
- Olha Kobylianska
- Ilya Mechnikov
- Igor Sikorsky
- Leonid Kuchma
- Mikhail Bulgakov
- Leonid Utyosov

                       ===============================================
				                               ПОСИЛАННЯ НА КОД
                       ===============================================

https://github.com/AriSnowie97/Samostiyna_2/blob/main/sr2.py
