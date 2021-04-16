import requests
import time
import json
import os


class TelegramBot:
    def __init__(self):
        token = '1712093415:AAHRy95VEKP8uvoJBHOqh_KyX81F8c-5s4U'
        self.url_base = f'https://api.telegram.org/bot{token}/'

    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_novas_mensagens(update_id)
            dados = atualizacao["result"]
            if dados:
                for dado in dados:
                    update_id = dado['update_id']
                    mensagem = str(dado["message"]["text"])
                    chat_id = dado["message"]["from"]["id"]
                    eh_primeira_mensagem = int(
                        dado["message"]["message_id"]) == 1
                    resposta = self.criar_resposta(
                        mensagem, eh_primeira_mensagem)
                    self.responder(resposta, chat_id)

    # Obter mensagens
    def obter_novas_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)

    # Criar uma resposta
    def criar_resposta(self, mensagem, eh_primeira_mensagem):
        if eh_primeira_mensagem == True or mensagem in ('menu', 'Menu'):
            return f'''Olá, tudo bem?

Deixa eu me apresentar \U0001F64B\U0000263A

Meu nome é Robert Brayner, sou graduado em educação musical e pós graduado em docência na educação superior.

Salva ai o meu contato.

Já salvou ?
Ótimo!!! \U0000263A\U0001F44F
            
Esse é meu atendimento eletrônico.


\U0001F4CD Digite o número de uma das opções, para melhor atendê-lo!

MENU:

1 - \U0001F3B8 Informações sobre aula de violão 

2 - \U0001F3B9 Informações sobre aula de teclado

3 - \U0001F3A4 Informações sobre aula de canto

4 - \U0001F4D5 Informações sobre teoria musical

5 - \U0001F468\U0000200D\U0001F3EB Falar diretamente com professor

6 - \U0000260E Redes Sociais'''#menu normal


        if mensagem == '1':
                return f'''\U0001F3B8 1 Aluno:

\U00002714 1 vez por semana/50 min cada aula
\U00002714 R$80,00 por mês (manhã ou tarde)
\U00002714 R$100,00 por mês (noite)


\U0001F3B8 2 Alunos:

\U00002714 Ao mesmo tempo.
\U00002714 1 vez por semana/50min cada aula
\U00002714 R$150,00 por mês (manhã ou tarde)
\U00002714 R$170,00 por mês (noite)


\U0001F3B8 3 Alunos:

\U00002714 Ao mesmo tempo.
\U00002714 1 vez por semana/50min cada aula.
\U00002714 R$180,00 por mês (manhã ou tarde)
\U00002714 R$200,00 por mês (noite).


\U0001F3B8 4 Alunos ou mais:

\U00002714 Ao mesmo tempo.
\U00002714 1 vez por semana/50min cada aula
\U00002714 R$50,00 por mês cada aluno (manhã ou tarde)
\U00002714 R$60,00 por mês por aluno (noite)


\U0001F6A8\U0001F6A8 OBS: CASO FOR FAZER DUAS AULAS POR SEMANA, O VALOR IRÁ DOBRAR

\U0001F6A8\U0001F6A8 O PAGAMENTO È FEITO SEMPRE NA PRIMEIRA AULA E AS AULAS SÃO DE SEGUNDA À SEXTA



\U00002705 QUER SABER O QUE IRÁ APRENDER NAS AULAS DE VIOLÃO? DIGITE: SIMV'''
        elif mensagem == '2':
            return f'''\U0001F3B9 1 Aluno:

\U00002714 1 vez por semana/50 min cada aula
\U00002714 R$130,00 por mês (manhã ou tarde)
\U00002714 R$150,00 por mês (noite)


\U0001F3B9 2 Alunos:

\U00002714 Ao mesmo tempo.
\U00002714 1 vez por semana/50min cada aula
\U00002714 R$100,00 por mês (manhã ou tarde)
\U00002714 R$120,00 por mês (noite)


\U0001F3B9 3 Alunos:

\U00002714 Ao mesmo tempo.
\U00002714 1 vez por semana/50min cada aula
\U00002714 R$90,00 por mês (manhã ou tarde)
\U00002714 R$110,00 por mês (noite)


\U0001F3B9 4 Alunos ou mais:

\U00002714 Ao mesmo tempo.
\U00002714 1 vez por semana/50min cada aula
\U00002714 R$70,00 por mês cada aluno (manhã ou tarde)
\U00002714 R$90,00 por mês por aluno (noite)


\U0001F6A8\U0001F6A8 OBS: CASO FOR FAZER DUAS AULAS POR SEMANA, O VALOR IRÁ DOBRAR

\U0001F6A8\U0001F6A8 O PAGAMENTO È FEITO SEMPRE NA PRIMEIRA AULA E AS AULAS SÃO DE SEGUNDA À SEXTA



\U00002705 QUER SABER O QUE IRÁ APRENDER NAS AULAS DE TECLADO? DIGITE: SIMT'''
        elif mensagem == '3':
            return f'''\U0001F3A4 1 Aluno:

\U00002714 1 vez por semana/50 min cada aula
\U00002714 R$130,00 por mês (manhã ou tarde)
\U00002714 R$150,00 por mês (noite)


\U0001F3A4 2 Alunos:

\U00002714 Ao mesmo tempo.
\U00002714 1 vez por semana/50min cada aula
\U00002714 R$200,00 por mês (manhã ou tarde)
\U00002714 R$220,00 por mês (noite)


\U0001F3A4 3 Alunos:

\U00002714 Ao mesmo tempo.
\U00002714 1 vez por semana/50min cada aula.
\U00002714 R$180,00 por mês (manhã ou tarde)
\U00002714 R$200,00 por mês (noite)


\U0001F3A4 4 Alunos ou mais:

\U00002714 Ao mesmo tempo.
\U00002714 1 vez por semana/50min cada aula
\U00002714 R$50,00 por mês cada aluno (manhã ou tarde)
\U00002714 R$70,00 por mês por aluno (noite)

\U0001F6A8\U0001F6A8 OBS: CASO FOR FAZER DUAS AULAS POR SEMANA, O VALOR IRÁ DOBRAR

\U0001F6A8\U0001F6A8 O PAGAMENTO È FEITO SEMPRE NA PRIMEIRA AULA E AS AULAS SÃO DE SEGUNDA À SEXTA



\U00002705 QUER SABER O QUE IRÁ APRENDER NAS AULAS DE CANTO? DIGITE: SIMC'''

        elif mensagem == '4':
            return f'''\U0001F4D5 1 Aluno:

\U00002714 1 vez por semana/50 min cada aula
\U00002714 R$80,00 por mês (manhã ou tarde)
\U00002714 R$100,00 por mês (noite)


\U0001F4D5 2 Alunos:

\U00002714 Ao mesmo tempo.
\U00002714 1 vez por semana/50min cada aula
\U00002714 R$130,00 por mês (manhã ou tarde)
\U00002714 R$150,00 por mês (noite)


\U0001F4D5 3 Alunos:

\U00002714 Ao mesmo tempo.
\U00002714 1 vez por semana/50min cada aula
\U00002714 R$180,00 por mês (manhã ou tarde)
\U00002714 R$200,00 por mês (noite)


\U0001F4D5 4 Alunos ou mais:

\U00002714 Ao mesmo tempo.
\U00002714 1 vez por semana/50min cada aula
\U00002714 R$50,00 por mês cada aluno (manhã ou tarde)
\U00002714 R$80,00 por mês por aluno (noite)

\U0001F6A8\U0001F6A8 OBS: CASO FOR FAZER DUAS AULAS POR SEMANA, O VALOR IRÁ DOBRAR

\U0001F6A8\U0001F6A8 O PAGAMENTO È FEITO SEMPRE NA PRIMEIRA AULA E AS AULAS SÃO DE SEGUNDA À SEXTA



\U00002705 QUER SABER O QUE IRÁ APRENDER NAS AULAS DE TEORIA MUSICAL? DIGITE: SIMTM'''

        elif mensagem == '5':
            return f'''TELEGRAM:    https://t.me/RobertBrayner

WHATSAPP:   https://wa.me/5533988420019'''   
        
        if mensagem == '6':
                return f'''instagram.com/robertbrayner

''' 

        elif mensagem.lower() in ('simv'):
            return f'''O QUE IRÁ APRENDER

\U00002705 TROCAR AS CORDAS DO VIOLÃO
\U00002705 LER CIFRAS
\U00002705 AFINAR O VIOLÃO
\U00002705 ESCALAS
\U00002705 INTERVALOS
\U00002705 RITMOS
\U00002705 ACORDES MAIORES E MENORES
\U00002705 ACORDES SUSTENIDOS E BEMÓIS MAIORES E MENORES
\U00002705 DEDILHADO
\U00002705 POSTURA PARA TOCAR VIOLÃO
\U00002705 CAMPO HARNÔNICO
\U00002705 CONHECER O BRAÇO DO VIOLÃO
\U00002705 LER PARTITURA
\U00002705 LER TABLATURA


\U0001F4B0\U0001F4B0 CLIQUE ABAIXO EM UM DOS LINKS PARA INICIAR AS AULAS:

TELEGRAM:    https://t.me/RobertBrayner

WHATSAPP:   https://wa.me/5533988420019


\U0001F6A8\U0001F6A8 CASO FOR QUERER MARCAR PARA COMEÇAR A FAZER AS AULAS, SERÁ NECESSÁRIO DAR UM SINAL DE 50% DO VALOR, PARA PODER GARANTIR A SUA VAGA COM ANTECEDÊNCIA


NÃO DEIXE PARA AMANHÃ, AQUILO QUE VOCÊ PODE APREDER HOJE \U0000263A'''
        
        elif mensagem.lower() in ('simt'):
            return f'''O QUE IRÁ APRENDER

\U00002705 LER CIFRAS 
\U00002705 CONHECER O TECLADO 
\U00002705 ESCALAS 
\U00002705 INTERVALOS 
\U00002705 RITMOS 
\U00002705 ACORDES MAIORES E MENORES 
\U00002705 ACORDES SUSTENIDOS E BEMÓIS MAIORES E MENORES 
\U00002705 MONTAR ARRANJOS MUSICAIS 
\U00002705 ARRANJOS PRONTOS 
\U00002705 POSTURA PARA TOCAR O TECLADO 
\U00002705 CAMPO HARMÔNICO 
\U00002705 LER PARTITURA


\U0001F4B0\U0001F4B0 CLIQUE ABAIXO EM UM DOS LINKS PARA INICIAR AS AULAS:

TELEGRAM:    https://t.me/RobertBrayner

WHATSAPP:   https://wa.me/5533988420019


\U0001F6A8\U0001F6A8 CASO FOR QUERER MARCAR PARA COMEÇAR A FAZER AS AULAS, SERÁ NECESSÁRIO DAR UM SINAL DE 50% DO VALOR, PARA PODER GARANTIR A SUA VAGA COM ANTECEDÊNCIA


NÃO DEIXE PARA AMANHÃ, AQUILO QUE VOCÊ PODE APREDER HOJE \U0000263A'''

        elif mensagem.lower() in ('simc'):
            return f'''O QUE IRÁ APRENDER

\U00002705 AQUECIMENTO VOCAL 
\U00002705 RESPIRAÇÃO 
\U00002705 ALTURA 
\U00002705 INTENSIDADE 
\U00002705 AFINAÇÃO 
\U00002705 TIMBRE 
\U00002705 TESSITURA VOCAL 
\U00002705 EXTENSÃO VOCAL 
\U00002705 VOCALIZES 
\U00002705 MELISMA 
\U00002705 STACCATO 
\U00002705 LEGATO 
\U00002705 CANTAR COM DIAFRAGMA 
\U00002705 TIPOS DE CANTOS 
\U00002705 POSTURA 
\U00002705 VIBRATO 
\U00002705 VOZ DE CÂNONE 
\U00002705 COMO É FEITA A DIVISÃO DE VOZES 
\U00002705 CLASSIFICAÇÃO VOCAL 
\U00002705 CUIDADOS COM A VOZ 
\U00002705 COMO A VOZ É PRODUZIDA


\U0001F4B0\U0001F4B0 CLIQUE ABAIXO EM UM DOS LINKS PARA INICIAR AS AULAS:

TELEGRAM:    https://t.me/RobertBrayner

WHATSAPP:   https://wa.me/5533988420019


\U0001F6A8\U0001F6A8 CASO FOR QUERER MARCAR PARA COMEÇAR A FAZER AS AULAS, SERÁ NECESSÁRIO DAR UM SINAL DE 50% DO VALOR, PARA PODER GARANTIR A SUA VAGA COM ANTECEDÊNCIA


NÃO DEIXE PARA AMANHÃ, AQUILO QUE VOCÊ PODE APREDER HOJE \U0000263A'''

        elif mensagem.lower() in ('simtm'):
            return f'''O QUE IRÁ APRENDER

\U00002705 O QUE É NOTA MUSICAL 
\U00002705 O QUE É CIFRA
\U00002705 O QUE  É ESCALA NATURAL OU DIATÔNICA 
\U00002705 O QUE É ESCALA CROMÁTICA 
\U00002705 INTERVALOS 
\U00002705 RITMOS 
\U00002705 O QUE É ACORDE MUSICAL 
\U00002705 O QUE É SUSTENIDO
\U00002705 O QUE É BEMOL
\U00002705 CAMPO HARMÔNICO  
\U00002705 LER PARTITURA 
\U00002705 LER TABLATURA


\U0001F4B0\U0001F4B0 CLIQUE ABAIXO EM UM DOS LINKS PARA INICIAR AS AULAS:

TELEGRAM:    https://t.me/RobertBrayner

WHATSAPP:   https://wa.me/5533988420019


\U0001F6A8\U0001F6A8 CASO FOR QUERER MARCAR PARA COMEÇAR A FAZER AS AULAS, SERÁ NECESSÁRIO DAR UM SINAL DE 50% DO VALOR, PARA PODER GARANTIR A SUA VAGA COM ANTECEDÊNCIA


NÃO DEIXE PARA AMANHÃ, AQUILO QUE VOCÊ PODE APREDER HOJE \U0000263A'''
        else:
            return '''Seja bem vindo(a)!!!
Gostaria de acessar o menu? Digite "menu"'''#primeira mensagem

    # Responder
    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)


bot = TelegramBot()
bot.Iniciar()