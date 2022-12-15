import webbrowser
import pyautogui
from time import sleep
import pyperclip

def mensagem(mensagens):
    pyperclip.copy(mensagens)
    pyautogui.hotkey('ctrl', 'v')

#telefones = [55XX927XXXX, 55XX820XXXX, 55XX817XXXX]

telefones = []

with open('telefones.txt', 'r') as arquivo:
    for linha in arquivo:
        telefones.append(linha.split('\n')[0])
  
for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(10)
    pyautogui.click(920,298, duration=1)
    sleep(5)
    pyautogui.click(676,394, duration=1)
    sleep(8)
    pyautogui.click(920,298, duration=1)
    sleep(5)
    pyautogui.click(2453,701, duration=1)
    mensagem('Bom dia!\nFavor não responder, estou fazendo um teste de mensagens automaticas!')
    sleep(5)
    pyautogui.press('enter')
    sleep(30)