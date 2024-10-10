from collections import deque

class VirtualClassManagement:
    def __init__(self):
        self.available_courses = ["Math", "Science", "History", "Art", "Computer Science"]
        self.registered_students = {}
        self.registration_stack = []
        self.class_queue = deque()

    def register_student(self, student_name, course_name):
        if course_name not in self.available_courses:
            print(f"Course '{course_name}' is not available.")
            return
        if student_name not in self.registered_students:
            self.registered_students[student_name] = []
        self.registered_students[student_name].append(course_name)
        self.registration_stack.append((student_name, course_name))
        print(f"{student_name} registered for {course_name}.")

    def undo_registration(self):
        if not self.registration_stack:
            print("No registration to undo.")
            return
        student_name, course_name = self.registration_stack.pop()
        self.registered_students[student_name].remove(course_name)
        if not self.registered_students[student_name]:
            del self.registered_students[student_name]
        print(f"Undo registration: {student_name} unregistered from {course_name}.")

    def schedule_class(self, course_name):
        if course_name not in self.available_courses:
            print(f"Course '{course_name}' is not available.")
            return
        self.class_queue.append(course_name)
        print(f"Scheduled class for {course_name}.")

    def get_scheduled_classes(self):
        if not self.class_queue:
            print("No classes scheduled.")
            return
        print("Scheduled classes:", list(self.class_queue))

    def show_available_courses(self):
        print("Available courses:", self.available_courses)

    def show_registered_students(self):
        if not self.registered_students:
            print("No students registered.")
            return
        for student, courses in self.registered_students.items():
            print(f"{student}: {', '.join(courses)}")


# Example Usage
if __name__ == "__main__":
    vc_management = VirtualClassManagement()
    
    vc_management.show_available_courses()
    
    vc_management.register_student("Alice", "Math")
    vc_management.register_student("Bob", "Science")
    
    vc_management.show_registered_students()
    
    vc_management.schedule_class("Math")
    vc_management.schedule_class("History")
    
    vc_management.get_scheduled_classes()
    
    vc_management.undo_registration()
    vc_management.show_registered_students()
