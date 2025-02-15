
def letterGrade(percentage):
    if percentage >= 90:
        return "A"
    elif 90 > percentage >= 80:
        return "B"
    elif 80> percentage >= 70:
        return "C"
    elif 70 > percentage >= 60:
        return "D"
    else:
        return "F"

student_name = input("Enter your name: ")
list_value = []
value = int(input("Enter your grade: "))
list_value.append(value)
value = int(input("Enter your grade: "))
list_value.append(value)
value = int(input("Enter your grade: "))
list_value.append(value)
value = int(input("Enter your grade: "))
list_value.append(value)
value = int(input("Enter your grade: "))
list_value.append(value)

average= (list_value[0]+list_value[1]+list_value[2]+list_value[3]+list_value[4]) /len(list_value)
letter_grade = letterGrade(average)

print("\n", student_name,
      "\n average:", average,
      "\n Letter Grade:", letter_grade)
