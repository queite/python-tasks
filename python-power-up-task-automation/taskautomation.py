# Entrar no sistema da empresa https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Fazer login
# Importar base de produtos para cadastrar
# Cadastrar produto
# Repetir cadastro até o fim
import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.3

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(x=499, y=390)
pyautogui.write("teste@gmail.com")
pyautogui.press("tab")
pyautogui.write("teste")
pyautogui.click(x=656, y=554)
pyautogui.press("enter")
time.sleep(3)

df = pd.read_csv("produtos.csv")

for line in df.index:
    pyautogui.click(x=609, y=313)
    pyautogui.write(str(df.loc[line, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(df.loc[line, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(df.loc[line, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(df.loc[line, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(df.loc[line, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(df.loc[line, "custo"]))
    pyautogui.press("tab")
    obs = df.loc[line, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
