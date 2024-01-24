import yfinance as yf
import pyautogui
import pyperclip

#buscar as empresas automaticamente
ticker = input("Digite o código da empresa: ")
periodo = input("Digite o periodo que deseja ver: ")
email=input("Digite o email que deseja enviar: ")

dados = yf.Ticker(ticker).history(periodo)
fechamento = dados.Close

#analise solicitadas pelo gestor
maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
atual = round(fechamento[-1], 2)


#enviar o e-mail automaticamente
#pausa de dois segundos entre os passos
pyautogui.PAUSE = 4

#abrir navegador
pyautogui.click(x=771, y=740)

#abrir uma nova aba(ctr + t)
pyautogui.hotkey("ctrl", "t")

# digitar o gmail e dar um enter
pyperclip.copy("www.gmail.com")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")

#clicar no botao escrever
pyautogui.click(x=117, y=189)

#digitar os dados do email
pyperclip.copy(email)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

pyperclip.copy("Análises diárias")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

mensagem=f"""
Prezado Gestor,

Segue, conforme solicitado, as análises dos últimos {periodo} da ação {ticker}:
 
 Contação máxima: R$ {maxima}
 Cotação mínima: R$ {minima}
 Cotação atual: R$ {atual}
 
 Qualquer dúvida, fico à disposição!
 
 Atte.
 Adryanno Roque
 """

pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")
pyautogui.click(x=841, y=689)
print("E-mail enviado com sucesso")