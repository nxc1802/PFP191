# Question 2 (3 Marks): Load Course Data from a File

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
            for line in lines[1:]:          # skip header
                parts = line.strip().split(",")
                if len(parts) == 5:
                    course_id, course_name, instructor, department, credit_hours = parts
                    c = CourseRegistration(course_id, course_name, instructor, department, int(credit_hours))
                    courses.append(c)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return courses


# Test with missing file
load_course_data("file_not_found.txt")

# Load actual data
courses = load_course_data("course_data.txt")
for c in courses:
    print(c)
