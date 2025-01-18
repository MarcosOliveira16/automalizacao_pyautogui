# pip install pyautogui
import pandas as pd
import pyautogui
import time

# para dar uma pausa entre os comandos
pyautogui.PAUSE = 0.5

# =======================================
# passo 1: abrir o sistema

# apertar a tecla windows
pyautogui.press("win")

# abrir o navegador Edge e em tela cheia
pyautogui.write("edge")

# apertar enter
pyautogui.press("enter")


# entrar no sistema https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

# apertar enter
pyautogui.press("enter")

# pedir para o programa esperar 3 segundos
time.sleep(3)

# =======================================
# passo 2: fazer login

# o comando abaixo foi feito usando o 'auxiliar.py'
# clicar no campo de email
pyautogui.click(x=628, y=498)
# digitar email
pyautogui.write("loginautomacao@projetopython.com")

# pulando para o campo senha
pyautogui.press("tab")

# digitar senha
pyautogui.write("123456")

# pulando para o botão de login
pyautogui.press("tab")

# apertar enter
pyautogui.press("enter")

# =======================================
# passo 3: importar base de dados dos produtos

# pip install pandas openpyxl

# ler uma base de dados csv
tabela = pd.read_csv("produtos.csv")

# exbir a base de dados
print(tabela)

# para garantir q o sistema carregue antes de começarmos a cadastrar
time.sleep(2)

# =======================================
# passo 4: cadastrar um produto

# construir o modelo para preenchimento

# modelo usado na tabela:
# codigo,marca,tipo,categoria,preco_unitario,custo,obs
# MOLO000251,Logitech,Mouse,1,25.95,6.50,
# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=660, y=358)

    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]

    # preencher o campo
    pyautogui.write(str(codigo))

    # passar para o proximo campo
    pyautogui.press("tab")

    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))

    pyautogui.press("tab")
    pyautogui.press("enter")  # cadastra o produto (botao enviar)

    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
# =======================================
# passo 5: repetir o passo 4 até acabar os produtos - feito implementando um loop acima
