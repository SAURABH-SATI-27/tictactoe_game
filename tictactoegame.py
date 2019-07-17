def welcome():
    print(".....................WELCOME  TO  TIC  TAC  TOE...................")
    print("""
                   1 | 2 | 3                          this is  the format of marker 
                   4 | 5 | 6                          location , press the number 
                   7 | 8 | 9                          where you want to print your
                                                            mark """)
    print("                                                       ")
    n= input("type start to start game :: ")
    n=n.lower()
    if n=='start':
    
        m1=input("player1 please choose your marker either 'X' or 'O'  ")
        if m1=='X':
            m2='O'
        if m1=='O':
            m2='X'
        brain(m1,m2)    
         
    
        
def replay(m1,m2):
    print("                     ")
    m=input("if you want to play it again type Yes  else No :: ")
    print("                     ")
    m=m.lower()
    if m=='yes':
        brain(m1,m2)
    if m=='no':
        print('ok bye')
                         
                  
def brain(m1,m2):
    i=0
    
    tie=0
    box=['* ', '* ', '* ' ,'* '  ,'* ', '* ' ,'* ' ,'* ' , '* ' ]
    while(tie == 0):

        if tie > 1:
            break
        print("  ")
        p1=int(input("enter the marker location player1 :: "))
        print("    ")
        p2=int(input("enter the marker location player2 :: "))
    
        i+=1
    
        box[p1-1]= m1
        box[p2-1]= m2

    
        print('                                                  ')
        print (box[0] ,'|',box[1] , '|' , box[2])
        print (box[3] ,'|',box[4] , '|' , box[5])
        print (box[6] ,'|',box[7] , '|' , box[8])
        print ('                                                 ')

     
        # for coloumns
        if (box[0]==box[3]==box[6]=='O') or (box[0]==box[3]==box[6]=='X') :
        
            if box[0]=='X':
                print('player 1 wins')
                tie+=1
            else:
                print('player 2 wins')
                tie+=1
                         
        if (box[1]==box[4]==box[7]=='O')or(box[1]==box[4]==box[7]=='X'):
        
            if box[1]=='X':
                tie+=1
                print('player 1 wins')
            else:
                tie+=1
                print('player 2 wins')
            
        
        if (box[2]==box[5]==box[8]=='O')or(box[2]==box[5]==box[8]=='X'):
        
            if box[2]=='X':
                print('player 1 wins')
                tie+=1
            else:
                print('player 2 wins')
                tie+=1
            
        
            # for rows
        if (box[6]==box[7]==box[8]=='X') or (box[6]==box[7]==box[8]=='O'):
            i+=1
            if box[6]=='X':
                print('player 1 wins')
                tie+=1
            else:
                print('player 2 wins')
                tie+=1
                    
        if (box[0]==box[1]==box[2]=="X")or(box[0]==box[1]==box[2]=="O"):
            i+=1
            if box[6]=='X':
                print('player 1 wins')
                tie+=1
            else:
                print('player 2 wins')
                tie+=1
            
        if (box[3]==box[4]==box[5]=='X') or (box[3]==box[4]==box[5]=='O'):
            i+=1
            if box[6]=='X':
                print('player 1 wins')
                tie+=1
            
            else:
                print('player 2 wins')
                tie+=1
            
                # for diagonals

        if (box[0]==box[4]==box[8]=='X') or (box[0]==box[4]==box[8]=='O'):
            i+=1
            if box[0]=='X':
                print('player 1 wins')
                tie+=1
            else:
                print('player 2 wins')
                tie+=1
            
        if (box[2]==box[4]==box[6]=='X') or (box[2]==box[4]==box[6]=='O'):
            i+=1
            if box[6]=='X':
                print('player 1 wins')
                tie+=1
            else:
                print('player 2 wins')
                tie +=1
        if tie>1:
            break

     #for tie;
    if  tie==0:
        print('           ')
        print('Its a tie')
    # for replay
    replay(m1,m2)

welcome()

