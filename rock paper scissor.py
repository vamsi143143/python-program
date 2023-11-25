import pyautogui as t
import random
t.alert(title='Rock&Paper&Scissior',text='Hi...',button='next')
name=t.prompt(title="User Details",text='Name of Player')
score=0
computer_score=0
r,p,s='✊','✋','✌'
c='play again'
def computer_out():
    s=('✊','✋','✌')
    u=random.randrange(0,2)
    return s[u]
def result(a,b):
    global score,computer_score
    if(a==b):
        return 'tie'
    elif(a=='✊' and b=='✌'):
        score+=1
        return 'you won'
    elif(a=='✋' and b=='✊'):
        score+=1
        return 'you won'
    elif(a=='✌' and b=='✋'):
        score+=1
        return 'you won'
    else:
        computer_score+=1
        return 'you lost'
if(name!=None):
    while(c=='play again'):
        user_input=t.confirm(title='Choose',text='Choose',buttons=(r,p,s))
        computer_input=computer_out()
        l=result(user_input,computer_input)
        c=t.confirm(text=f'User={user_input}\t\tComputer={computer_input}\n\n\t{l.upper()}',title='Result',buttons=('end','play again'))
    else:
        t.alert(title='SCORE CARD',text=f'NAME={name}\nUSER_SCORE={score}\nCOMPUTER_SCORE={computer_score}')
        t.alert(title='Rock&Paper&Scissior',text='Thank You...\nHappy Gaming Sir..',button='close')
else:
    t.alert(title='Rock&Paper&Scissior',text='Thank You...',button='close')
    
    
