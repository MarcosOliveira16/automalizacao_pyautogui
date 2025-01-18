# Documentação do Projeto de Automalização com PyAutoGUI

Este projeto realiza a automação de tarefas utilizando a biblioteca [PyAutoGUI](https://pyautogui.readthedocs.io/). Ele simula interações com um navegador da web e um sistema para cadastro automático de produtos com base em uma planilha CSV.

## Requisitos

Certifique-se de que os seguintes requisitos estejam instalados em seu ambiente:

### Bibliotecas Python

1. Instale as dependências necessárias com o seguinte comando:

   ```bash
   pip install pyautogui pandas
   ```

2. Certifique-se de ter o [Python](https://www.python.org/downloads/) instalado (versão 3.6 ou superior).

### Arquivos Necessários

- **produtos.csv**: Arquivo CSV contendo os dados dos produtos a serem cadastrados. O modelo do arquivo deve seguir o formato abaixo:
  ```csv
  codigo,marca,tipo,categoria,preco_unitario,custo,obs
  MOLO000251,Logitech,Mouse,1,25.95,6.50,
  ```

## Estrutura do Código

O projeto é dividido em etapas descritas a seguir.

### Passo 1: Abrir o Sistema

1. Simula o pressionamento da tecla **Windows** para abrir o menu iniciar.

2. Digita "edge" e abre o navegador Microsoft Edge.

3. Acessa a URL do sistema:

   ```
   https://dlp.hashtagtreinamentos.com/python/intensivao/login
   ```

4. Aguarda 3 segundos para garantir o carregamento da página.

### Passo 2: Fazer Login

1. Clica no campo de e-mail e insere o seguinte e-mail:

   ```
   loginautomacao@projetopython.com
   ```

2. Usa a tecla **Tab** para navegar até o campo de senha e digita:

   ```
   123456
   ```

3. Pressiona **Tab** para navegar até o botão de login e confirma com **Enter**.

### Passo 3: Importar Base de Dados

1. Lê os dados de um arquivo CSV chamado `produtos.csv` utilizando a biblioteca **Pandas**:

   ```python
   tabela = pd.read_csv("produtos.csv")
   ```

2. Exibe os dados no console com:

   ```python
   print(tabela)
   ```

3. Aguarda 2 segundos antes de iniciar o cadastro.

### Passo 4: Cadastrar Produtos

1. Percorre todas as linhas da tabela para realizar o cadastro automático de cada produto:

   - Clica no campo correspondente a cada informação (ex.: código, marca, tipo).
   - Digita os valores diretamente da planilha CSV.
   - Se o campo **obs** estiver vazio, ele será ignorado.

2. Realiza o envio do cadastro pressionando **Enter** após preencher todos os campos.

3. Ajusta a visualização da página com `pyautogui.scroll(5000)` para garantir que todos os campos estejam visíveis.

### Passo 5: Repetir o Cadastro

O loop percorre todas as linhas do arquivo `produtos.csv` até que todos os produtos sejam cadastrados.

## Configurações Adicionais

### Tempo de Pausa

A propriedade `pyautogui.PAUSE = 0.5` garante uma pausa de 0,5 segundos entre cada comando para evitar erros causados pela velocidade de execução.

### Fail-Safe

O recurso `pyautogui.FAILSAFE = True` permite interromper a automação movendo o mouse para o canto superior esquerdo da tela.

### Coordenadas Fixas

Os valores de `x` e `y` usados em `pyautogui.click(x=..., y=...)` dependem da resolução da tela e podem precisar ser ajustados.

Para identificar as coordenadas corretamente, utilize o script auxiliar da biblioteca **PyAutoGUI**.

## Exemplo de Execução

1. Garanta que o arquivo `produtos.csv` está na mesma pasta do script.

2. Execute o script:

   ```bash
   python automacao.py
   ```

3. Verifique os cadastros no sistema.

## Avisos

- A automação por coordenadas pode ser frágil, caso a interface do sistema ou a resolução da tela mudem.
- Certifique-se de que nenhum outro programa interfira durante a execução do script.

---

Este projeto foi criado com o intuito de demonstrar a utilização do PyAutoGUI para automação de tarefas repetitivas.

Feito com base na aula 1 da "Jornada Python da Hashtag".
