#Importar dataset no Colab usando Google Drive
##Tutorial
###Passo 1: Importar o Drive para o Colab
Para adicionar seus Drive ao arquivos do collab basta utilizar o seguinte código:
```
from google.colab import drive
drive.mount('/content/drive')
  ```
Feito isso já é possivel visualizar seus arquivos na aba "Arquivos" do colab
###Passo 2: Utilizando o dataset
Na hora de encaminhar o "PATH" de seu dataset é preciso estar atento com algumas adições.
Seu novo PATH será "/content/drive/MyDrive/+caminho_drive", +caminho_drive vai depender de como esta organizado seu drive, escreva os nomes das pastas onde se encontra o dataset e por fim a pasta do dataset.
#### Achando o PATH através do colab
  Se preferir você pode utilizar a aba arquivos do lado para procurar seu Dataset. Dentro da pasta "content" haverá uma pasta "drive" dentro dela é possivel navegar entre seus arquivos e quando chegar na pasta do Dataset, basta clickar com o botão direito e então "Copiar caminho"
