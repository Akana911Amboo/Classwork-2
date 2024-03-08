students_list = []
students_dict = {}

name = input("Choe ra gi ming drish:")
age = int(input("Choe ra gi lo drish:"))
grade = int(input("choe ra gi lobrim drish:"))

students_list.append(name)
students_dict[name] = {age , grade} 

search_student = input("Enter your name")
if search_student in students_list:
    print(f"Student found! Age: {students_dict[search_student]}")

else:
    print("Student not found!")

print("List of students:")
for student in students_list:
    print(student)

remove_name = ("Enter the name you want to remove or enter to skip")
if remove_name in students_list:
    remove_name = students_dict[remove_name]
    students_list.remove(remove_name)
    del students_dict[remove_name]
    print("Name removed successfully!'")
    print("Name available: ", students_list)

else:
    print("Student not found")