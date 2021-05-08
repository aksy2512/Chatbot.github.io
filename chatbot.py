from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
from flask import Flask, render_template, request






#trains the AI
chatbot = ChatBot('tutor')
trainer = ListTrainer(chatbot)

# for _file in os.listdir('txt'):
#     chats = open('txt/' + _file, 'r').readlines()

#     trainer.train(chats)
chats = open("Database.txt", "r").readlines()
trainer.train(chats)

trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    "chatterbot.corpus.english"
)

#t = True
#while(t):
 #   request = input('You:')
#     response = bot.get_response(request)

#     print('Bot:' , response)  
def respond(event):
     re = ue.get()

     res = chatbot.get_response(re)
     be.config(state=NORMAL)

     be.delete(1.0,'end')
     ue.delete(0, 'end')

     be.insert(1.0, res)
     be.config(state=DISABLED)


r=tk.ThemedTk()
r.get_themes()
r.set_theme('adapta')
r.title("Chatbot")
r.iconbitmap("favicon.ico")

ue = ttk.Entry(r)
l = ttk.Label(r,text='')
be =Text(r,width=150,height=50)
sb=ttk.Button(r, text ='Enter')
sb.bind("<Button-1>", respond)
bl = ttk.Label(r,text ='Bot:')
ul = ttk.Label(r, text = 'User:')







sb.grid(row=0, column=3)
be.grid(row=4, column=2)
l.grid(row=3, column=2)
ue.grid(row=0,column=2)
bl.grid(row=4,column=1)
ul.grid(row=0 , column=1)

r.mainloop()

 
 