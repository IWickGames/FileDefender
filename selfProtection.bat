@echo off
timeout /nobreak 2 >nul
:1
tasklist | findstr /c:"FileDefender.exe" && echo Process found || goto SelfProtect
goto 1

:SelfProtect
timeout /nobreak 3 >nul
mkdir "AttackSave"
shutdown /l 00
exit