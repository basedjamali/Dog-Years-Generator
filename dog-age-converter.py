welcome = 'Hello my friend :)\r\nWelcome to our app where you can convert human years into dog years or the other way round!'
print(welcome)

# Dog into Human years
def asking_1():
    question = input('Dog into Human years? [yes/no]:').lower()
    
    if question == 'yes':
        age = input('Pick a Dog year:')
        calculating = int(age) * 7
        print('Human years:', calculating)
        
    elif question == 'no':
        question_2 = input('Human into Dog years? [yes/no]:').lower()
        
        if question_2 == 'yes':
            age = input('Pick a Human year:')
            calculating = int(age) / 7
            print('Dog years:', calculating)
            
        elif question_2 == 'no':
            asking_1
            
    # if the user wants to calculate again
    again = input('Do you want to calculate again? [yes/no]:').lower()
    if again == 'yes':
        asking_1()
    else:
        print('Have a nice day :)')
        
asking_1()