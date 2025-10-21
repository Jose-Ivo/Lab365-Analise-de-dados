import pandas as pd

# Lendo os arquivos com o PANDAS

produtos = pd.read_csv("produtos.csv")
pedidos = pd.read_csv("pedidos.csv")
clientes = pd.read_csv("clientes.csv")

# Visualização dos dados com .head()

produtos.head()
pedidos.head()
clientes.head()

# Fazendo a verificação de tipos nulos com .info() e isnull.sum()

produtos.info()
produtos.isnull().sum()

pedidos.info()
pedidos.isnull().sum()

clientes.info()
clientes.isnull().sum()

# Obtendo estatisticas descritivas

produtos.describe()

pedidos.describe()

clientes.describe()