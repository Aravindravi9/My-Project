
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 23:17:36 2020

@author: Aravind
"""
import requests
import json 
import random


print("Quiz game")
r=requests.get("https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=boolean")
#print(r.status_code)
dict=json.loads(r.text)
#pprint.pprint(dict)
#print(dict['results'][0])
correct=0
rnd=1
print("Anser the following True or false")
while True:
     while True:
         print("Round",rnd)
         index=random.randint(0,9)
         while True:
             
             ans=input(dict['results'][index]['question']  )
             if(ans.lower() =='true' or ans.lower()=='false'):
                 break                 
             else:
                 print("Invalid answer, Please choose True or False")
                 continue
         if (ans.lower()==dict['results'][index]['correct_answer'].lower()):
             print("you got it right")
             correct =correct+ 1
             break
         else:
              print("you got it Wrong")
              break
     rep=input("Do you want to continue?")
     if(rep.lower()=="yes"):
         rnd =rnd+1
         continue
     else:
         break
              
          
print("Total correct",correct)
         
         
