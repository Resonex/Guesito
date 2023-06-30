guessed_lines = []
guessed_lines2 = []
answer = []
line1= ["A","B","C","D","E"]
line2= ["F","G","H","I","J"]
line3= ["K","L","M","N","O"]
line4= ["P","Q","R","S","T"]
line5= ["U","V","W","X","Y"]
line6= ["Z"]
horizontal_lines = [line1,line2,line3,line4,line5,line6]


line_1=["A","F","K","P","U","Z"]
line_2=["B","G","L","Q","V"]
line_3=["C","H","M","R","W"]
line_4=["D","I","N","S","X"]
line_5=["E","J","O","T","Y"]
vertical_lines =[line_1 , line_2 , line_3 , line_4 ,line_5]

name =input(f"what's your name please? ")
while name =="" or len(name)< 4:
    name =input(f"what's your name please? ")
print(f"Dear {name}, you're welcome \n Below is a game created by MHIZTA PIO")
print(f'....................................................\n')
print(f'BEFORE WE PROCEED >>>\n please, carry three letter words in your mind.\n')
print(f'....................................................\n')

print(f'Make sure that this words of yours are meaningful....')
print(f'....................................................\n')
print(f' AM GOING TO GUESS THIS WORDS IN YOUR MIND CORRECTLY.....')
print(f'....................................................\n')
print(f"JUST FOLLOW THE RULES!!!\n LET'S GO >>>>>>>>>>>>>>>>>>")
print(f'::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n')
print(f'HORIZONTAL LINES ARE:\n line_1 = {line1}\n line_2 = {line2}\n line_3 = {line3}\n line_4 = {line4}\n line_5 = {line5}')
  
choice_1 = input("Horizontally, which line is your first Alphabet located? \n"
"type either line1 | line2 | line3 | line4 | line5: ")

if choice_1 == 'line1' :
    choice_1 = line1
    guessed_lines.append(choice_1)
    
elif choice_1 == 'line2':
  choice_1 = line2
  guessed_lines.append(choice_1)
  
elif choice_1 == 'line3':
  choice_1 = line3
  guessed_lines.append(choice_1)
  
elif choice_1 == 'line4':
  choice_1 = line4
  guessed_lines.append(choice_1)
  
elif choice_1 == 'line5':
  choice_1 = line5
  guessed_lines.append(choice_1)
  
elif choice_1 == 'line6':
  choice_1 = line6
  guessed_lines.append(choice_1)
  
  #For Choice 2
  
choice_2 = input("Horizontally, which line is your second Alphabet located? \n"
"type either line1 | line2 | line3 | line4 | line5: ")

if choice_2 == 'line1' :
    choice_2 = line1
    guessed_lines.append(choice_2)
 
elif choice_2 == 'line2':
    choice_2 = line2
    guessed_lines.append(choice_2)
  
elif choice_2 == 'line3':
    choice_2 = line3
    guessed_lines.append(choice_2)
  
elif choice_2 == 'line4':
    choice_2 = line4
    guessed_lines.append(choice_2)
  
elif choice_2 == 'line5':
    choice_2 = line5
    guessed_lines.append(choice_2)
    
elif choice_2 == 'line6':
    choice_2 = line6
    guessed_lines.append(choice_2)
  
#For Choice_3  
#'''::::::      ......;;;;;::::

choice_3 = input("Horizontally, which line is your third Alphabet located? \n"
"type either line1 | line2 | line3 | line4 | line5: ")

if choice_3 == 'line1' :
    choice_3 = line1
    guessed_lines.append(choice_3)
 
elif choice_3 == 'line2':
    choice_3 = line2
    guessed_lines.append(choice_3)
  
elif choice_3 == 'line3':
    choice_3 = line3
    guessed_lines.append(choice_3)
  
elif choice_3 == 'line4':
    choice_3 = line4
    guessed_lines.append(choice_3)
  
elif choice_3 == 'line5':
    choice_3 = line5
    guessed_lines.append(choice_3)

elif choice_3 == 'line6':
    choice_3 = line6
    guessed_lines.append(choice_3)

#FOR Vertical lines........... 
#.................................

print(f'Vertical lines are:\n line_1 ={line_1}\n line_2 ={line_2}\n line_3 ={line_3}\n line_4 = {line_4}\n line_5= {line_5}')

choice_v1 = input("vertically, which line is your first Alphabet located? \n"
"type either line_1 | line_2 | line_3 | line_4 | line_5: ")

if choice_v1 == 'line_1' :
    choice_v1 = line_1
    guessed_lines2.append(choice_v1)

elif choice_v1 == 'line_2':
    choice_v1 = line_2
    guessed_lines2.append(choice_v1)

elif choice_v1 == 'line_3':
    choice_v1 = line_3
    guessed_lines2.append(choice_v1)

elif choice_v1 == 'line_4':
    choice_v1 = line_4
    guessed_lines2.append(choice_v1)

elif choice_v1 == 'line_5':
    choice_v1 = line_5
    guessed_lines2.append(choice_v1)


#FOR VERTICAL LINE 2..........
#........USERS CHOICE 2.............
#.....................................

choice_v2 = input("vertically, which line is your second Alphabet located? \n"
"type either line_1 | line_2 | line_3 | line_4 | line_5: ")

if choice_v2 == 'line_1' :
    choice_v2 = line_1
    guessed_lines2.append(choice_v2)

elif choice_v2 == 'line_2':
    choice_v2 = line_2
    guessed_lines2.append(choice_v2)

elif choice_v2 == 'line_3':
    choice_v2 = line_3
    guessed_lines2.append(choice_v2)

elif choice_v2 == 'line_4':
    choice_v2 = line_4
    guessed_lines2.append(choice_v2)

elif choice_v2 == 'line_5':
    choice_v2 = line_5
    guessed_lines2.append(choice_v2)
    
    
#FOR VERTICAL LINE 3 .............
#........Users CHOICE 3.................
#......'.........'..................



choice_v3 = input("vertically, which line is your THIRD Alphabet located? \n"
"type either line_1 | line_2 | line_3 | line_4 | line_5: ")

if choice_v3 == 'line_1' :
    choice_v3 = line_1
    guessed_lines2.append(choice_v3)

elif choice_v3 == 'line_2':
    choice_v3 = line_2
    guessed_lines2.append(choice_v3)

elif choice_v3 == 'line_3':
    choice_v3 = line_3
    guessed_lines2.append(choice_v3)

elif choice_v3 == 'line_4':
    choice_v3 = line_4
    guessed_lines2.append(choice_v3)

elif choice_v3 == 'line_5':
    choice_v3 = line_5
    guessed_lines2.append(choice_v3)

for a in guessed_lines2[0]:
    for b in guessed_lines2[1]:
        for c in guessed_lines2[2]:
            if a in guessed_lines[0]:
                answer.append(a)
                if b in guessed_lines[1]:
                    answer.append(b)
                    if c in guessed_lines[2]:
                        answer.append(c)
                        print(set(answer))














#for i in line_1:
#    for k in lineY_1:
 #       if line_1.issuperset(k):
 #           print(k)
  #          break

