# pokIEEEdex
Rede Neural identificadora de Pokémons

## Importando datasets do Kaggle no Google Colab:
Este mesmo tutorial pode ser encontrado [nesta página do Kaggle](https://www.kaggle.com/general/74235) (em inglês).
Para pular o tutorial e/ou copiar todas as linhas num bloco só, desça até o fim da página clicando [aqui](#todos-os-comandos).

## Tutorial
### 1. Obter um Token
- Crie uma conta no Kaggle (você pode fazer log in com a conta Google)
- Acesse a página de configurações de sua conta
- Procure pela seção "API"
- Clique em "Expire API Token" para remover possíveis tokens antigos
- Clique em "Create New API Token" para fazer download do arquivo _kaggle.json_ localmente no seu computador.
### 2. Configurar o ambiente
Dentro do seu projeto no Google Colab, execute os seguintes comandos:

Para instalar a biblioteca que lida com Kaggle:
>```! pip install -q kaggle```

Para importar a biblioteca que lida com arquivos no ambiente do Google Colab:
>```from google.colab import files```

Para fazer upload de um arquivo ao ambiente:
>```files.upload()```

Quando este comando for executado, será pedido que você selecione um arquivo para upload. Você deve subir o arquivo _kaggle.json_ que foi previamente baixado.

Para criar uma pasta (diretório) com nome _kaggle_:
>```! mkdir ~/.kaggle```

Copiar o arquivo selecionado na pasta criada:
>```! cp kaggle.json ~/.kaggle/```

Para mudar as permissões do arquivo:
>```! chmod 600 ~/.kaggle/kaggle.json```

Listar os arquivos na pasta _kaggle/datasets/_ e verificar visualmente se tudo deu certo.
>```! kaggle datasets list```

Agora você configurou seu ambiente do Google Colab para importar datasets diretamente do Kaggle.

### 3. Baixar um dataset escolhido
Execute os seguintes comandos:
Para baixar o dataset na pasta escolhida:
>```! kaggle <folder> download -d <path>/<dataset-name>```

Por exemplo, se eu encontrei um dataset cujo link é https://www.kaggle.com/thedagger/pokemon-generation-one, e pretendo baixá-lo para uma pasta chamada _datasets_, o comando fica:
>```! kaggle datasets download -d thedagger/pokemon-generation-one```

Assim, o arquivo será adicionado ao diretório virtual do seu ambiente no Google Colab (ou seja, as pastas do Colab) em formato _.zip_.

### 4. Descompactar e extrair os dados
>```! unzip <file-name> -d <folder-name>```

O comando ```unzip``` descompacta arquivos em formato _.zip_. Por exemplo, podemos criar um diretório chamado _train_:
>```! mkdir train```

Para extrair o conteúdo do arquivo _train.zip_ na pasta _train_:
>```! unzip train.zip -d train```

## Todos os comandos
```
# setup
! pip install -q kaggle
from google.colab import files
files.upload()
! mkdir ~/.kaggle
! cp kaggle.json ~/.kaggle/
! chmod 600 ~/.kaggle/kaggle.json

# download data
! kaggle datasets list
! kaggle datasets download -d thedagger/pokemon-generation-one

# unzip data
! mkdir train
! unzip train.zip -d train
```
