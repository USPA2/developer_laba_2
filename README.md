
Функциогнал данного проекта реализован на языке программирования Python.
1) Создание приветствия.
Поприветствуйте пользователя в игре. Спросите у пользователя его имя и поприветствуйте его по имени:
Welcome to the Brain Games!
May I have your name? John
Hello, John!

2) Для проверки и оценки кода был использован Pylint

3) Реализация игры "НОК"
Суть игры в следующем: пользователю показывается три случайных числа, например, 5 7 15. Пользователь вычисляет и вводит наименьшее общее кратное этих чисел.
Вывод получил следующий:

Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
Find the smallest common multiple of given numbers.
Question: 5 7 15
Your answer: 105
Correct!
Question: 100 50 1
Your answer: 100
Correct!
Question: 3 9 27
Your answer: 27
Correct!
Congratulations, Sam!

В случае, если пользователь даст неверный ответ, выводится:
Question: 5 10 25
Your answer: 15
'15' is wrong answer ;(. Correct answer was '25'.
Let's try again, Sam!

4) Реализация игры "Геометическая прогрессия"
Показываем игроку ряд чисел, образующий геометрическую прогрессию, заменив любое из чисел двумя точками. Игрок должен определить это число.
•	Рекомендуемая длина прогрессии – 10 чисел. Длина может генерироваться случайным образом, но должна содержать не менее 5 чисел
•	Позиция спрятанного элемента каждый раз изменяется (выбирается случайным образом)
Пример:


Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
What number is missing in the progression?
Question: 1 2 4 8  .. 32 64 128
Your answer: 16
Correct!
Question: 1 3 9 27 ..
Your answer: 81
Correct!
Question: 5 25 .. 625 3125
Your answer: 125
Correct!
Congratulations, Sam!
В случае, если пользователь даст неверный ответ, выводится:
Question: 4 16 64 .. 1024 4096
Your answer:  1
'1' is wrong answer ;(. Correct answer was '256'.
Let's try again, Sam!

Выполнено:
1. Реализованы две игры
2. Проверьте работоспособность новой игры
3. Проект подключен к сервису по проверке качества кода: www.CodeClimate.com	
4. Общая логика игр выведена в файл cli.py. Логика запуска игр выведена в файл engine.py. Исходный код игр помещен в папку games.Главное в этом задании выполнить рефакторинг, в результате которого общая логика будет н
