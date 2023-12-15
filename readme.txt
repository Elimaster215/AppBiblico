O projeto 'Mensagem biblica' tem como objetivo criar uma aplicação que envie automaticamente um trecho da bibilia aleatorio, escolhido pelo sistema para um numero escolhido numa lista para o whatsapp e telegram.
Utilizamos o openpyxl para abrir o 'banco de dados' onde é armazenado os nomes e telefone das pessoas para qual desejamos mandar as mensagens
A função 'obter_versiculo_biblia' busca no site https://www.abibliadigital.com.br a api responsavel por nos fornecer um capitulo aleatorio para cada usuario
Preparamos a mensagem e colocamos em uma variavel para colocarmos juntos em uma URL que será acessada atravez da função 'webbrowser'
Utilizamos o 'pyautogui' para clicar no "botão" de enviar no whatsapp web
nota-se que usamos 'sleep' em varias partes da aplicação para que o navegador tenha tempo de abrir a pagina e preparar a mensagem
após o envio de uma mensagem a tela do navegador é fechada para inciar um novo envio.
caso não consiga enviar para alguma das pessoas, é inserida numa lista.
