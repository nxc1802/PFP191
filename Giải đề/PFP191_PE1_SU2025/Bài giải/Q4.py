# Question 4 (3 Marks): Group and Print Courses by Credit Hours

class CourseRegistration:
    def __init__(self, course_id, course_name, instructor, department, credit_hours):
        self.course_id = course_id
        self.course_name = course_name
        self.instructor = instructor
        self.department = department
        self.__credit_hours = credit_hours

    def get_credit_hours(self):
        return self.__credit_hours

    def set_credit_hours(self, value):
        if value > 0:
            self.__credit_hours = value

    def __str__(self):
        return f"{self.course_id} - {self.course_name}, {self.instructor}, {self.department}, {self.__credit_hours} credits"


def load_course_data(filename):
    courses = []
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            for line in lines[1:]:
                parts = line.strip().split(",")
                if len(parts) == 5:
                    course_id, course_name, instructor, department, credit_hours = parts
                    c = CourseRegistration(course_id, course_name, instructor, department, int(credit_hours))
                    courses.append(c)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return courses


def group_courses_by_credit_hours(courses):
    result = {}
    for c in courses:
        ch = c.get_credit_hours()
        if ch not in result:
            result[ch] = []
        result[ch].append(c)
    return result


# Load and group
courses = load_course_data("course_data.txt")
grouped = group_courses_by_credit_hours(courses)

for credit_hours, course_list in sorted(grouped.items()):
    print(f"CreditHours: {credit_hours}")
    for c in course_list:
        print(f"- {c.course_id} - {c.course_name}, {c.instructor}, {c.department}, {c.get_credit_hours()} credits")
