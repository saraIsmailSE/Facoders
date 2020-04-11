def grade_list(grade_name):
    grade_one={'Faris': [18, 19, 17, 26, 9], 'Salem': [20, 20, 19, 30, 10], 'Mahmoud': [12, 13, 11, 18, 7]}
    grade_two= {'Lana': [17, 19, 20, 28, 9], 'Dina': [18.5, 19.5, 20, 29, 10], 'Maha': [20, 20, 18, 26, 9], 'Abeer': [16, 18, 19.5, 25, 8]}
    grade_three = {'Rima': [18, 19, 18, 26, 9], 'Tala': [20, 20, 19, 29, 10], 'Lamar': [19, 20, 18, 26, 9], 'Rola': [15, 14, 16, 19, 7], 'Naya': [9, 6, 11, 14, 7], 'Dalal': [1, 5, 2, 6, 7], 'Ola': [19.5, 20, 20, 29.5, 10]}
    if grade_name == "grade one":
        return grade_one
    elif grade_name == "grade two":
        return grade_two
    elif grade_name == "grade three":
        return grade_three
    else:
        return "invalid"
        
def students_names(grade_name):
    if grade_list(grade_name) != "invalid":
        return print (list(grade_list(grade_name).keys()))
    else:
        print("Invalid Grade Name")

def student_score(grade_name,std_name):
    if grade_list(grade_name) != "invalid":
        grade_std = grade_list(grade_name)
        if std_name in grade_std:
            return print (sum(grade_std[std_name]))
        else:
            return print ("Wrong Name")
    else:
        print("Invalid Grade Name")
def students_count(grade_name):
    if grade_list(grade_name) != "invalid":
        return len(grade_list(grade_name))
    else:
        print("Invalid Grade Name")
play = True
def more_done():
    state=input("more or done? \n")
    if state.lower() == "done":
        return False
    
while play:
 
    choice = int(input("Choose one: 1- students names, 2- student score, 3- students count \n"))
    if choice == 1: 
        grade_name = input("Enter Grade Name \n") 
        print("students names")
        students_names(grade_name)
        play =more_done()
        
    elif choice == 2: 
        grade_name = input("Enter Grade Name\n") 
        std_name = input("Enter Student Name\n") 
        print("student Score")
        student_score(grade_name,std_name.title())
        play =more_done()
        
    elif choice == 3: 
        grade_name = input("Enter Grade Name \n")
        print("Number of Student")
        print(students_count(grade_name))
        play=more_done()
    else:
        print("Enter valid Number")


print("Goodbye !!")
  


