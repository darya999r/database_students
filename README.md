### Задача: Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы. Обязательно наличие внешнего хранилища информации в виде или текстового файла или файла .json.

# Информационная система по работе с учениками школы:

## Архитектура информационной системы:
## 1. Модуль графического интерфейса взаимодействия с пользователем
## 2. Модуль обработки информации
## 3. База данных учеников

![img_1](img\img_1.jpg)

Наполнение базы данных по ученикам (файл .json):
1. ФИО
2. Дата рождения
3. Класс
4. ФИО классного руководителя
5. Адрес
6. Номер телефона родителя
7. Средняя успеваемость

Графичкский интерфейс выполнен через библиотеку easygui.

![img_1](img\img_2.jpg)

Функции информационной системы:
1. Добавить ученика в БД

![img_1](img\img_3.jpg)
![img_1](img\img_4.jpg)
2. Удалить ученика из БД

![img_1](img\img_5.jpg)

3. Редактировать данные ученика в БД

![img_1](img\img_6.jpg)
![img_1](img\img_7.jpg)

4. Вывести список учеников конкретного класса

![img_1](img\img_8.jpg)
![img_1](img\img_9.jpg)
![img_1](img\img_10.jpg)
![img_1](img\img_11.jpg)

5. Вывести информацию одного ученика по его фамилии

![img_1](img\img_12.jpg)
![img_1](img\img_13.jpg)

6. Вывести ФИО классного раководителя по фамилии ученика

![img_1](img\img_14.jpg)
![img_1](img\img_15.jpg)

7. Вывести номер телефона родителя по фамилии ученика

![img_1](img\img_16.jpg)
![img_1](img\img_17.jpg)

8. Вывести список именинников месяца по школе (можно вводить как численное значение месяца, так и название)

![img_1](img\img_18.jpg)

9. Вывести списки отличников, хорошистов и ударников школы

![img_1](img\img_21.jpg)
![img_1](img\img_22.jpg)

Work team:
1. Корчагин Дмитрий - control.py; main.py
2. Соловьев Ярослав - control.py; main.py
3. Нестерова Дарья - student_data_base.json; README.md
