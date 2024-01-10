import pyautogui
import time 
import pandas 

pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=510, y=374)
pyautogui.write("python.dev@gmail.com")
pyautogui.press("tab")
pyautogui.write("minha senha")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)


tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:

    pyautogui.click(x=462, y=259)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write()
        
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)