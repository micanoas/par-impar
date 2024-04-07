a) import pandas as pd
tabela = pd.read_excel(r"C:\Users\paulo\Desktop\Michelle\dados.xlsx")
coluna = int(input("Digite a coluna:"))
resultado = coluna % 2
if resultado == 0:
    print("Coluna Par")
else:
    print("Coluna Ímpar")





 b)   import pandas as pd
tabela = pd.read_excel(r"C:\Users\paulo\Desktop\Michelle\dados.xlsx")
linha = int(input("Digite a coluna:"))
resultado = linha % 2
if resultado == 0:
    print("Linha Par")
else:
    print("Linha Ímpar")
 
