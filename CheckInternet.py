import os, subprocess, time
import win32com.shell.shell as shell 
from colorama import Fore, init

init(autoreset=True)

def revisar_internet():
    resultado = ''
    try:
        resultado = subprocess.check_output('ping www.google.com', stderr=subprocess.STDOUT,universal_newlines=True)
    except:
        internet = False

    if 'perdidos = 0' in resultado:
        internet = True
    else:
        internet = False
    
    return internet


def reconectar_wifi():

    print(Fore.LIGHTGREEN_EX+'Reconectando al Wi-Fi COWIFI264539605/0'+'\n')

    desactivar_wifi = 'netsh interface set interface "Wi-Fi" disable'
    activar_wifi = 'netsh interface set interface "Wi-Fi" enable'
    concetar_red = 'netsh wlan connect name="COWIFI264539605/0"'
    
    #Usamos lpVerb para ejcutar runas lo cual nos permite ejecuta el cmd con privilegios de admin
    #esto es necesario ya que los comandos netsh requieren privilegios de administrador 
    shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+desactivar_wifi)
    time.sleep(6)
    shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+activar_wifi)
    time.sleep(10)
    shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+concetar_red)
    time.sleep(8)
    print(Fore.LIGHTGREEN_EX+'Reconexión a intertnet realizada con éxito!!!\n')


if __name__ == '__main__':
    
    while True:
        
        internet = revisar_internet()
        
        if internet == True:
            print(Fore.LIGHTYELLOW_EX+'Conexión a internet exitosa!!!\n')
            #Si tenemos conexion a internet entonces esperamos 5 minutos para volver a verificar
            time.sleep(300)
        
        elif internet == False:
            
            reconectar_wifi()
            
            #Despues de realizar la reconexion al wifi y recuperar interntet entonces nos reconectamos al a VPN
            print(Fore.LIGHTMAGENTA_EX+'Reconectando a la VPN...\n\n')
            os.chdir('C:\Program Files (x86)\Cisco Systems\VPN Client')
            os.system('vpnclient.exe connect vpn-switch user yet02265 pwd Panama25')
