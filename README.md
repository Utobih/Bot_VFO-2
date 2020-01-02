# Bot_VFO-2
Bot, crawling que verifica se algum perfil está online no facebook, desenvolvido em python.


#### reqs
FVO(FaceVerifyOnline), é a versão v2.0 do bot VFO que havia publicado a um tempo atrás, porem mais eficaz, leve e instavel, eu utilizava o Selenium e tals, isso comia muita memoria ram, então resolvi fazer um v2 mais minimalista e de melhor performance.


#### instalar requisitos(LINUX):
> sudo pip3 install -r requeriments.txt

(colorama, mechanize, argparse, bs4)

#### Uso (TERMINAL LINUX)
Para usar o script você deve usa-lo com 3 parametros, "-u" de "user" para o email ou id da sua conta; "-p" de "password" para sua senha; E "-t" de "target" para o link alvo; Exemplo:

> ./Bot_VFO-2.py -u meu_email@email.com -p minha_senha -t https://m.facebook.com/link_do_perfil_alvo

ou

> ./Bot_VFO-2.py --user meu_email@email.com --password minha_senha --target https://m.facebook.com/link_do_perfil_alvo

para um help basico, digite:

> ./Bot_VFO-2.py -h

ou

> ./Bot_VFO-2.py --help


##### OBS: sempre utilize o url facebook mobile > (https://m.face..) ou (https://mbasic.face..) e não o desktop > (http://www.face..) pois o unico que retorna a imagem a ser analizada é a versão mobile.


> ~ by Rob ~
