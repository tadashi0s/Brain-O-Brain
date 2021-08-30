#welcome screen
def introduction():
  for i in range(0,44):print("*",end="*")
  print("\n..................................WELCOME TO THE QUIZ...............................")
 
  print("\n***************************** INSTRUCTIONS TO PLAY THE GAME*************************")

  print("\n 1) enter your name ")

  print("\n 2) enter 'Y' to start the quiz or 'N' to exit .")

  print("\n 3) your quiz will began and now play the game.")

  print("\n 4) total 15 questions will be displayed(one by one) along with there four options ")

  print("\n 5) you have to choose any one option among the four given options")

  print("\n 6) at the last you will be rewarded marks according to your correct answers")

 
def welcome():
  for i in range(0,44):print("*",end="*")

  print("\n..................................WELCOME TO THE QUIZ...............................")

  pname=input("enter your name : ")

  print(" to start the quiz 'Y' and to exit 'N'")

  ch=input()

  if ch=='y' or ch=='Y':

    print(pname,"your quiz has begin :")

  else:
    print(pname,"good bye , Have a nice day ")

    exit(0)

  for i in range(0,44):print("*",end="*")


def quiz():
  q=[]
  q.append("\n Q) A light sensitive device that converts   drawing,printed text or other images into digital form     is  ?")
  q.append("\n Q) which protocol provides e-mail facility   among different hosts?")
  q.append("\n Q) The basic architecture of computer was   developed by ?")
  q.append("\n Q) In order to tell Excel that we are   entering a formula in cell, we must begin with an   operator   such as ?")
  q.append("\n Q) In how many generations a computer   can be classified?")
  q.append("\n Q) fifth generation computers are based on   ")
  q.append("\n Q) first generation computers are based on  ")
  q.append("\n Q) microprocessors was introduced in which generation of computer ")
  q.append("\n Q) which of the following memory is non-volatile")
  q.append("\n Q) GUI stand for ")
  q.append("\n Q) time during which a job is processed by the computer is ")
  q.append("\n Q) which of the following circuit is used   as a 'memory device' in computers ")
  q.append("\n Q) which one of the following is not an   application software package") 
  q.append("\n Q) who invented the supercomputer")
  q.append("\n Q) the size of commonly used floppy disk")
  
  opta=[]
  opta.append("a) keyboard")
  opta.append("a) FTP")
  opta.append("a) John Von Neumann")
  opta.append("a) $ ")
  opta.append("a) 3")
  opta.append("a) Artifical intelligence ")
  opta.append("a) Transtiors ")
  opta.append("a) second")
  opta.append("a) SRAM")
  opta.append("a) graph use interface")
  opta.append("a) execution time ")
  opta.append("a) rectifiers ")
  opta.append("a) red hat linux")
  opta.append("a) Seymour cray")
  opta.append("a) 4.5")
  
  optb=[]
  optb.append("b) plotter")
  optb.append("b) SMTP")
  optb.append("b) Charles Babbage")
  optb.append("b) @")
  optb.append("b) 4")
  optb.append("b) programming intelligence ")
  optb.append("b)  LSI")
  optb.append("b) fourth")
  optb.append("b) DRAM")
  optb.append("b) graphical universal interface")
  optb.append("b) delay time")
  optb.append("b) flip flop")
  optb.append("b) MS office")
  optb.append("b) charles babbage")
  optb.append("b) 3.5")


  optc=[]
  optc.append("c) scanner")
  optc.append("c) TELNET")
  optc.append("c) Blaise Pascal")
  optc.append("c) +")
  optc.append("c) 5")
  optc.append("c) system knowledge ")
  optc.append("c) VLSI")
  optc.append("c) third")
  optc.append("c) ROM")
  optc.append("c) graphical user interface")
  optc.append("c) real time ")
  optc.append("c) comparators")
  optc.append("c) open office ")
  optc.append("c) JH Van Tassell")
  optc.append("c) 3.25")
  

   optd=[]
  optd.append("d) OMR \n")
  optd.append("d) SNMP \n")
  optd.append("d) Garden Moore \n")
  optd.append("d) =\n")
  optd.append("d) 6\n")
  optd.append("d)none of these \n") 
  optd.append("d) vaccum tube  \n") 
  optd.append("d) All of these \n") 
  optd.append("d) None of these \n") 
  optd.append("d) None of these \n") 
  optd.append("d) waiting time \n") 
  optd.append("d) attenuator\n") 
  optd.append("d) adobe pagemaker \n") 
  optd.append("d) charles ginsberg  \n") 
  optd.append("d) 5.5\n") 


  keys=["c","b","a","d","c","a","d","b","c","c","a","b","a","a",]
  
  print("your questions are as follows : ")
  score=0
  from itertools import permutations 
  perm = permutations([ 0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ]) 
  mylist=list(perm)
   
  import random
  ran=random.choice([int(x) for x in range(120)]) 
  for i in list(mylist[ran]):
    print(q[i])
    print(opta[i])
    print(optb[i])
    print(optc[i])
    print(optd[i])
    print("enter the correct option(a,b,c,d) :")
    ans=input()
    if ans==keys[i]:
      score+=1
  print("yous score is ",score)

introduction()
welcome()
quiz()
