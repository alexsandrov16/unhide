import subprocess,time,os

print("             _     _     _       ")
print(" _   _ _ __ | |__ (_) __| | ___  ")
print("| | | | '_ \| '_ \| |/ _` |/ _ \ ")
print("| |_| | | | | | | | | (_| |  __/ ")
print(" \__,_|_| |_|_| |_|_|\__,_|\___| v0.1")

time.sleep(2)
os.system('cls')

disk=input("Especifique la letra de la unidad a escanear.[Ej. D]")

if len(disk)>1:
    disk=disk[-1]

print(f"Escaneando unidad {disk.upper()}:\ ")
pr=subprocess.Popen(["ATTRIB", "/d", "/s", "-r", "-h", "-s", f"{disk}:*"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
pr.communicate()

if pr.returncode==0:
    print("Proceso finalizado.")
else:
    print("Ha ocurrido un error.")

os.system("PAUSE")