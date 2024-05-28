grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

grades = [sum(i) / len(i) for i in grades]
students = sorted(list(students))
stud_dic = {i: j for i,j in zip(students, grades)}

print(stud_dic)