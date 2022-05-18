import subprocess

data = subprocess.check_output(['wmic', 'printer', 'list', 'brief']).decode('utf-8').split('\r\r\n')

data = data[1:]

for line in data:
    for printername in line.split("  "):
        if printername != "":
            print(printername)
            break