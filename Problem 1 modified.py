"""
According to given instructions, I have been developed this system to recognize how many times words in array come in a string.
I have given the option to enter a string for a user and also default inputs are available which are a copy of example.
The string maximum length capacity is 1000 and the minimum is 10 according to given instructions. But the length of the input array can be 10 maximum and 2 minimum.
Here I used python so a list can not be predefined thus I made the maximum length of an array is 10 and the minimum is 2.
But I thing using c++ it can be performed ideally according to given instructions.
After that, I filtered string for "punctuation marks" and convert hole string in to lower case.
Then operation will perform on inputs and show output.
All output for default string is an ideal exception of "face". Which is a substring of "Facemasks".Thus the only drawback is it can't work for a substring.
"""

class WordsCalculation:
    def __init__(self):
        self.validation_array=None
        self.Input_str33=None
        self.x=None
        self.Input_str=""
        self.lnt=None
        self.lp=None

    def enter_input(self):
        choice=int(input("Choice 1:- If you want to enter your string and array of words press 1 \n"
                         "Choice 2:- Press 2 for use default string and word array \n"
                         "NOTE :- String should be minimum 10 and 1000 alph-numeric characters and array should be maximum 10 and minimum 2 word. \n"
                         "        Also the length of array should lesser then string length. \n"))
        if choice == 2:
            self.Input_str33="With the recent uptick to the COVID-19 positive cases and many states in various phases of restarting the economy; the food service industry and the restaurant sector have been strongly impacted. DMS Coalition is proud to announce the \"Facemasks For Restaurants Donation Initiative with a target of $2M in donation."
            self.validation_array = ["food", "face", "the", "donation", "coalition", "economy", "sector"]
        elif choice == 1:
            self.Input_str33=input("Enter your string \n")
            self.x=input("Enter the list of array element use space for diffentiet elements \n")
            self.validation_array=self.x.split(" ")




    def InputVerification_InputFilter(self):
        self.lnt=len(self.validation_array)
        self.lp=len(self.Input_str33)

        if self.lp<10 or self.lp>1000 or (self.lnt-1)<1 or (self.lnt-1)>10:
            print("====+=+=+=+=+ Please enter valid input according to given note +=+=+=+=+====\n\n")
            choice=1
            while choice==1:
                choice=int(input("\n Enter 0 to terminate program \n"))
            exit()
        else:
            pass


        input_str22=ti.Input_str33.lower()

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        for char in input_str22:
            if char not in punctuations:
                self.Input_str = self.Input_str + char



    def operation(self):
        x=self.Input_str.split()

        temp1=temp2=temp3=temp4=temp5=temp6=temp7=temp8=temp9=temp10=0

        for xl in x:
            if self.lnt>=1 and  xl==self.validation_array[0] :
                temp1=temp1+1

            elif self.lnt>=2 and xl==self.validation_array[1] :
                temp2=temp2+1

            elif self.lnt>=3 and xl==self.validation_array[2] :
                temp3=temp3+1

            elif self.lnt>=4 and xl==self.validation_array[3] :
                temp4=temp4+1

            elif self.lnt>=5 and xl==self.validation_array[4] :
                temp5=temp5+1

            elif self.lnt>=6 and xl==self.validation_array[5] :
                temp6=temp6+1

            elif self.lnt>=7 and xl==self.validation_array[6] :
                temp7=temp7+1

            elif self.lnt>=8 and xl==self.validation_array[7] :
                temp8=temp8+1

            elif self.lnt>=9 and xl==self.validation_array[8] :
                temp9=temp9+1

            elif self.lnt>=10 and xl==self.validation_array[9] :
                temp10=temp10+1

        temp=[temp1,temp2,temp3,temp4,temp5,temp6,temp7,temp8,temp9,temp10]
        ll=0
        while ll<self.lnt:
            print(self.validation_array[ll],":-",temp[ll])
            ll=ll+1


choice=1
while choice==1:
    ti=WordsCalculation()
    ti.enter_input()
    ti.InputVerification_InputFilter()
    ti.operation()
    choice=int(input("\n Enter 0 to terminate program \n"))
