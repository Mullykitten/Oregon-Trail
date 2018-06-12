class Person:
	def __init__(self, first, last):
		self.first_name = first
		self.last_name = last

	def __str__(self):
		return self.last_name + ", " + self.first_name



class Doctor(Person):
	balance = "balance is 2000"

	def __str__(self):
		return "Dr." + self.last_name + ", " + self.first_name

	def CreateCharacter(JobClass):
		first = input("PLEASE TYPE YOUR FIRST NAME")
		last = input("PLEASE TYPE YOUR LAST NAME")



class Lawyer(Person):
	balanace = "balance is 1700"

	def __str__(self):
		return  self.last_name + ", " + self.first_name + "Esq."

	def CreateCharacter(JobClass):
		first = input("PLEASE TYPE YOUR FIRST NAME")
		last = input("PLEASE TYPE YOUR LAST NAME")

class Dentist(Person):
	balance = "balance is 2,200"

	def __str__(self):
		return "Dr" + self.last_name + "," + self.first_name

	def CreateCharacter(JobClass):
		first = input("PLEASE TYPE YOUR FIRST NAME")
		last = input("PLEASE TYPE YOUR LAST NAME")

class RetailWorker(Person):
	balance = "balance is 600, you asked for this"

	def __str__(self):
		return "Get to the store" + self.last_name + "," + self.first_name

	def CreateCharacter(JobClass):
		first = input("PLEASE TYPE YOUR FIRST NAME")
		last = input("PLEASE TYPE YOUR LAST NAME")

class Chef(Person):
	balance = "balance is 1400"
	def __str__(self):
		return "Chef" + self.last_name + "," + self.first_name

	def CreateCharacter(JobClass):
		first = input("PLEASE TYPE YOUR FIRST NAME")
		last = input("PLEASE TYPE YOUR LAST NAME")


class Engineer(Person):
	balance = "balance is 1700"
	def __str__(self):
		return "Mister" + self.last_name + "," + self.first_name

	def CreateCharacter(JobClass):
		first = input("PLEASE TYPE YOUR FIRST NAME")
		last = input("PLEASE TYPE YOUR LAST NAME")


class Heir(Person):
	balance = "balance is 6000, good luck sucker"

	def __str__(self):
		return "Lord" + self.last_name + "," + self.first_name

	def CreateCharacter(JobClass):
		first = input("PLEASE TYPE YOUR FIRST NAME")
		last = input("PLEASE TYPE YOUR LAST NAME")

options = {
	"Doctor" : Doctor,
	"Lawyer" : Lawyer,
	"Dentist" : Dentist,
	"RetailWorker": RetailWorker,
    "Chef" : Chef,
	"Engineer" : Engineer,
	"Heir" : Heir,
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
person = JobClass.CreateCharacter(JobClass)
print(person)
print(JobClass.balance)

def main():
	Companions = [
		Companion.CreateCharacter(Companion),
		Companion.CreateCharacter(Companion),
		Companion.CreateCharacter(Companion),
		Companion.CreateCharacter(Companion),
	]


print(Companion)


main()

print("Your journey begins in Portland Maine and will end in Seattle Washington. This trip will be long and tiring, particularly with your companions. In order to keep your companion from abandoning the trip and hitchhiking home or simply disappearing into the wilderness, we suggest buying food, clothing, extra car parts, and luxury items to keep their interest.")


class items:
	def __init__ (self,):
		self.Food = Food
		self.Clothing = Clothing
		self.SpareParts = SpareParts
		self.Luxuryitems = Luxuryitems

items = {

   "9 dollars per pound" : Food,
   "10 dollars per set" : Clothing,
   "20 dollars per part": SpareParts,
   "20 dollars per item" : Luxuryitems,
}

selection = int(getUserSelection())
if selection == 0:
	Food(self.Food)
elif selection == 1:
	Clothing(self.Clothing)
elif selection == 2:
	SpareParts(self.SpareParts)
elif selection == 3:
	Luxuryitems(self.Luxuryitems)

else: print ("SELECTION NOT RECOGNIZED")


inputQuestions =[
"For food price, type 0",
"For for clothing price, type 1",
"For spare parts price, type 2",
"For for luxury items price, type 3",

]

def getUserSelection():
    print (inputQuestions[0])
    print (inputQuestions[1])
    print (inputQuestions[2])
    print (inputQuestions[3])


    return input("Type Selection and press enter" )
main()
