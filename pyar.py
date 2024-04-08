import pyautogui

n = int(input())

for i in range(1,n+1):

    pyautogui.typewrite('#'*i + '\n')
    



