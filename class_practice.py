class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, *args, **kwargs):
        return cls(friend_name, origin.school, *args, **kwargs)
    # def friend(cls, origin, friend_name, salary):
    #     return cls(friend_name, origin.school, salary)


class WorkingStudent(Student):
    # pass  # Inheritance
    def __init__(self, name, school, salary, job_title):
        super().__init__(name, school)
        self.salary = salary
        self.job_title = job_title


if __name__ == '__main__':
    jack = WorkingStudent('Jack', 'OSU', 100, job_title='Engineer')
    sean = WorkingStudent.friend(jack, 'Sean', 20, job_title='Engineer')
    print(jack.name, jack.school, jack.salary, jack.job_title)
    print(sean.name, sean.school, sean.salary, sean.job_title)
