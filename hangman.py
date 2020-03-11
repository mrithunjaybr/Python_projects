# Write your code here
import random
import string
def checkanswer(s,b):
    if ''.join(s) == b:
        print("You guessed the word {}!".format(''.join(s)))
        print("You survived!")
        return True

print("H A N G M A N")
l = ['python','java', 'kotlin', 'javascript']
tries = 8
b = random.choice(l)
s= '-'*len(b)
s=list(s)
alpha='abcdefghijklmnopqrstuvwxyz'
guessed_words=[]
while tries>0:

    print('\n'+''.join(s))
    userMove= input('Input a letter: > ')
    if len(userMove) == 1:
        if userMove in alpha:
            if userMove in b:
                    if userMove in guessed_words :
                        if tries!=0:

                            print("You already typed this letter")
                        else:
                            tries-=1
                            print("No improvements")
                            print("You are hanged!")
                            break
                    else:
                        for i in range(len(b)):
                             if b[i]==userMove:
                                    s[i]=userMove

                        if checkanswer(s, b):
                            break

            else:

                if tries!=0 and userMove in guessed_words:

                    print("You already typed this letter")
                elif tries!=1 and userMove not in guessed_words:

                    tries-=1
                    print('No such letter in the word')
                elif tries==1 and userMove not in guessed_words:

                    tries-=1
                    print("No such letter in the word")
                    print("You are hanged!")
                    break

            guessed_words.append(userMove)
        else:
            print('It is not an ASCII lowercase letter')

    else:
        print('You should print a single letter')


