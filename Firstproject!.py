#Final Grade Avg Formula Sheet
#ELA x5
#SS x5
#RM x3
#Math x5

#^^Mandatory Courses^^

#Sci x5
#Elective x3
#Second highest elective x2
#Total divided by 28
#-----------------------------------


#Defining variables

Scicourses = [] #List of Sci Courses
ElecCourses = [] #List of Elective Courses
GradesList = [] #List of Grades 
CandG = [] #Course Names and Grade in tuples
Clist = [] #List of Course Names
ElectiveGrade = [] #Non academic elective grades
Ctype = {} #Courses Y/N Academic 
Gbalanced = [] #For calclating Final Avg
AcademicG = [] #Academic Grades

#--------------------------------------------------------#

#Input for Science courses into ScienceCinput variable

ScienceCinput = input("Input SCIENCE courses ONLY *Seperate with a comma*:").split(",")

#Input invalid detection

while "ELA" in ScienceCinput or "SS" in ScienceCinput or "RM" in ScienceCinput  or "MATH" in ScienceCinput:
    ScienceCinput = input("Please provide SCIENCE courses ONLY:").split(",")

while ScienceCinput == "":
    ScienceCinput = input("Please provide a valid input:").split(",")

#Strips spaces from string

for sci in ScienceCinput:
    Scicourses.append(sci.strip().upper()) 

#--------------------------------------------------------#


#Input for Courses into Elective Courses input variable
ECinput = input("Input ELECTIVE courses ONLY *Seperate with a comma*:").split(",")


#Input invalid detection

while "ELA" in ECinput or "RM" in ECinput or "MATH" in ECinput:
    ECinput = input("Please provide ELECTIVE courses ONLY:").split(",")

while ECinput == "":
    ECinput = input("Please provide a valid input:").split(",") 

for Elec in ECinput:
    ElecCourses.append(Elec.strip().upper()) 

#Putting the Course names from Cinput and Scicourses into Clist

Clist = ["ELA", "SS", "RM", "MATH"] + Scicourses + ElecCourses

#Calclating the number of Courses
Numofc = len(Clist)

print("--------------------------------------------------------")

#--------------------------------------------------------#

#Input for course grades into GradesList
print("Enter GRADES: *Next course will appear after input*")

for i in range (Numofc):
    GradesList.append(float(input(Clist[i] + ":"))) 

#Puting each respective course and grades into a tuple inside CoursesandGrades(CandG) list
for i in range (Numofc):
    CandG.append((Clist[i], GradesList[i]))

#--------------------------------------------------------#

#Assigned default variables as these r mandatory courses
print("Input y/n academic course:")

Ctype[CandG[0]] = "Y" #ELA

Ctype[CandG[1]] = "Y" #SS

Ctype[CandG[2]] = "Special" #RM is a mandatory course than is weighted x3 but is not academic or non academic, so doesnt fit in any catagories

Ctype[CandG[3]] = "Y" #MATH

#Assigning the tuples in CandG with Y/N academic grades, putting them in new list called Ctype

for i in range (Numofc-4):
    Ctype[CandG[i + 4]] = input(Clist[i + 4].strip() + ": " + "Y/N? ").strip().upper() 


#--------------------------------------------------------#
#FINAL GRADE#

#Calclating the Final Grade multiplying each type of grade according to formula sheet 

for i, (keys,values) in enumerate(Ctype.items()):

    if i <= 3 and values != "Special":
        Gbalanced.append(keys[1]*5)

    elif values == "Special":
        Gbalanced.append(keys[1]*3)

    elif keys[0] in Scicourses:
        Gbalanced.append(keys[1]*5)

    else:
        ElectiveGrade.append(keys[1])
    

#Find the highest Grade for Electives and multiply it by 3

for i in range (1): 

    if len(ElectiveGrade) == 0:
        break 

    else:
        HighestEG = max(ElectiveGrade) 
        Gbalanced.append(HighestEG*3)

        if HighestEG == max(ElectiveGrade):
            del ElectiveGrade[ElectiveGrade.index(HighestEG)]  

#Repeate same thing for the 2nd highest elective grade but multiply by 2 this time

for i in range (1):
    if len(ElectiveGrade) == 0:
        break

    else:
        HighestEG2 = max(ElectiveGrade) 
        Gbalanced.append(HighestEG2*2) 

        if HighestEG2 == max(ElectiveGrade):
            del ElectiveGrade[ElectiveGrade.index(HighestEG2)]  


  #Adding all Grades together 

value = 0

for currentvalues in Gbalanced:
    value += currentvalues 

#Converting Final grade into percentage and round

FinalGrade = round(value/28, 2) 

print("Final Grade Avg: " + str(FinalGrade) + "%") #Prinitng Final Avg

print("--------------------------------------------------------")



#--------------------------------------------------------#


#Calclate 5-6 Academic Grades Avg:



#Assigning values in Ctype that is "Y" to AcademicG list

for keys, values in Ctype.items():

    if values == "Y":
        AcademicG.append(keys[1])
 
NumofAG = len(AcademicG)

#Making 2 copies of the list, each for diffrent calclations

AcademicG2 = []

AcademicG2 = AcademicG + AcademicG2


#Calclate 5 avg academic course (Using AcademicG2 List)

if NumofAG >= 5:

#Keep the 5 best academic courses in the list, delete the rest

    for i in range (NumofAG-5): 
        del AcademicG2[AcademicG2.index(min(AcademicG2))]

    value3 = 0

#Adding all Grades together

    for currentvalues in AcademicG2: 
        value3 = currentvalues + value3

#Calclating the final percentage 

    Final5academic = round(value3/5, 2) 

#Printing 5 Academic Grades out

print("5 Academic Grades Avg: " + str(Final5academic) + "%") 



#Calclate 6 avg academic course (Using AcademicG List)


if NumofAG >= 6:

#Keep 6 best academic courses, delete rest

    for i in range (NumofAG-6): 
        del AcademicG[AcademicG.index(min(AcademicG))]

    value2 = 0

#Adding all Grades in the list together

    for currentvalues in AcademicG: 
        value2 = currentvalues + value2

    Final6academic = round(value2/6, 2)

    print("6 Academic Grades Avg: " + str(Final6academic) + "%") #Printing 6 academic Grades avg out 


print("--------------------------------------------------------")


#--------------------------------------------------------#


#Calclate 5-6 Academic and Non-academic Grades

#Making copy of GradesList, each list for diffrent calclations
GradesList2 = []
GradesList2 = GradesList + GradesList2
NumofGradeList = len(GradesList)

#Deleting Grades until top 5 grades are left (Using GradesList2)

if NumofGradeList >= 5:
    for i in range (NumofGradeList - 5):
        del GradesList2[GradesList2.index(min(GradesList2))]

    value5 = 0

#Adding all grades from list tgt

    for currentvalues in GradesList2:
        value5 = currentvalues +value5

#Finding grade % and rounding

    final5bothgrades = round(value5/5, 2)


#Printing 5 Academic and Non Academic Grades Avg

    print("5 Academic and Non-academic Grades Avg: " + str(final5bothgrades) + "%") 


#Deleting all grades until top 6 are left (Using GradesList List)

if NumofGradeList >= 6:

    for i in range(NumofGradeList - 6): 
        del GradesList[GradesList.index(min(GradesList))] 

    value4 = 0

#Adding all grades in list tgt

    for currentvalues in GradesList:
        value4 = currentvalues + value4 

#Calclating % and rounding

    final6bothgrades = round(value4/6, 2)

#printing 6 academic and non academic Grades avg

    print("6 Academic and Non-academic Grades Avg: " + str(final6bothgrades) + "%")


#--------------------------------------------------------#