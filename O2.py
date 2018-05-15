class Person:
	def __init__(self, first, last):
		self.first_name = first
		self.last_name = last

	def __str__(self):
		return self.last_name + ", " + self.first_name

	def CreateCharacter(JobClass):
		first = input("PLEASE TYPE YOUR FIRST NAME")
		last = input("PLEASE TYPE YOUR LAST NAME")
		return JobClass(first, last)



class Doctor(Person):

	def __str__(self):
		return "Dr." + self.last_name + ", " + self.first_name

class Lawyer(Person):

	def __str__(self):
		return  self.last_name + ", " + self.first_name + "Esq."

	def CreateCharacter(JobClass):
		first = input("PLEASE TYPE YOUR FIRST NAME")
		last = input("PLEASE TYPE YOUR LAST NAME")
		return Lawyer(first, last)

options = {
	"Doctor" : Doctor,
	"Lawyer" : Lawyer,
	"Person" : Person
}


jobClassInput = input("Please TYPE your job")
JobClass = options[jobClassInput]
steve = JobClass.CreateCharacter( JobClass )
