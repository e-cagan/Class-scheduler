class Course:
    def __init__(self, course_id, course_starts, course_ends, course_day, student_capacity, credit):
        self.course_id = course_id
        self.course_starts = course_starts
        self.course_ends = course_ends
        self.course_day = course_day
        self.student_capacity = student_capacity
        self.credit = credit
        self.schedule = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
        self.schedule[self.course_day].append(self.course_id)
        self.credit_limit = 20
        self.student_counter = 0

    # Function for displaying the schedule
    def display_schedule(self):
        return self.schedule

    # Function for checking overlap situations
    def check_overlap(self, course_id, course_start_time, course_end_time, course_day):
        if self.course_starts < course_end_time and self.course_ends > course_start_time and course_day == self.course_day:
            print(f"The {course_id} is overlapping with {self.course_id}. Please reconsider your choice.")
            return True
        else:
            return False

    # Function for adding a course
    def add_course(self, course_id, course_start_time, course_end_time, course_day, credit):
        if not self.check_overlap(course_id, course_start_time, course_end_time, course_day):
            if self.student_counter >= self.student_capacity:
                print(f"Course {course_id} can't be taken because the student capacity is full.")
                return False
            elif self.credit + credit > self.credit_limit:
                print(f"Course {course_id} can't be taken because you've reached your credit limit.")
                return False
            else:  
                self.schedule[course_day].append(course_id)
                self.student_counter += 1
                self.credit += credit
                print(f"The course {course_id} is successfully added to the schedule.")
                print(f"Start time: {course_start_time}")
                print(f"End time: {course_end_time}")
                self.display_schedule()
                return True

    # Funciton for removing the course
    def remove_course(self, course_id, course_day):
        if course_id not in self.schedule[course_day]:
            print(f"{course_id} is not in the schedule on {course_day}. So it cannot be removed.")
            return False
        else:
            self.schedule[course_day].remove(course_id)
            self.student_counter -= 1
            print(f"Course {course_id} is removed successfully.")
            self.display_schedule()
            return True

# Testing a real life simulation
def real_life_simulation():
    course_id = input("Enter the course id: ").upper()
    course_starts = int(input(f"When will start the course {course_id}? "))
    course_ends = int(input(f"When will end the course {course_id}? "))
    course_day = input("Enter the course day: ").title()
    student_capacity = int(input("Enter the student capacity: "))
    credit = int(input("Enter the amount of credit: "))
    
    course = Course(course_id, course_starts, course_ends, course_day, student_capacity, credit)
    print(course.display_schedule())

    while True:
        action = input("Enter 'add' to add a course, 'remove' to remove a course, or 'exit' to stop: ").lower()

        if action == 'add':
            new_course_id = input("Enter the new course id: ").upper()
            new_course_day = input("Enter the course day: ").title()
            new_course_start_time = int(input("Enter the course start time: "))
            new_course_end_time = int(input("Enter the course end time: "))
            new_credit = int(input("Enter the amount of credit for the new course: "))  
            course.add_course(new_course_id, new_course_start_time, new_course_end_time, new_course_day, new_credit)
            print(course.display_schedule())
        elif action == 'remove':
            remove_course_id = input("Enter the course id for removal: ").upper()
            remove_course_day = input("Enter the course day for removal: ").title()
            course.remove_course(remove_course_id, remove_course_day)
            print(course.display_schedule())
        elif action == 'exit':
            print("Have a nice day.")
            break
        else:
            print("Invalid action. Please enter 'add', 'remove', or 'exit'.")

real_life_simulation()
