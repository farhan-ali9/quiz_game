print("-------QUIZ PROJECT--------")
name = str(input("what is you name : "))
print("Welcome " + name)
print("Lets start the quiz! Press Y/y for Yes and N/n for No")
choice = input()
score = 0
if choice == 'Y' or choice == 'y':
    print("Question 1 : CPu stand for ")
    user = input()
    if user == 'central processing unit':
        score += 1
    print("Question 2 : Communication between user and the computer is… ")
    user = input()
    if user == 'programming language':
        score += 1
    print("Question 3 : language is not an object oriented pogramming language ")
    user = input()
    if user == 'c++':
        score += 1
    print("Question 4 : translates the source code into machine language ")
    user = input()
    if user == 'language processor ':
        score += 1
    print("Question 5 : the language processor translates the program into object code as a whole ")
    user = input()
    if user == 'compiler':
        score += 1
    print("Question 6 : communication between user and the computer is ")
    user = input()
    if user == 'programming language':
        score += 1
    print("Question 7 : the pseudocode is ")
    user = input()
    if user == 'algorithm':
        score += 1
    print("Question 8 : In late binding, function call is resolved during")
    user = input()
    if user == 'runtime':
        score += 1
    print("Question 9 : Early binding can be implemented by ")
    user = input()
    if user == 'function overloading':
        score += 1
    print("Question 10 : In late binding, function call is resolved during?")
    user = input()
    if user == 'runtime':
        score += 1
else:
    print('Exit')
    quit()
print(name + "  you socred  " + str(score) + "  out of 10 !")