post = {"user_id":209,"message":"D5 E5 C4 G4","language":"English","datetime":"20230215T124231Z",
        "location":44.590533-104.715556}
print(post["user_id"])
print(post["message"])
print(post["language"])
print(post["datetime"])
print(post["location"])


post2 = dict(message= "hello there ", language= "English")
post2["user_id"] = 209
post2["datetime"] = "19771116T093001Z"
post2["location"] = "tel aviv"
print(post2)

print(post2["message"])
print(post2["location"])

if "location" in post2:
    print(post2["location"])
else:
    print("The post does not contain a location value.")
    try:
      print(post2["location"])
    except KeyError:
     print("The post does not have a location")




# convert a list of tuples into  dictionary



def convert(tup,di):
    di = dict(tup)
    return di



tup = [("gatluak",12),("james",13),("Peter",22),("Both",15),("Taban",21)]
dictionanry = {}

print(convert(tup,dictionanry))






def courses_per_student(tuples_lst):
  student = {}
  for i in tuples_lst:
    student_name = i[0].lower()
    courses_name = i[1].lower()
    if student_name in student:
      student[student_name].append (courses_name)
    else:
      student[student_name]= [courses_name]
    print(student)
  return student


def students_per_course(tuples_lst):
    course = {}
    for i in tuples_lst:
        student_name = i[0].lower()
        courses_name = i[1].lower()
        if courses_name in course:
            course[courses_name] += 1
        else:
            course[courses_name] = 1
        print(course)
    return course




print(courses_per_student([('Goanar', 'Math'), ('Efrem', 'Chemistry'),
         ('Philmon', 'python'), ('Goanar', 'pYthon')
     ,('EFrem', 'biology')]) =={'Goanar': ['math', 'python'],
     'EFrem': ['chemistry', 'biology'], 'Pilmon': ['python']})





print(students_per_course([('Goanar','Math'),('Taban','Chemistry')
,('Goanar', 'python'), ('Philmo','Python'),('Bol', 'biology'),('Philmon','Biology')])==
{'Goanar': ['math', 'python'], 'Taban': ['chemistry', 'biology'],
 'Bol': ['python'],'Efrem':['English'],'Philmon':['Arabic','Python']})






favorite_languages = {'Goanar':'Python',
        'Taban':'Ruby','Gaga':'C','Bol':'Python'}
for name,language in favorite_languages.items():
    print(name.title()+ "'s favorite language is " + language.title() + "."  )


friends =['Goanar','Taban']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + " I see your favorite language is " +favorite_languages[name].title()+".")

