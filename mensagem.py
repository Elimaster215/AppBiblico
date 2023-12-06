import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui
import requests

#robo abre whatsapp para cliente logar com uma pausa de 30 segundos
webbrowser.open('https://web.whatsapp.com/')
sleep(30)

#robo abre o arquivo xml e recolhe as informações do cliente
workbook = openpyxl.load_workbook('clientes.xlsx')
pagina_clientes = workbook['Sheet1']



for linha in pagina_clientes.iter_rows(min_row=2):
    nome = linha[0].value
    telefone = linha[1].value
    
    # robo busca um versiculo aleatorio na API da Biblia Digital
    def obter_versiculo_biblia():
        url = "https://www.abibliadigital.com.br/api/verses/nvi/random"
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()
            livro = dados["book"]["name"]
            capitulo = dados["chapter"]
            versiculo_numero = dados["number"]
            versiculo_texto = dados["text"]
            return livro, capitulo, versiculo_numero, versiculo_texto
        else:
            return "Erro ao obter o versículo da Bíblia"

    # Exemplo de uso
    livro, capitulo, versiculo_numero, versiculo_texto = obter_versiculo_biblia()
    
    #robo escreve a mensagem e preparar para o envio
    mensagem = f'Olá {nome}. Versículo biblíco do dia:  {livro} {capitulo}:{versiculo_numero} - {versiculo_texto}'
    
    #link para o envio e aberto do site

    del livro, capitulo, versiculo_numero, versiculo_texto

    try:
        link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
        webbrowser.open(link_mensagem_whatsapp)

        sleep(10)
    
        seta = pyautogui.locateCenterOnScreen('seta.png')
        sleep(5)
        pyautogui.click(seta[0],seta[1])
        sleep(5)
        pyautogui.hotkey('Ctrl','w')
        sleep(5)
    except:
        print(f'Não foi possivel enviar mensagem para {nome}')
        with open('erros.csv', 'a',newline='',encoding='utf-8')as arquivo:
            arquivo.write(f'{nome},{telefone}')