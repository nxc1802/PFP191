# Question 1 (2 Marks): Implement the CourseRegistration Class

class CourseRegistration:
    def __init__(self, course_id, course_name, instructor, department, credit_hours):
        # Public attributes
        self.course_id = course_id
        self.course_name = course_name
        self.instructor = instructor
        self.department = department
        # Private attribute
        self.__credit_hours = credit_hours

    # Getter
    def get_credit_hours(self):
        return self.__credit_hours

    # Setter
    def set_credit_hours(self, value):
        if value > 0:
            self.__credit_hours = value

    def __str__(self):
        return f"{self.course_id} - {self.course_name}, {self.instructor}, {self.department}, {self.__credit_hours} credits"


# Demo
c = CourseRegistration("C101", "IntroToAI", "Dr.Smith", "CS", 3)
print(c)
print("Credit hours:", c.get_credit_hours())
c.set_credit_hours(4)
print("After update:", c.get_credit_hours())
