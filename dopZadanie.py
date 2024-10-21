# Средний балл

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

sorted_students = list(sorted(students))
print(sorted_students)

for_Aaron = grades.pop(0)
sumIlenOfAaron = sum(for_Aaron) / len(for_Aaron)

for_Bilbo = grades.pop(0)
sumIlenOfBilbo = sum(for_Bilbo) / len(for_Bilbo)

for_Johnny = grades.pop(0)
sumIlenOfJohnny = sum(for_Johnny) / len(for_Johnny)

for_Khendrik = grades.pop(0)
sumIlenOfKhendrik = sum(for_Khendrik) / len(for_Khendrik)

for_Steve = grades.pop(0)
sumIlenOfSteve = sum(for_Steve) / len(for_Steve)

print([sumIlenOfAaron], [sumIlenOfBilbo], [sumIlenOfJohnny], [sumIlenOfKhendrik], [sumIlenOfSteve])

