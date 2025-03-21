import pyautogui
import pandas as pd
import time

# Configura o tempo de espera entre as ações
pyautogui.PAUSE = 1

# Lê o Monitor 24 Polegadas
produtos = pd.read_csv('automacao/produtos.csv')

# Abre o Chrome e o site (você pode mudar essa parte para abrir o site direto)
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")
time.sleep(3)  # Espera o Chrome abrir
pyautogui.write("http://127.0.0.1:5500/main.html")  # Coloca o endereço do site
pyautogui.press("enter")

print("Você tem 10 segundos para posicionar na tela de cadastro...")
time.sleep(10)

# Loop para cada produto
for index, produto in produtos.iterrows():
    pyautogui.click(x=1383, y=189)
    # Preenche o nome
    pyautogui.write(str(produto['Nome']))
    pyautogui.press('tab')
    
    # Preenche a descrição
    pyautogui.write(str(produto['Descricao']))
    pyautogui.press('tab')
    
    # Preenche o preço
    pyautogui.write(str(produto['Preco']))
    pyautogui.press('tab')
    
    # Preenche a categoria
    pyautogui.write(str(produto['Categoria']))
    pyautogui.press('tab')
    
    # Simula clique no botão "Cadastrar"
    pyautogui.click(x=2541, y=528)  # Ajuste a posição para o botão correto

    # Espera um pouco antes do próximo
    time.sleep(2)

print("Cadastro finalizado!")
