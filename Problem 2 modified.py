"""
According to a given task, Here I accept two arrays from a user or provide two arrays which are copied
from the example and validate them maximum 1000 for Input array and 100 for validate array and also take
care of empty input. If a rejected array is greater then an input array it will show an error message.
"""

class ArrayFilter:
    def __init__(self):
        self.Input_array=None
        self.rejected_items=None
        self.output_items=None

    def enter_input(self):
        choice=int(input("Choice 1:- If you want to enter your input array and rejected array 1  \n"
                         "Choice 2:- Press 2 for use default string and word array  \n"
                         "NOTE :- The length of input array can be maximum 1000 and minimum 2,"
				"maximum length of rejected array can be maximum 10 and minimum 2,"
				"And should not cross maximum and minimum length for both of them.\n"
                         "        Also the length of input array should be greater then length of rejected array \n"))
        if choice == 2:
            self.Input_array = ["impolite", "cows", "undress", "rule", "illustrious", "beam", "helpless", "gold", "hair", "vacuous", "help", "guess", "squalid", "wonderful", "memorise", "present", "painful", "brake", "sand", "lip", "rainstorm", "talk", "abashed", "box", "partner", "chop", "tenuous", "robin", "trees", "moor", "hunt", "pack", "old-fashioned"]
            self.rejected_items=["undress","impolite","cows", "partner", "wonderful", "rainstorm", "pack", "painful"]
        elif choice == 1:
            k=input("Enter your input array's elements list in single line use space between them to differentiate elements \n")
            self.Input_array=k.split(" ")
            x=input("Enter a list of rejected array's elements list in single line use space between them to differentiate elements \n")
            self.rejected_items=x.split(" ")
            self.validation_of_inputs()

    def validation_of_inputs(self):
        lnt=len(self.rejected_items)
        lp=len(self.Input_array)
        print(lnt,lp)

        if lp-1==0 or lp-1>1000 or lnt-1==0 or lnt-1>10 or lnt>lp:
            print("====+=+=+=+=+ Please enter valid input according to given note +=+=+=+=+====\n\n")
            self.enter_input()
        else:
            pass

    def operation(self):
        x=len(self.rejected_items)
        y=0
        print("Original array:-",self.Input_array)
        while x!=0:
            k=self.Input_array.index(self.rejected_items[y])
            self.Input_array.pop(k)
            x=x-1
            y=y+1
        print("modified array:-",self.Input_array)

T=ArrayFilter()
T.enter_input()
T.operation()
choice=1
while choice==1:
    choice=int(input("Enter 0 to terminate a program. \n"))
