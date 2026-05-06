# Создаем списки для хранения данных
names = []
math_scores = []
physics_scores = []
english_scores = []
attendance = []

# Читаем файл
with open("students.csv", "r", encoding="utf-8") as file:
    header = file.readline()  # пропускаем заголовок
    
    for line in file:
        line = line.strip()
        if not line:  # пропускаем пустые строки
            continue
        data = line.split(",")
        
        # Заполняем списки
        names.append(data[0])
        math_scores.append(int(data[1]))
        physics_scores.append(int(data[2]))
        english_scores.append(int(data[3]))
        attendance.append(int(data[4]))

# Проверка на пустой файл
if len(names) == 0:
    print("Файл пуст или не содержит данных!")
    exit()

# средние оценки по предметам
avg_math = sum(math_scores) / len(math_scores)
avg_physics = sum(physics_scores) / len(physics_scores)
avg_english = sum(english_scores) / len(english_scores)

# общая успеваемость каждого студента
total_score = []
for math, phys, eng in zip(math_scores, physics_scores, english_scores):
    student_avg = (math + phys + eng) / 3
    total_score.append(round(student_avg, 1))

# создаем словарь имя -> оценка
students_dict = {}
for i, name in enumerate(names):
    students_dict[name] = total_score[i]

# поиск лучшего и худшего студента (оценка на первом месте!)
data = list(zip(total_score, names))
best_score, best_name = max(data)
worst_score, worst_name = min(data)

# поиск "загадочных" студентов
wonder_students = []
for name, att, score in zip(names, attendance, total_score):
    if att > 90 and score < 80:
        wonder_students.append((name, att, score))

# Запись результатов в файл
with open("analysis.txt", "w", encoding="utf-8") as out_file:
    out_file.write("=== РЕЗУЛЬТАТЫ АНАЛИЗА ===\n\n")
    
    out_file.write("Средние оценки по предметам:\n")
    out_file.write(f"Математика: {avg_math}\n")
    out_file.write(f"Физика: {avg_physics}\n")
    out_file.write(f"Английский: {avg_english}\n\n")
    
    out_file.write("Студенты и их средняя успеваемость:\n")
    for name, score in students_dict.items():
        out_file.write(f"{name}: {score}\n")
    out_file.write("\n")
    
    out_file.write(f"Лучший студент: {best_name} ({best_score})\n")
    out_file.write(f"Худший студент: {worst_name} ({worst_score})\n\n")
    
    out_file.write("=== АНАЛИЗ: Больше 90% посещаемости, но успеваемость < 80 ===\n")
    if wonder_students:
        for name, att, score in wonder_students:
            out_file.write(f"{name} (Посещаемость: {att}, Успеваемость: {score})\n")
    else:
        out_file.write("Таких студентов нет\n")

print("Анализ завершен! Результаты сохранены в analysis.txt")
