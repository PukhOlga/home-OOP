
#hare_all = 0 # подсчитайте общую дистанцию зайца

#hare=0

#for hare in hare_distances:
#    print(hare)
    #turtle_all = 0 # подсчитайте общую дистанцию черепахи
    #for ...
    #...
    # определите, кто из двоих прошел бОльшую дистанцию

'''hare_distances = [8, 5, 3, 2, 0, 1, 1]
turtle_distances = [3, 3, 3, 3, 3, 3, 3]
hare_all=0
turtle_all=0
for x in hare_distances:
  hare_all=hare_all+x
for x in turtle_distances:
  turtle_all=turtle_all+x

if turtle_all > hare_all:
    result = "черепаха"
elif hare_all > turtle_all:
    result = "заяц"
else:
    result = "одинаково"
print(result)'''
'''todo_list = [
    ["Разобрать почту", 1],
    ["Обзвонить клиентов", 2],
    ["Запланировать дела на завтра", 0.6],
    ["Сделать презентацию", 3],
    ["Созвон с командой", 0.5]
]

worktime = 0.0
workday = 8.0

for todo in todo_list:  # посчитайте в цикле сумму рабочего времени и сохраните в переменную worktime
    worktime+=todo[1]
    print(worktime)
print(round(workday - worktime, 1))'''
'''
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
#boys = ['Peter', 'Alex', 'John', 'Arthur', 'Sichard']
#girls = ['Kate', 'Liza', 'Kira', 'Emma']
result = ""
new_pair = []
#Girls=sorted(girls)
#print(Girls)
#pair = zip(sorted(boys), sorted(girls))
#print(list(pair))
if len(girls)==len(boys):  # проверьте, что длины списков одинаковы
    """for pair in zip(sorted(boys), sorted(girls)):  # отсортируйте пары, объедините при помощи zip и распакуйте в цикле
        #new_pair.append(pair[0] + " и " + pair[1])
        #new_pair = int(f"{pair[0]} и {pair[1]}")
        result += pair[0] + " и " + pair[1]+", """
    for boy, girl in zip(sorted(boys), sorted(girls)):
        result+=boy + " и " + girl + ", "
    result = result[:-2]
    print(result)
else:
    result = "Кто-то может остаться без пары!"
    print(result)
'''


'''def solve(phrases: list):
    result = [] # список палиндромов
    for phrase in phrases: # пройдите циклом по всем фразам
        ... # сохраните фразу без пробелов
        if ... # сравните фразу с ней же, развернутой наоборот (через [::-1])
           result.append(phrase)
    return result

if __name__ == '__main__':
    # Этот код менять не нужно
    phrases = ["нажал кабан на баклажан", "дом как комод", "рвал дед лавр", "азот калий и лактоза",
               "а собака боса", "тонет енот", "карман мрак", "пуст суп"]
    result = solve(phrases)
    assert result == ["нажал кабан на баклажан", "рвал дед лавр", "азот калий и лактоза",
               "а собака боса", "тонет енот", "пуст суп"], f"Неверный результат: {result}"
    print(f"Палиндромы: {result}")'''

#str = ' Привет, мир! '
#str = str.replace(' ', '')
#print(str)
'''
phrases = [
           "нажал кабан на баклажан",
           "дом как комод",
           "рвал дед лавр",
           "азот калий и лактоза",
           "а собака боса",
           "тонет енот",
           "карман мрак",
           "пуст суп"
]

result = []  # список палиндромов
for phrase in phrases:  # пройдите циклом по всем фразам
    str = phrase.replace(' ', '')
    if str==phrase.replace(' ', '')[::-1]:  # сравните фразу с ней же, развернутой наоборот (через [::-1])
        print(str)
        result.append(phrase)
print(result)
#str = phrases[0].replace(' ', '')
#print(str)'''

'''
cook_book = [
  ['Салат',
      [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],
      ]
  ],
  ['Пицца',
      [
        ['сыр', 50, 'гр.'],
        ['томаты', 50, 'гр.'],
        ['тесто', 100, 'гр.'],
        ['бекон', 30, 'гр.'],
        ['колбаса', 30, 'гр.'],
        ['грибы', 20, 'гр.'],
      ],
  ],
  ['Фруктовый десерт',
      [
        ['хурма', 60, 'гр.'],
        ['киви', 60, 'гр.'],
        ['творог', 60, 'гр.'],
        ['сахар', 10, 'гр.'],
        ['мед', 50, 'мл.'],
      ]
  ]
]

#rint(cook_book[0][0])
#print(len(cook_book))
#i=0

bluds = []

#bluds=cook_book[0][1]
#bluds.append(cook_book[1][1])
#bluds.append(cook_book[2][1])
#print(bluds[0][0])
for i in range(len(cook_book)):
    bluds.append(cook_book[i][1])

print(bluds[1][0][0])
'''



'''# Добавьте в список всех преподавателей со всех курсов
all_list = []
#print(mentors[0])
for m in mentors:
   all_list.extend(m)
    #for name in m:
    #all_list.append(name)
    #print(m)
print(all_list)
all_names_list = []
for name in all_list:
    all_names_list.append(name.split()[0])
print(all_names_list)
unique_names = set(all_names_list)
print(unique_names)
all_names_sorted = sorted(list(unique_names))
print(all_names_sorted)
all_names_sorted = ", ".join(all_names_sorted)
print(f'Уникальные имена преподавателей: {all_names_sorted}')
#print(all_list[0].split())'''
'''
all_list = []
popular = []
for m in mentors:
   all_list.extend(m)
all_names_list = []
for name in all_list:
    all_names_list.append(name.split()[0])
unique_names = set(all_names_list)
for name in unique_names:
    sum = all_names_list.count(name)
    popular.append([name, sum])
popular.sort(key=lambda x:x[1], reverse=True)
top_3=popular[:3]
print(top_3)
new_top=''
for name in top_3:
    new_top += (f"{name[0]}: {name[1]}, ")
print(new_top[:-2])
#print(unique_names)

# Подсчитайте встречаемость каждого имени через list.count()
popular = []
for name in unique_names:
	popular.append([name, ...]) # Добавьте подсчёт имён

# Это код для сортировки списка с элементами вида [имя, количество] по убыванию встречаемости
# Используйте его, как есть, или напишите собственный :)
popular.sort(key=lambda x:x[1], reverse=True)

# Получите топ-3 часто встречающихся имён из списка popular
# Подсказка: возьмите срез списка
top_3 = popular[...]'''


"""
a = [[2, 4, 6, 8],
     [1, 3, 5, 7],
     [8, 6, 4, 2],
     [7, 5, 3, 1]]

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")
    print()"""

"""professions = ['IT', 'Изобразительное искусство', 'Музыка', 'Наука']
persons = [
    ['Гейтс (Microsoft)', 'Джобс (Apple)', 'Возняк (Apple)', 'Торвальдс (Linux)'],
    ['Пикассо (художник)', 'Моне (художник)', 'Ван Гог (художник)', 'Дали (художник)'],
    ['Моцарт (композитор)', 'Бах (композитор)', 'Бетховен (композитор)', 'Шопен (композитор)'],
    ['Эйнштейн (физика)', 'Тесла (физика)', 'Кюри (химия)', 'Хокинг (астрофизика)']
]

for pro, names in zip(professions, persons):
    print(f'{pro}:')
    for name in names:
        print(name)
    print()
for pro, names in zip(professions, persons):
    print(f'{pro}:')
    print("\n".join(names))
    print()"""
'''
courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python",
           "Frontend-разработчик с нуля"]

mentors = [
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
mentors_names = []
#for name, fam in zip(mentors, courses):
for m in mentors:
    course_name = []
    for name in m:
        course_name.append(name.split()[0])
    mentors_names.append(course_name)


# Храните здесь пары курсов, в которых есть совпавшие имена
pairs = []
# # Попарное сравнение "наборов" преподавателей на курсах. Каждую новую пару запоминаем для исключения повторов.
for id1 in range(len(mentors_names)):
    for id2 in range(len(mentors_names)):
        if id1==id2:
            continue
        intersection_set = set(mentors_names[id1]) & set(mentors_names[id2])
        if len(intersection_set) > 0:
            pair = courses[id1] + courses[id2]
            pair1 = courses[id2] + courses[id1]
            if pair not in pairs and pair1 not in pairs:
                pairs.append(pair)
                all_names_sorted = sorted(intersection_set)
                print(f"На курсах '{courses[id1]}' и '{courses[id2]}' преподают: {', '.join(all_names_sorted)}")'''
side1=10
side2=1
side3=-100


"""if side1 <= 0 or side2 <= 0 or side3 <= 0 or side1 + side2 < side3 or side2 + side3 < side1 or side3 + side1 < side2: # условие, что треугольник существует
    print("Треугольник не существует")
elif side1==side2 and side2==side3 and side1==side3: # условие, что треугольник равносторонний
    print("Равносторонний треугольник")
elif (side1==side2 and side3!=side2) or (side1==side3 and side3!=side2) or (side3==side2 and side3!=side1): # условие, что треугольник равнобедренный
    print("Равнобедренный треугольник")
else:
    print("Разносторонний треугольник")"""


if side1 <= 0 or side2 <= 0 or side3 <= 0 or (side1 + side2) < side3 or (side2 + side3) < side1 or (side3 + side1) < side2: # условие, что треугольник существует
    print("Треугольник не существует")
elif side1 == side2 and side2 == side3 and side3==side1: # условие, что треугольник равносторонний
    print("Равносторонний треугольник")
elif (side1 == side2 and side1!=side3) or (side1==side3 and side1!=side2) or (side3==side2 and side1!=side3): # условие, что треугольник равнобедренный
    print("Равнобедренный треугольник")
else: # во всех остальных случаях треугольник разносторонний
    print("Разносторонний треугольник")


////////////////////////

courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]

mentors = [
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов",
	 "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко",
	 "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]

codes_info = [
	"",
	"1 — число цели, которая проявляется в форме агрессивности и амбиций",
	"2 — число равновесия и контраста одновременно, поддерживает равновесие, смешивая позитивные и негативные качества",
	"3 — неустойчивость, объединяет талант и весёлость, символ приспосабливаемости",
	"4 — означает устойчивость и прочность",
	"5 — символизирует риск, свободу и душевное беспокойство, которое толкает человека к путешествиям и новому опыту. С одной стороны, это самое счастливое число, с другой — самое непредсказуемое",
	"6 — символ надёжности. Идеальное число, которое делится как на чётное, так и на нечётное, объединяя элементы каждого",
	"7 — символизирует тайну, а также изучение и знание как путь исследования неизвестного и невидимого",
	"8 — число материального успеха, означает надёжность, доведённую до совершенства, символ всеобщего успеха",
	"9 — указывает на сильную личность с потенциальным интеллектом, способную к высокому развитию"
]
# Здесь ничего менять не нужно, это готовый код, который считает число имени
def calc_namecode(name):
	letters = ["", "А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т",
			   "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]

	name = name.upper()
	code = 0
	for letter in name:
		try:
			ltr_code = letters.index(letter) % 9
		except:
			continue
		if ltr_code == 0:
			ltr_code = 9
		code += ltr_code

	while code > 9:
		curr = code // 10 + code % 10
		code = curr

	return code

# Добавьте сюда ваш код из Задачи 1
all_list = []
for m in mentors:
	all_list.extend(m)

all_names_list = []
for mentor in all_list:
	all_names_list.append(mentor.split()[0])
unique_names = set(all_names_list)


names_codes = [[] for n in range(10)]



for name in unique_names:

	code = calc_namecode(name)


	names_codes[code].append(name)


for id, name in enumerate(names_codes):

	print(codes_info[id])

	all_names_sorted = sorted(names_codes[id])

	if id==0:
		continue
	print(f"Коду {id} соответствуют: {', '.join(all_names_sorted)}")

# Черновик

for course in courses_list:
	for name in unique_names_sort:
		count = 0
		for mentor in course["mentors"]:
			if name in mentor:
				count = count+1
				if count > 1 and mentor not in same_name_list:
					#print(count, name)
					same_name_list.append(mentor)