#Foundation English(FE),Score(S),Average score per ques.(A), Midterm score = 35/100 Ques.
#Part 1 = 3 score (5 Questions),Part 2 = 15 score (45 Ques.),Part 3 = 17 score (50 Ques,)
FEASP1 = 3/5
FEASP2 = 15/45
FEASP3 = 17/50

#General Business(GB),Score(S),Average score per ques.(A), Midterm score = 35/90 Ques.
#Part 1 = 20 score (50 Ques.), Part 2 = 15 score (40 Ques.)
GBASP1 = 20/50
GBASP2 = 15/40

#Introduction to Computer System(IC),Score(S),Average score per ques.(A)
#Midterm score = 30/120 Ques.
#Part 1 = 30 score (120 Ques.)
ICASP1 = 30/120

#Computer Programming(CP),Score(S),Average score per ques.(A),Midterm score = 30/100 Ques.
#Part1 = 15 score (50 Ques.), Part 2 = 15 score (50 Ques)
CPASP1 = 15/50
CPASP2 = 15/50

print('-----------', 'Your Score', '----------')
print('Foundation English   : ',(5*FEASP1)+(30*FEASP2)+(35*FEASP3))
print('General Business     : ', (42*GBASP1)+(30*GBASP2))
print('Introduction to Computer System : ',(95*ICASP1))
print('Computer Programming : ', (32*CPASP1)+(35*CPASP2))
