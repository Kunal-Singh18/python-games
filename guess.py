import random

number=random.randint(1,50)
print("RULES: ")
print("guess a number between 1 and 50")
print("maximum of 10 guesses can be made \nthere would be deduction of 5 points per wrong guess till 5 guesses and thereafter of 10 points")
print("you can at anytime quit game by pressing 0")

input("click to begin:")
chances=10
flag=0

while(chances):
    chances=chances-1
    guess=(int)(input("enter the number or QUIT(0)"))
    if(guess==0):
        flag=1
        break
    elif(guess>number and chances>0):
        print("take a smaller guess or QUIT(0)")
        print("chances left:",chances)
    elif(guess<number and chances>0):
        print("take a bigger guess QUIT(0)")
        print("chances left:",chances)
    elif(guess==number):
        print("correct guess")
        win=1
        break

    
print("game over!")

if(flag==0):  # incase game is quit in between.
    if(chances==0):
        print("score: 0")
    else:
        final_score=100
        if(chances>=5):
            final_score=final_score-((10-chances-1)*5)
        else:
            final_score=final_score-25-(5-chances-1)*10
        print("score:",final_score)
else:
    print("score:0")

