import customtkinter as ck 
import random
def next_turn(row,col):
    global turn  
    if (game_bt[row][col].cget("text") == "") and (check_winner() ==False) : 
        if turn == players[0]:
            game_bt[row][col].configure(text =turn)
            if check_winner()==False :  

                turn=players[1]
                l1.configure(text=f'{turn} Turn')
            elif check_winner()==True : 
                l1.configure(text=f'{players[0]} Win!')
                
            elif check_winner() == "tie" : 
                l1.configure(text=f'Tie , No Winner!')

    if (game_bt[row][col].cget("text")== "") and (check_winner() ==False) : 
        if turn == players[1]:
            game_bt[row][col].configure(text =f'{turn}')
            if check_winner()==False : 
                turn=players[0]
                l1.configure(text=f'{turn} Turn')
            elif check_winner()==True : 
                l1.configure(text=f'{players[1]} Win!')
                game_bt[row][col].configure(fg_color='#ff9d3c')
            elif check_winner() == "tie" : 
                l1.configure(text=f'Tie , No Winner!')

def check_winner(): 
    for row in range(3): 
        if (game_bt[row][0].cget("text")==game_bt[row][1].cget("text")==game_bt[row][2].cget("text")) and (game_bt[row][0].cget("text")!="" ):
            game_bt[row][0].configure(fg_color='#ff9d3c')
            game_bt[row][1].configure(fg_color='#ff9d3c')
            game_bt[row][2].configure(fg_color='#ff9d3c')
            return True  
    for col  in range (3) : 
        if (game_bt[0][col].cget("text")==game_bt[1][col].cget("text")==game_bt[2][col].cget("text")) and (game_bt[0][col].cget("text")!="" ) :
            game_bt[0][col].configure(fg_color='#ff9d3c')
            game_bt[1][col].configure(fg_color='#ff9d3c')
            game_bt[2][col].configure(fg_color='#ff9d3c')
            return True
    
    if (game_bt[0][0].cget("text")==game_bt[1][1].cget("text")==game_bt[2][2].cget("text")) and (game_bt[0][0].cget("text")!=""):
        game_bt[0][0].configure(fg_color='#ff9d3c')
        game_bt[1][1].configure(fg_color='#ff9d3c')
        game_bt[2][2].configure(fg_color='#ff9d3c')
        return True 
    elif (game_bt[0][2].cget("text")==game_bt[1][1].cget("text")==game_bt[2][0].cget("text")) and game_bt[0][2].cget("text")!=""  :
        game_bt[0][2].configure(fg_color='#ff9d3c')
        game_bt[1][1].configure(fg_color='#ff9d3c')
        game_bt[2][0].configure(fg_color='#ff9d3c')
        return True 

    if check_empty() == False : 
        return "tie"
    else : 
        return False

def check_empty(): 
    sapces= 9 
    for i in range(3): 
        for j in range(3):
            if game_bt[i][j].cget("text") != "": 
                sapces-=1 
    if sapces==0 : 
            return False
    else :
            return True
def start_new_game(): 
    global turn
    turn=random.choice(players)
    l1.configure(text=f'{turn} Turn')
    for i in range(3): 
        for j in range(3): 
            game_bt[i][j].configure(text="",fg_color="#1f6aa5")
wind=ck.CTk()
wind.update()
wind.title("tik tak toe")
wind.geometry(f'700x700+100+50')
wind.resizable(False,False)
players=['o','x']
turn=random.choice(players)
game_bt= [  [0,0,0],
            [0,0,0],
            [0,0,0]]
l1=ck.CTkLabel(wind,text=f'{turn} Turn',font=('Ink Free',40))
l1.place(x=300,y=30)
restart_button =ck.CTkButton(wind,text="Restart" ,font=("Ink Free",20),width=200,command=start_new_game)
restart_button.place(x=250 ,y=100)
btn_frame=ck.CTkFrame(wind,width=690,height=520)
btn_frame.place(x=5 ,y=170)
for i in range(3): 
    for j in range(3) : 
        game_bt[i][j]=ck.CTkButton(btn_frame,text="",font=('Ink free',40),width=220, height=150,command=lambda row=i, col=j: next_turn(row, col))
        game_bt[i][j].grid(row=i, column=j, padx=5, pady=5)

wind.mainloop()