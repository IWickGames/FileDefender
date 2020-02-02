@echo off
REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "FileDefender Startup" /t REG_SZ /F /D "C:\Program Files\FileDefender\execute.bat">nul
cd "%~dp0"
start "FileDefender Self Protection" "selfProtection.vbs"

echo.>>filedefender.log
echo.>>filedefender.log
echo %time% - %date% : Launch Log>>filedefender.log
call "FileDefender.exe"

exit