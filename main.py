# -*- coding: utf-8 -*-
from random import randint
import re
import random
import platform
from os import system
from time import sleep

print('--------------------------')
print('Bem Vindo ao Painel HID   ')
print('--------------------------')

print('[1] Devs')
print('[2] Gerador de Cpfs Validos')
print('[3] Sair')
n1 = int(input("Digite sua escolha:"))

if n1 == 1:
  print('By: CoronelModz')
  sleep(2)
  print('Vish, O painel crashou Reinicie o painel')
  
elif n1 == 2:
  def getRandom():
      #Gera um valor inteiro aleatório entre 111111111 e 999999999
      numero = randint(111111111, 999999999)
      #Filtra numeros repetidos pois são inválidos apesar de passar na conta de validação
      repetidoRegex = re.compile(r'(\d)\1{8}')
      repetidoTest = repetidoRegex.search(str(numero))
      while repetidoTest:
          numero = randint(111111111, 999999999)
          repetidoTest = repetidoRegex.search(str(numero))
      return numero

if __name__ == "__main__":
    cpf = str(getRandom())
    print "[+] 9 digitos gerados:", cpf

    #Gera o primeiro digito verificador
    validar = 0
    m = 10
    for n in range(0, 9):
        validar += int(cpf[int(n)]) * m
        m -= 1
    validar = (validar * 10) % 11
    if validar == 10:
        validar = 0

    print "[+] Primeiro digito verificador:", validar

    #Concatena o digito ao CPF
    cpf += str(validar)

    #Gera o segundo digito verificador
    validar = 0
    m = 11
    for n in range(0, 10):
        validar += int(cpf[int(n)]) * m
        m -= 1
    validar = (validar * 10) % 11
    if validar == 10:
        validar = 0

    print "[+] Segundo digito verificador:", validar

    #Concatena o digito ao CPF
    cpf += str(validar)

    #Imprime o CPF final
    print "[!] CPF Final gerado: "+cpf[:3]+"."+cpf[3:6]+"."+cpf[6:9]+"-"+cpf[9:11]
    sleep(2)
    print('Vish, O painel crashou Reinicie o painel')   
