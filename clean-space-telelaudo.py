# O código abaixo verifica pelos arquivos no Disco C do servidor do Telelaudo, se o espaço em disco for menor do que 5GB ele realiza as exclusões das pastas não atuais

import os
import sys
import shutil
import datetime

base_dir = r'E:\DCM4CHEE\DCM4CHEE'
current_year = str(datetime.datetime.now().year)
current_month = str(datetime.datetime.now().month)
current_day = str(datetime.datetime.now().day)
current_date = datetime.datetime.now()

# Verifica se o disco local C tem menos de 5GB de espaço livre
# DiskDrive = os.getenv('SystemDrive')
DiskDrive = 'E:'
total, used, free = shutil.disk_usage(DiskDrive)

# Convertendo bytes para gigabytes
totalGB = total / (1024 ** 3)
totalGB_formated = float("{:.2f}".format(totalGB))

usedGB = used / (1024 ** 3)
usedGB_formated = float("{:.2f}".format(usedGB))

freeGB = free / (1024 ** 3)
freeGB_formated = float("{:.2f}".format(freeGB))

print("Espaço em disco total:", totalGB_formated, "GB")
print("Espaço em disco usado:", usedGB_formated, "GB")
print("Espaço em disco livre:", freeGB_formated, "GB")

try:
    if freeGB_formated < 50.00:
        # Verificar e excluir diretórios que não são iguais ao ano atual
        for dir_name in os.listdir(base_dir):
            if dir_name != current_year:
                dir_path = os.path.join(base_dir, dir_name)
                print(f"Excluir diretórios que não são iguais ao ano atual")
                print(f"Excluindo diretório: {dir_path}...")
                shutil.rmtree(dir_path)
                print(f"Deletado: {dir_path}")

        # Entrar no diretório atual do ano
        year_dir = os.path.join(base_dir, current_year)
        os.chdir(year_dir)
        print(year_dir)

        # Verificar e excluir diretórios que não são iguais ao mês atual.
        for name_month in os.listdir(year_dir):
            if name_month != current_month:
                dir_path_month = os.path.join(year_dir, name_month)
                print(f"Excluir diretórios que não são iguais ao mes atual")
                print(f"Deletando diretorios: {dir_path_month}...")
                shutil.rmtree(dir_path_month)
                print(f"Deletado: {dir_path_month}")
            
        # Entrar no diretório atual do mês.
        month_dir = os.path.join(base_dir, current_year, current_month)
        os.chdir(month_dir)
        print(month_dir)

        for name_day in os.listdir(month_dir):
            if name_day != current_day:
                dir_path_day = os.path.join(month_dir, name_day)
                print(f"Excluir diretórios que não são iguais ao dia atual")
                print(f"Diretorios deletados: {dir_path_day}...")

                # Tente excluir, se ocorrer algum erro de permissão, lance o erro no bloco de exceção.
                try:
                    shutil.rmtree(dir_path_day)
                    print(f"Deletado diretorio: {dir_path_day}")
                except PermissionError as e:
                    print(f"Erro de permissao ao deletar diretorio: {dir_path_day}")
                    continue
    else:
        print(f"O espaço total em disco é superior a 50GB livre!")
        sys.exit(0)
except os.error as error:
    print("Error:", error)
    sys.exit(0)
