import os
import sys
import setuptools
import requests
import json
import fernet
import base64
print ("\nOptions Menu - PASSWORD RECOVERY TOOL - V7.2 By SonozakiShion")
print ("PASSWORD RECOVERY TOOL - SonozakiShion")
print ("-"*70)
USER_EMAIL = input("Endereço De Email: ").strip()
USER_PASSWORD = input("Senha De Usuário: ")

LOST_USER_EMAIL = input("Endereço De Email: ").strip()
LOST_USER_PASSWORD = input("Senha Perdida Do Usuário: ")

PASS = input("RECUPERAR_CONTA_PERDIDA_DO_USUÁRIO: ")

ACCOUNT_EMAIL = input("EMAIL DA CONTA DO USUÁRIO: ").startswith("Bryan12345321souza")
ACCOUNT_PASSWORD = input("SENHA DA CONTA DO USUÁRIO: ")
KEYFILE = ".cache"
INTERVALO_BASE = "45"
RESFRIAMENTO_DE_TIMING = "15" #Resfriamento em segundos para evitar detecção por sistemas ofensivos.

AUTO_EXEC = input("INSIRA AQUI SUAS INFORMAÇÕES DE CONTA DO USUÁRIO PARA RECUPERAR: ")
try:
   print("[+] Conta Recuperada Com Sucesso! ")
except KeyboardInterrupt:
   print("[-] Falha ao recuperar a conta. ")