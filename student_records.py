student_records = {}
def add_student(name, age, courses):
    if name in student_records:
        print(f"Student {name} already exists.")
    else:
        student_records[name] = {'age' : age, 'grades' : set(), 'courses' : set(courses)}
        print(f"Student '{name}' added successfully.")

def add_grade(name, grade):
    if name not in student_records:
        print(f"Student '{name}' not found.")
    else:
        student_records[name]['grades'].add(grade)
        print(f"Grade {grade} added for student '{name}'.")
    
def is_enrolled(name, course):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return False
    else:
        if course in student_records[name]['courses']:
            return True
        else:
            return False

def calculate_average_grade(name):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return None
    else:
        if student_records[name]['grades'] == {}:
            return 0
        else:
            average_grade = float(sum(student_records[name]['grades'])/len(student_records[name]['grades']))
            return average_grade

def list_students_by_course(course):
    list_by_course = []
    for key in student_records:
        if course in student_records[key]['courses']:
            list_by_course.append(key)
    if list_by_course == []:
        return []
    else:
        return sorted(list_by_course)

def filter_top_students(threshold):
    top_students = []
    for key in student_records:
        if calculate_average_grade(key) > threshold:
            top_students.append(key)
    return top_students
    

        
    
