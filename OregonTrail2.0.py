class FirstChoice:
    def __init__(self,):
        self.Doctor
        self.Dentist
        self.RetailWorker
        self.Chef
        self.Engineer
        self.ArrogantHeir

class SecondChoice:
    def __init__(self,):
        self.Doctor1
        self.Dentist2
        self.RetailWorker3
        self.Chef4
        self.Engineer5
        self.ArrogantHeir6

Doctor = [

 "The doctor can handle illness and possible injury, is decent with food and has a minor understanding of mechanical repair, carries 2,000$"

 ]

Dentist = [

"The dentist can handle minor illness, decent with food and can handle some mechanical issues and repairs, carries 3,000$"

 ]

RetailWorker = [

"The retail worker can handle people surprisingly well and is decent with self defense, good with mechanical issues and decent with food, carries 500"

 ]


Chef = [

 "The chef can handle the production and prevent most foodborne illness, the chef is okay with socializing, not the best with mechanial issues, carries 1,300"

 ]

Engineer = [

"The engineer can handle all mechanial and electrical problems, not the best with the production of food or the socialization with people, carries 1,750"

 ]

ArrogantHeir = [

"The arrogant heir is not good at getting food, socializing, handling mechanical issues, gets lost easily, but can smooth talk to get lower prices, carries 6,000"

]

Doctor1 = [

"You have chosen the doctor, a wise choice, here is 2,000 dollars"

]

Dentist2 = [

"You have chosen the dentist, a safe choice, here is 3,000 dollars"

]

RetailWorker3 = [

"You have chosen the retail worker, you truly must have some spite within you, here is 500 dollars"

]

Chef4 = [

"You have chosen the chef, prepare for a delicious journey, here is 1,300 dollars"

]

Engineer5 = [

"You have chosen the engineer, a pratical choice, here is 1,750 dollars"

]

ArrogantHeir6 = [

"You have chosen the arrogant heir, here is 6,000 dollars, good luck surviving, sucker"

]

def main():
     printHeader()
     FirstChoices = [
     FirstChoice(),
     ]
     SecondChoices = [
     SecondChoice(),
     ]


     selection = int(getUserSelection())

     if selection == 0:
         printFirstChoiceDoctor(FirstChoices)

     if selection == 1:
         printFirstChoiceDentist(FirstChoices)

     if selection == 2:
         printFirstChoiceRetailWorker(FirstChoices)

     if selection == 3:
         printFirstChoiceChef(FirstChoices)

     if selection == 4:
         printFirstChoiceEngineer(FirstChoices)

     if selection == 5:
         printFirstChoiceArrogantHeir(FirstChoices)

     if selection == 6:
         printSecondChoiceDoctor1(SecondChoices)

     if selection == 7:
         printSecondChoiceDentist2(SecondChoices)

     if selection == 8:
         printSecondChoiceRetailWorker3(SecondChoices)

     if selection == 9:
         printSecondChoiceChef4(SecondChoices)

     if selection == 10:
         printSecondChoiceEngineer5(SecondChoices)


     if selection == 11:
         printSecondChoiceArrogantHeir6(SecondChoices)

     else:
        print ("SELECTION NOT RECOGNIZED")

inputQuestions = [
"For information on the doctor, type 0",
"For information on the dentist, type 1",
"For the information on the retail worker, type 2",
"For information on the chef, type 3",
"For information on the engineer, type 4"
"For infromation on the arrogant heir, type 5"
"Be a doctor, type 6",
"Be a dentist, type 7",
"Be a retail worker, if you dare, type 8",
"Be a chef, type 9",
"Be an engineer, type 10",
"Be an arrogant heir, because why not, type 11"
     ]

def getUserSelection():
    print (inputQuestions[0])
    print (inputQuestions[1])
    print (inputQuestions[2])
    print (inputQuestions[3])
    print (inputQuestions[4])
    print (inputQuestions[5])
    print (inputQuestions[6])
    print (inputQuestions[7])
    print (inputQuestions[8])
    print (inputQuestions[9])
    print (inputQuestions[10])
    print (inputQuestions[11])

    return input("Type Selection and press enter" )

def printHeader():
    print("DOG INFO")

def  printFirstChoiceDoctor(FirstChoices):
    print ("----Doctor----")
    sortFirstChoices= sorted(Choices, key=lambda Doctor: Choice.Doctor)
    for FirstChoice in FirstChoices:
        print(Choice.Doctor)

def printFirstChoiceDentist(FirstChoices):
    print("----Dentist----")
    sortFirstChoices = sorted(Choices, key=lambda Dentist: Choice.Dentist)
    for FirstChoice in FirstChoices:
        print(Choice.Dentist)

def printFirstChoiceRetailWorker(FirstChoices):
    print("----Retail Worker----")
    sortFirstChoices = sorted(Choices, key=lambda RetailWorker: Choice.RetailWorker)
    for FirstChoice in FirstChoices:
        print(Choice.RetailWorker)

def printFirstChoiceEngineer(FirstChoices):
    print("----Engineer----")
    sortFirstChoices = sorted(Choices, key=lambda Engineer: Choice.Engineer)
    for FirstChoice in FirstChoices:
        print(Choice.Engineer)

def printFirstChoiceArrogantHeir(FirstChoices):
    print("----Arrogant Heir----")
    sortFirstChoices = sorted(Choices, key=lambda ArrogantHeir: Choice.ArrogantHeir)
    for FirstChoice in FirstChoices:
        print(Choice.ArrogantHeir)

def printSecondChoiceDoctor1(SecondChoices):
    print("----Doctor----")
    sortSecondChoices = sorted(Choices, key=lambda Doctor1: Choice.Doctor1)
    for FirstChoice in FirstChoices:
        print(Choice.Doctor1)


main()
