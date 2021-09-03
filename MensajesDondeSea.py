# -*- coding: utf-8 -*-
"""
@author: mafervicas
"""

import pyautogui, time

time.sleep(7)


for i in range(5):
    pyautogui.typewrite("Vales mil x" + str(i+1))
    pyautogui.press('enter')
    #Solo en Messenger y Teams
    time.sleep(1) 