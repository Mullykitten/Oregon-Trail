class Person:
	def __init__(self, first, last):
		self.first_name = first
		self.last_name = last

	def __str__(self):
		return self.last_name + ", " + self.first_name



class Doctor(Person):

	def __str__(self):
		return "Dr." + self.last_name + ", " + self.first_name

	def CreateCharacter(JobClass):
		first = input("PLEASE TYPE YOUR FIRST NAME")
		last = input("PLEASE TYPE YOUR LAST NAME")



class Lawyer(Person):

	def __str__(self):
		return  self.last_name + ", " + self.first_name + "Esq."

	def CreateCharacter(JobClass):
		first = input("PLEASE TYPE YOUR FIRST NAME")
		last = input("PLEASE TYPE YOUR LAST NAME")


options = {
	"Doctor" : Doctor,
	"Lawyer" : Lawyer,
	"Person" : Person,
}



class Companion(Person):


   def __str__(self):
	   return  self.last_name + ", " + self.first_name

   def CreateCharacter(Companion):
	   first = input("PLEASE TYPE THEIR FIRST NAME")
	   last = input("PLEASE TYPE THEIR LAST NAME")
	   return Companion(first, last)




jobClassInput = input("Please TYPE your job: ")
JobClass = options[jobClassInput]
Person = JobClass.CreateCharacter(JobClass)
print(Person)

def main():
	Companions = [
		Companion.CreateCharacter(Companion),
		Companion.CreateCharacter(Companion),
		Companion.CreateCharacter(Companion),
		Companion.CreateCharacter(Companion),
	]


print(Companion)

main()
