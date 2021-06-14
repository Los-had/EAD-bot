from pyautogui import *
from time import sleep
from random import choice
import sys
import webbrowser

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
* SAIR(s)                                        *
==================================================
'''

print(options)

userchoice = input("O que deseja fazer?\n >  ")
#funções
def vlink(link):
    #opt1 = 'https://'
    opt2 = 'http://'
    if opt2 or opt1 not in link:
        print("Isto não é um link")
        sleep(10)
        sys.exit()
    else:
        webbrowser.open_new_tab(link)
def bot_action(ulink):
    vlink(ulink)
    pyautogui.hotkey("ctrl", "d")
    pyautogui.hotkey("ctrl", "e")
#verificando o que o usuario digitou
if userchoice == "s":
    sys.exit()
elif userchoice == "soe":
    slink = input("Coloque o link da aula embaixo.\n >  ")
    bot_action(slink)
else:
    print("Comando inválido")
    sleep(10)
#made by Los-had
