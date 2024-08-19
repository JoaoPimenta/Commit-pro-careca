from time import sleep
import webbrowser
import os

def calculador_de_cabelo():
    print('Analisando o bulbo capilar... ')
    sleep(5)
    cabelo_atual = 0
    if cabelo_atual == 0:
        print('Calvice Galopante! vamos iniciar o tratamento agora!!!')
    sleep(3)
    url = 'https://hello.manual.com.br/a/queda-de-cabelo-minox-o-sem?utm_source=google&utm_medium=cpc&utm_campaign=16664307590&utm_term=minoxidil&gclid=Cj0KCQjw2ou2BhCCARIsANAwM2HLAkeMG1u2DTPLhsxBcPingSeYiwk6LKoEPJYv1xJVaE4_slTzZ3kaAkJgEALw_wcB'
    webbrowser.open(url)
    sleep(8)
    print('Não se preocupe, ser careca não é o fim do mundo! Veja algumas celebridades que também são: ')
    sleep(4)
    referencias = os.path.abspath('referencias_calvas.html')
    webbrowser.open(referencias)
calculador_de_cabelo()