import json

data_base = []

def load():
    global data_base
    with open("student_data_base.json", "r", encoding="utf-8") as fh:
        data_base = json.load(fh)
    print("База учеников была успешно загружена")

def save():
    with open("student_data_base.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(data_base,ensure_ascii=False))
    print("База была успешно сохранена в файле student_data_base.json")

def ent_stud(list):
    ret_msg = f"Инфомация: {list} добавлена в систему."
    flag = True
    for i in range(len(data_base)):
        if data_base[i][0] == list[0] and data_base[i][1] == list[1]:
           ret_msg = f"Ученик {list[0]} {list[1]} уже есть в системе"
           flag = False
           break
    if flag:
        with open("student_data_base.json", "w", encoding="utf-8") as fh:
            data_base.append(list)
            fh.write(json.dumps(data_base,ensure_ascii=False))
    return ret_msg

def dict(text):
    if text == "Дата рождения":
        return 2
    elif text == "Класс":
        return 3
    elif text == "Классный руководитель":
        return 4
    elif text == "Адрес":
        return 5
    elif text == "Телефон родителя":
        return 6
    elif text == "Средняя успеваемость":
        return 7

def edit_stud(list1, list2, list3):
    ret_msg = "Ученик не найден в системе."
    for i in range(len(data_base)):
        if data_base[i][0] == list1[0] and data_base[i][1] == list1[1]:
            for j in range(len(list2)):
                data_base[i][dict(list2[j])] = list3[j]
            save()
            ret_msg = "Информация изменена."
    return ret_msg