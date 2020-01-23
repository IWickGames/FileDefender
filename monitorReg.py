import os
import sys

#Check shell and remove changes
def checkShell():
    os.system('reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell | findstr /c:"explorer.exe">nul && echo True>regOutput.save || echo False>regOutput.save')

    with open("regOutput.save") as f:
        regStatus = f.read().splitlines()
    os.remove("regOutput.save")

    if "True " in regStatus:
        output = True
    else:
        output = False
    return output;

#Reset Shell back to explorer.exe
def recoverReg():
    os.system('start "" /wait "RegFixRun.vbs"')