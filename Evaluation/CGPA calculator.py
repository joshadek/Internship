def convert_grade(score):
    if student_score>=70:
        return("A")
    elif student_score>=60:
        return("B")
    elif student_score>=50:
        return("C")
    elif student_score>=45:
        return("D")
    elif student_score>=40:
        return("E")
    else:
        return("F")
    


def calculate_gp(student_score, course_unit):
    if student_score >= 70:
        return 5*course_unit
    elif student_score >= 60:
        return 4*course_unit
    elif student_score >= 50:
        return 3*course_unit
    elif student_score >= 45:
        return 2*course_unit
    elif student_score >= 40:
        return 1*course_unit
    else:
        return 0*course_unit


def calculate_cgpa(total_grade_points, total_units):
    return total_grade_points/total_units

grade_points=[]
units=[]



print("Enter the number of subjects you're offering")
subjects_offering=int(input())


for i in range(subjects_offering):
    print("Enter subject, grade and unit respectively")
    subject=input()
    student_score=int(input())
    course_unit=int(input())
    units.append(course_unit)
    grade_points.append(calculate_gp(student_score, course_unit))
    
    
    
if student_score>100 or student_score<0:
    print("ERROR. Invalid score. Please enter a value between 0 and 100")
else:
    total_units=sum(units)
    total_grade_points=sum(grade_points)
    
    print(total_grade_points)
    print(total_units)

    print(calculate_cgpa(total_grade_points, total_units))


    






