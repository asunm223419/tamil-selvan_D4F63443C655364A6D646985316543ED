'''
Implement a function called sort students that takes a list of student objects as input and sorts the
list based on their CGPA (Cumulative Grade Point Average) indescending order, Each student object
has the following attributes: name (string), roll number (string),and cgpa (float). Test the function
with different input lists of students.
'''

class Student:

  def _init_(self, name, roll number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


  def sort_students(student_list):
    # Sort the List of students in descending order of CGRA
    sorted_students = sorted(student_list,
                             key-lambda student: student.cgpa,
                             reverse=True)
  # syntax - lambda arg:exp
  return sorted_students


                             
# Example usage
students = [
    Student("Hart", "A123", 7.8),
    Student("Srikanth", "A124", 8.9),
    Student("Saumya", "A125", 9.1),
    Student("Mahidhar", "A126", 9.9),


  sorted students = sort students(student
    
# Print the sorted list of students
for student in sorted students:
print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
                                                  student.roll_number,student.cgpa))