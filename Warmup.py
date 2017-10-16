from random import randint
def main():
  students = [
    Student("Larsson","Halsted", 37),
    Student("BonJovi","Jon", 55),
    Student("Billy","McBillyBob",22),
  ]
  printHeader()
  selection = getUserSelection()
  if selection == 0:
    printStudentsByAge(students)
  elif selection == 1:
    printStudentsByLName(students)
  elif selection == 2:
    printStudentsByFName(students)
  elif selection == 4:
    printAvgAge(students)
  else:
    print("SELECTION NOT RECOGNIZED")

class Student:
  def __init__(self, lastName, firstName, age):
    self.lastName = lastName
    self.age = age
    self.firstName = firstName

  def assignRandomName(self):
    pass

  def assignRandomAge(self):
    self.age = random.randint(0,100)

  def assignRandomWeight(self, isMetric):
    pass

  def assignRandomHeight(self, isMetric):
    pass

inputQuestions = [ 
  "For STUDENTS BY AGE, type 0",
  "For STUDENTS BY LAST NAME, type 1",
  "For STUDENTS BY FIRST NAME, type 2",
  "For SUM of STUDENT AGES type 3",
  "For AVERAGE of STUDENT AGES type 4",
]

def getUserSelection():
  for inputQuestion in inputQuestions:
    print(inputQuestion)
  return int(input("Type selection and press enter:"))
  

def printHeader():
    print("Generic Academy Student Registry")

def printStudentsByAge(students):
  print ("----Students By Age-----")
  sortStudents = sorted(students, key=lambda student: student.age)
  for student in students:
    print(student.lastName + ", " + student.firstName + ", " + str(student.age))

def printStudentsByLName(students):
  print ("----Students By Last Name-----")
  sortStudents = sorted(students, key=lambda student: student.lastName)
  for student in students:
    print(student.lastName + ", " + student.firstName + ", " + str(student.age))
    
def printStudentsByFName(students):
  print ("----Students By First Name-----")
  sortStudents = sorted(students, key=lambda student: student.firstName)
  for student in students:
    print(student.firstName + ", " + student.lastName + ", " + str(student.age))
def printSumAge(students):
  print ("Answer:")

def printAvgAge(students):
  k = 0
  for x in students:
    k += student.age
  k = k/len(student)
  print ("Answer: " + str(k))

def ageRange(studentA, studentB):
  return math.abs(studentA.age - studentB.age)


main()
