from script import * #importar dados do documento anterior
import zipfile #importar a biblioteca de zip


drive.close() #fechar a janela do chrome
#extrair arquivo
extrair = zipfile.ZipFile('/Users/brunopessi/Downloads/beer-consumption-sao-paulo.zip') #caminho da pasta zip
extrair.extract('Consumo_cerveja.csv', '/Users/brunopessi/Desktop') #extrair o arquivo
extrair.close() #fechar o arquivoaU