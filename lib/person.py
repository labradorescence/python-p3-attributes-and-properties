# class Person:
#     def get_name(self):
#         return self._name

#     def set_name(self, name):
#         if(type(name) == str) and (1<=len(name)<=25):
#             self._name = name.title()
#         else:
#             print("Name must be string between 1 and 25 characters.")

#     def get_job(self):
#         return self._job

#     def set_job(self, job):

#         approved_jobs = ["Admin", "Customer Service", "Human Resources", "ITC", "Production", "Legal", "Finance", "Sales", "General Management", "Research & Development", "Marketing", "Purchasing"]

#         if job in approved_jobs:
#             self._job = job
#         else:
#             print("Job must be in list of approved jobs.")

#     name = property(get_name, set_name)
#     job = property(get_job, set_job)

# justy = Person()
# justy.name = "Justy"
# setattr(justy, "name", "Justin")
# print(justy.name)


class Human:
    species = "Homo sapiens"

    def get_age(self):
        print("Retrieving age.")
        return self._age

    def set_age(self, age):
        if (type(age) in (int, float)) and (0 <= age <= 120):
            print(f"Setting age to { age }.")
            self._age = age

        else:
            print("Age must be a number between 0 and 120.")

    age = property(get_age, set_age,)


guido = Human()
guido.age = 0
guido.age = False
guido.age = 66
guido.age
print(guido.age)