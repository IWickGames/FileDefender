@echo off
cd "%~dp0"
title Windows Recovery
mode 45,30

net session >nul 2>&1
if %errorLevel% == 0 (
goto start
) else (
start "" "getAdmin.vbs"
exit
)

:start
REM Check if the current App is in shell
reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell | findstr /c:"explorer.exe">nul
if %errorlevel%==0 goto installSafeMode
goto startSafeMode

:startSafeMode
echo.
echo             Windows Recovery
echo +======================================+
echo   Welcome to Windows Recovery Interface
echo            +=================+
echo If you are seeing this screen your PC may
echo     be badly infected or non working.
echo     This program is made to help you!
echo.
echo   To get started there is a pre list of
echo            programs to open
echo.
echo   To select a item type the item in the 
echo   brackets and press enter to select it
echo.
echo   If you know what you are doing then try
echo     advanced to start a command prompt
echo.
echo          Press any key to start
pause >nul
:beginSelection
cls
echo.
echo             Windows Recovery
echo +======================================+
echo.
echo           Select a option below
echo.
echo.
echo [1] Explorer
echo [2] Google
echo [3] Regedit
echo [4] Msconfig
echo [5] Task Manager
echo.
echo [A] Advanced Mode
echo [B] Uninstall
set /p enter=">"
if %enter%==1 start explorer.exe
if %enter%==2 explorer.exe "https://google.com/"
if %enter%==3 regedit.exe
if %enter%==4 msconfig.exe
if %enter%==5 taskmgr.exe

if %enter%==A goto AdvancedMode
if %enter%==a goto AdvancedMode
if %enter%==B goto uninstall
if %enter%==b goto uninstall
goto beginSelection
:AdvancedMode
cls
echo      Windows Recovery Advanced Mode
echo +======================================+
echo.
echo Enter a command below
echo.
:cmdLoop
set /p com="%cd%>"
echo.
%com%
echo.
goto cmdLoop

:uninstall
echo y|reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell /t REG_SZ /d "explorer.exe" >nul
echo y|reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell /t REG_SZ /d "explorer.exe" >nul
echo y|reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell /t REG_SZ /d "explorer.exe" >nul
echo y|reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell /t REG_SZ /d "explorer.exe" >nul
echo         Press any key to restart
pause>nul
shutdown /r /t 00
exit
:installSafeMode
echo.
echo             Windows Recovery
echo +======================================+
echo.
echo    Welcome to Windows Recover Install
echo.
echo    To start install press any key to
echo    Close this install by just pressing
echo      The X button in the corner of 
echo               this window
echo.
echo         Press any key to install
pause>nul
echo y|reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell /t REG_SZ /d "C:\SafeMode\StartupKey.bat" >nul
echo y|reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell /t REG_SZ /d "C:\SafeMode\StartupKey.bat" >nul
echo y|reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell /t REG_SZ /d "C:\SafeMode\StartupKey.bat" >nul
echo y|reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell /t REG_SZ /d "C:\SafeMode\StartupKey.bat" >nul
echo         Press any key to restart
pause>nul
shutdown /r /t 00
exit