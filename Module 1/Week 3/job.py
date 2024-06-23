'''
Một Ward (phường) gồm có name (string) và danh sách của mọi người trong Ward.
Một người person có thể là student, doctor, hoặc teacher. Một student gồm có name,
yob (int) (năm sinh), và grade (string). Một teacher gồm có name, yob, và subject
(string). Một doctor gồm có name, yob, và specialist (string). Lưu ý cần sử dụng a
list để chứa danh sách của mọi người trong Ward.


(a) Cài đặt các class Student, Doctor, và Teacher theo mô tả trên. Thực hiện phương thức
describe() method để in ra tất cả thông tin của các object.

(b) Viết add_person(person) method trong Ward class để add thêm một người mới với nghề
nghiệp bất kỳ (student, teacher, doctor) vào danh sách người của ward. Tạo ra một ward
object, và thêm vào 1 student, 2 teacher, và 2 doctor. Thực hiện describe() method để in ra
tên ward (name) và toàn bộ thông tin của từng người trong ward.

(c) Viết count_doctor() method để đếm số lượng doctor trong ward.

(d) Viết sort_age() method để sort mọi người trong ward theo tuổi của họ với thứ tự tăng dần.
(hint: Có thể sử dụng sort của list hoặc viết thêm function đều được)

(e) Viết compute_average() method để tính trung bình năm sinh của các teachers trong ward.

'''


class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def count_doctor(self):
        count = 0
        for person in self.people:
            if isinstance(person, Doctor):
                count += 1
        return count

    def sort_age(self):
        self.people.sort(key=lambda x: x.yob)

    def compute_average(self):
        sum_yob = 0
        count = 0
        for person in self.people:
            if isinstance(person, Teacher):
                sum_yob += person.yob
                count += 1
        return sum_yob / count

    def describe(self):
        print(f"Ward: {self.name}")
        for person in self.people:
            person.describe()


class Student:
    def __init__(self, name, yob, grade):
        self.name = name
        self.yob = yob
        self.grade = grade

    def describe(self):
        print(f"Student: {self.name}, yob: {self.yob}, grade: {self.grade}")


class Teacher:
    def __init__(self, name, yob, subject):
        self.name = name
        self.yob = yob
        self.subject = subject

    def describe(self):
        print(
            f"Teacher: {self.name}, yob: {self.yob}, subject: {self.subject}")


class Doctor:
    def __init__(self, name, yob, specialist):
        self.name = name
        self.yob = yob
        self.specialist = specialist

    def describe(self):
        print(
            f"Doctor: {self.name}, yob: {self.yob}, specialist: {self.specialist}")


# Output:
# 2(a)
# Example 1:
student1 = Student(name=" studentA ", yob=2010, grade="7")
student1.describe()

# Example 2:
teacher1 = Teacher(name=" teacherA ", yob=1969, subject=" Math ")
teacher1.describe()

# Example 3:
doctor1 = Doctor(name=" doctorA ", yob=1945, specialist=" Endocrinologists ")
doctor1.describe()

# 2(b)
print()
teacher2 = Teacher(name=" teacherB ", yob=1995, subject=" History ")
doctor2 = Doctor(name=" doctorB ", yob=1975, specialist=" Cardiologists ")
ward1 = Ward(name=" Ward1 ")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()

# 2(c)
print()
print(f"\n Number of doctors : { ward1 . count_doctor ()}")

# 2(d)
print()
print("\n After sorting Age of Ward1 people ")
ward1.sort_age()
ward1.describe()

# 2(e)
print(f"\n Average year of birth ( teachers ): {ward1.compute_average()}")
