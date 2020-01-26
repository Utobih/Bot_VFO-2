#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#Bot_VFO-2.py
#
# Copyright 2019 rob <rob@Elementary-OS>
#  
import mechanize
import http.cookiejar as cookielib
from bs4 import BeautifulSoup
import sys, argparse
from colorama import Fore, Back

#cria a instancia para os argumentos
parser = argparse.ArgumentParser(description='@ Bot VFO by Rob @\n Sempre utilize o site mobile (m.) ou (mbasic)')
#cria o argumento url
parser.add_argument('-t',"--target", required=True, help= Fore.YELLOW+"[=]Escreva o link do perfil a ser verificado.", default="")
parser.add_argument('-u',"--user", required=True, help= Fore.YELLOW+"[=]Escreva o email do seu perfil.", default="")
parser.add_argument('-p',"--password", required=True, help= Fore.YELLOW+"[=]Escreva a senha do seu perfil.", default="")
#adiciona os argumentos na variavel args
args = parser.parse_args()

#Criando instancia do Browser
br = mechanize.Browser()
#Configurando cookie
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)
#cj.clear_session_cookies()
# Configurando configurações e user-agent
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-agent', 'Chrome')]


def login(verific,exitc,br):
    #Abrindo url de login
    br.open('https://www.facebook.com/login/')
    #selecionando formulario de login
    br.select_form(nr=0)
    #enviando email
    br.form['email'] = args.user
    #enviando senha
    br.form['pass'] = args.password
    #definindo metodo
    br.method = "POST"
    #enter
    result = br.submit()
    
    if (result.geturl() == "https://www.facebook.com/" or result.geturl() == "https://www.facebook.com/update_security_info.php?wizard=1"):
        print(Fore.GREEN+"[*] Login realizado com sucesso. :D")
        verific(exitc,br)
    else:
        print(Fore.RED+"[-] Infelizmente deu um erro no login, verifique o email e a senha. : /")
        exitc()

def verific(exitc,br):
    #abrindo url
    result = br.open(args.target)
    #links de verificação
    online="https://static.xx.fbcdn.net/rsrc.php/v3/yU/r/gATt-jY8pG8.png"
    in_cell="https://static.xx.fbcdn.net/rsrc.php/v3/yK/r/Ye1TQi63ARL.png"
    # abrindo pagina resposta
    soup = BeautifulSoup(br.response().read(), "lxml")
    #procurando todas as imagens localizadas no html
    resil = soup.find_all("img")
    # Se a imagem 3 tiver o mesmo link da variavel $online:
    try:
        if (resil[3]['src'] == online):
            #imprime ONLINE
            print(Fore.GREEN+"[*] O perfil encontra-se online!!!! YEAH :3")
            #sai
            exitc()
        
        #Se a imagem 3 tiver o mesmo link da variavel $In_cell:
        elif(resil[3]['src'] == in_cell):
            #imprima NO CELULAR
            print(Fore.YELLOW+"[*-] O perfil encontra-se no celular. :)")
            #sai
            exitc()
        #se nenhuma das situações acima estiver certa:
        else:
            #imprima OFFLINE
            print(Fore.RED+"[-] Infelizmente o perfil encontra-se Offline, mas não desista!!!! :(")
            #sai
            exitc()
    except IndexError:
        print(Fore.RED+"[-] Não foi encontrada a variavel de disponibilidade, provavelmente o perfil está off a muito. :(")
    
    
def exitc():
    print(Fore.YELLOW+"Espero ter ajudado-lhe!!! Até mais!! :D")
    print(Fore.BLUE+"Bot VFO v2")
    print(Fore.BLUE+">< By Rob ><")
    sys.exit(0)

login(verific, exitc,br)
