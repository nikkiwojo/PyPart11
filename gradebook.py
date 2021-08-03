import uuid
from enum import Enum

class alive_status(Enum):
    deceased = 0
    alive = 1


class person:

    def __init__(self, first, last, dob):
        self.first_name = first
        self.last_name = last
        self.dob = dob
        self.alive_status = alive_status.alive

    def update_first_name(self, new_name):
        self.first_name = new_name
    
    def update_last_name(self, last_name):
        self.last_name = last_name

    def update_dob(self, date_of_birth):
        self.dob = date_of_birth

    def updat_status(self, alive_stat):
        self.alive_status = alive_stat


class instructor(person):

    def __init__(self, first_name, last_name, dob):
        super().__init__(first_name, last_name, dob)
        self.instructor_id = "Instructor " + str(uuid.uuid4())

class student(person):

    def __init__(self, first_name, last_name, dob):
        super().__init__(first_name, last_name, dob)
        self.student_id = "Student " + str(uuid.uuid4())

class ZipCodeStudent(student):
    
    def__init__(self, first_name, last_name, dob):
        super().__init__(first_name, last_name, dob)
        

