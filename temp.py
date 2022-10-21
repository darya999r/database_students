# main

# import json

# student_n = [ [0]: Фамилия ученика, 
#               [1]: Имя Отчество ученика, 
#               [2]: дата рождения, 
#               [3]: место жительства, 
#               [4]: телефон, 
#               [5]: класс, 
#               [6]: классный руководитель, 
#               [7]: средняя успеваемость ]

# def save():
#     with open('student_data_base.json', 'w', encoding='utf-8') as sdb:  
#         sdb.write(json.dumps(sdb_local,ensure_ascii=False)) 
#     print('Database saved successfully!')

# def load():
#     students_db = 'student_data_base.json'
#     with open(students_db, 'r', encoding='utf-8') as sdb:
#         sdb_local = json.load(sdb)
#     print('Database loaded successfully!')
#     return sdb_local

# def add():
#     try:
#         info_student = []
#         info_student.append(str(input("Введите Фамилию ученика: ")))
#         info_student.append(str(input("Введите Имя и Отчество ученика: ")))
#         info_student.append(str(input("Введите дату рождения ученика: ")))
#         info_student.append(str(input("Введите место жительства ученика: ")))
#         info_student.append(int(input("Введите телефон ученика: ")))
#         info_student.append(str(input("Введите класс ученика: ")))
#         info_student.append(str(input("Введите ФИО классного руководителя: ")))
#         info_student.append(int(input("Введите среднюю успеваемость ученика\n(2-двоечник, 3-троечник, 4-хорошист, 5-отличник): ")))    
#         return info_student
#     except: print("Input error!")

    
# sdb_local = []
# try: sdb_local = load()
# except: print("Database failed to load!")

# while True:
#     command = input("Enter command: ")
#     if command=='/load':
#         sdb_local = load()
#         print(sdb_local)
#     elif command=='/save':
#         save()
#     elif command=='/add':
#         info_student = add()
#         sdb_local.append(info_student)
#         print("Student data successfully added!")
#     elif command=='/all':
#         print("Фамилия:\tИмяОтчество:\tДата рождения:\tАдрес:\tТелефон:\tКласс:\tКлас.Рук.:\tУспеваемость:")
#         for elem in sdb_local:
#             print("\t".join(map(str,elem)))
#     elif command=='/stop':
#         break
#     else: print("No such command exists!!!")