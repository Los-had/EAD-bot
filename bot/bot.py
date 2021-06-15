import pyautogui
from time import sleep
from random import choice, random, shuffle
import sys
import webbrowser
import os

bot_logo = '''
      \_/
     (* *)
    __)#(__
   ( )...( )(_)
   || |_| ||//     EAD-bot
>==() | | ()/
    _(___)_
   [-]   [-]
'''

options = '''
==================================================
* SOE (soe)                                      *
* MAT.1 (m1)                                     *
* MAT.2 (m2)                                     *
* PORTUGUÊS (p)                                  *
* INGLÊS (i)                                     *
* REDAÇÃO (r)                                    *
* OFICINA DE INGLÊS (oi)                         *
* OFICINA DO CORPO (oc)                          *
* HISTÓRIA (h)                                   *
* ARTES (a)                                      *
* DESAFIOS GLOBAIS (dg)                          *
* GEOGRAFIA (g)                                  *
* EDUCAÇÃO FÍSICA (ef)                           *
* MÚSICA (m)                                     *
* FILOSOFIA (f)                                  *
* QUIMICA (q)                                    *
* BIOLOGIA (b)                                   *
* FISICA (fis)                                   *
* SAIR(s)                                        *
==================================================
'''

print(bot_logo)
print(options)

userchoice = input("O que deseja fazer?\n >  ")
#funções
def vlink(link):
    #opt1 = 'https://'
    meet_link = 'https://meet.google.com/'
    if meet_link not in link:
        print("Isto não é um link do meet! Tente novamente =(")
        sleep(10)
        sys.exit()
    else:
        webbrowser.open_new_tab(link)
def bot_action(ulink):
    vlink(ulink)
    opt_msg = ['Bom dia.', 'Qual e o dever de hoje.', 'Qual e a pagina do livro.', 'Tudo bem.', 'Que legal.', 'Oi.']
    msg_choice = choice(opt_msg)
    pyautogui.sleep(15)
    pyautogui.hotkey("ctrl", "d")
    pyautogui.sleep(1)
    pyautogui.hotkey("ctrl", "e")
    pyautogui.sleep(1)
    pyautogui.click(x = 1025, y = 515, clicks=1)
    pyautogui.sleep(10)   
    pyautogui.hotkey("ctrl", "alt", "c")
    pyautogui.sleep(2)
    pyautogui.typewrite(msg_choice)
    pyautogui.sleep(1)
    pyautogui.press("enter")
    pyautogui.sleep(1)
    pyautogui.press("esc")
#verificando o que o usuario digitou
if userchoice == "s":
    usr_choice = input("Tem certeza que quer sair?(y/n)\n >  ")
    if usr_choice == "y":
        sys.exit()
    elif usr_choice == "n":
        print(userchoice)
    else:
        print('Comando inválido =(')
elif userchoice == "soe":
    slink = input("Coloque o link da aula embaixo.\n >  ")
    bot_action(slink)
elif userchoice == "m1":
    slink = input("Coloque o link da aula embaixo.\n >  ")
    bot_action(slink)
elif userchoice == "m2":
    slink = input("Coloque o link da aula embaixo.\n >  ")
    bot_action(slink)
elif userchoice == "p":
    slink = input("Coloque o link da aula embaixo.\n >  ")
    bot_action(slink)
elif userchoice == "i":
    slink = input("Coloque o link da aula embaixo.\n >  ")
    bot_action(slink)
elif userchoice == "oi":
    slink = input("Coloque o link da aula embaixo.\n >  ")
    bot_action(slink)
elif userchoice == "oc":
    slink = input("Coloque o link da aula embaixo.\n >  ")
    bot_action(slink)
elif userchoice == "h":
    slink = input("Coloque o link da aula embaixo.\n >  ")
    bot_action(slink)
elif userchoice == "a":
    slink = input("Coloque o link da aula embaixo.\n >  ")
    bot_action(slink)
elif userchoice == "dg":
    slink = input("Coloque o link da aula embaixo.\n >  ")
    bot_action(slink)
elif userchoice == "g":
    slink = input("Coloque o link da aula embaixo.\n >  ")
    bot_action(slink)
elif userchoice == "ef":
    slink = input("Coloque o link da aula embaixo.\n >  ")
    bot_action(slink)
elif userchoice == "m":
    slink = input("Coloque o link da aula embaixo.\n >  ")
    bot_action(slink)
elif userchoice == "f":
    slink = input("Coloque o link da aula embaixo.\n >  ")
    bot_action(slink)
elif userchoice == "q":
    slink = input("Coloque o link da aula embaixo.\n >  ")
    bot_action(slink)
elif userchoice == "b":
    slink = input("Coloque o link da aula embaixo.\n >  ")
    bot_action(slink)
elif userchoice == "fis":
    slink = input("Coloque o link da aula embaixo.\n >  ")
    bot_action(slink)
else:
    print("Comando inválido")
    sleep(10)
#made by Los-had
sleep(1)
print('Made by Los-had')
sleep(5)
