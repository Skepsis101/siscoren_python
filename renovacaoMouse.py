# RENOVAÇÃO

from pickletools import pytuple
from re import sub
import pyautogui
import time
import sys

pyautogui.alert("Renovação iniciada: não mexa no mouse!")

# clique na inscrição
pyautogui.click(59, 61)
time.sleep(1)

# abra a inscrição e cole o CPF no campo CPF
pyautogui.rightClick(851, 560)
time.sleep(0.5)
pyautogui.click(915, 632)

# aperte ENTER 3 vezes (rapidamente)
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.press('enter')
time.sleep(0.5)

# clicar na aba REQUERIMENTO
pyautogui.click(556, 395)
time.sleep(0.5)

# clicar no botão amarelo
pyautogui.click(501, 419)
time.sleep(0.5)

# clicar em incluir requerimento
pyautogui.click(499, 445)
time.sleep(0.5)

# rolar duas vezes para baixo
time.sleep(0.5)
pyautogui.moveTo(698, 590)
time.sleep(0.5)
pyautogui.scroll(-1000)
pyautogui.scroll(-1000)

# clicar em RENOVAÇÃO DEFINITIVA
pyautogui.click(698, 590)

# clicar em DEFINITIVA
pyautogui.click(698, 413)
time.sleep(1)

# rola duas vezes e selecionar FOTO
pyautogui.click(800, 546)
time.sleep(0.5)
pyautogui.scroll(-1000)
pyautogui.scroll(-1000)
pyautogui.scroll(-1000)
time.sleep(0.5)
pyautogui.click(703, 590)


# rolar 3 vezes e selecionar IDENTIDADE e CÉDULA
pyautogui.scroll(-1000)
pyautogui.scroll(-1000)
pyautogui.scroll(-1000)
pyautogui.click(698, 570)
time.sleep(0.5)

# clicar em ENVIAR pelo correio
pyautogui.click(698, 665)
time.sleep(0.5)
pyautogui.click(1102, 687)

# clicar em EMITIR
time.sleep(0.5)
pyautogui.click(1130, 894)

# apertar ENTER e clicar em EMITIR (caso ele peça pelo local de trabalho)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.click(1130, 894)

# clicar na impressora
time.sleep(1.5)
pyautogui.click(207, 34)

# apertar enter
pyautogui.press('enter')
time.sleep(7.5)

# fechar a janela
pyautogui.hotkey('alt', 'f4')
time.sleep(0.5)

# clicar em FECHAR
pyautogui.hotkey('alt', 'f4')
time.sleep(0.5)

# clicar em DOCUMENTOS
pyautogui.click(723, 396)
time.sleep(0.5)

# clicar em incluir documento
pyautogui.click(501, 419)
time.sleep(0.5)
pyautogui.click(503, 464)
time.sleep(0.5)

# digitar pasta de ren e apertar TAB
pyautogui.write('pasta de ren')
pyautogui.press('TAB')

# digitar sub e apertar ENTER
pyautogui.write('sub')
pyautogui.press('TAB')
pyautogui.press('r')

# clicar em situação e digitar aguardando envio para sede
pyautogui.click(1165, 440)
pyautogui.write('aguardando en')
pyautogui.press('down')
pyautogui.press('enter')
time.sleep(0.5)

# apertar TAB e digitar subseção de passo fundo
pyautogui.press('tab')
pyautogui.write('sub')
pyautogui.press('down')
pyautogui.press('down')
time.sleep(0.5)

# apertar TAB 5 vezes e apertar ENTER
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')

# apertar enter 3 vezes
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(2)
pyautogui.press('enter')

# apertar para a esquerda e apertar enter
time.sleep(2)
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(1)

pyautogui.alert("Renovação concluída! Sistema liberado.")
exit()
