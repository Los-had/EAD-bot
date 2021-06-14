from pyautogui import *
from time import sleep
from random import choice
import sys

import pyautogui

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

if userchoice == "s":
    sys.exit()
elif userchoice == "soe":
    soelink = input("Coloque o link da aula embaixo.\n >  ")
    
else:
    pass