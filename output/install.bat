@echo off
echo Moving files...
move /Y "FileDefender\SafeMode" "C:\" >nul
move /Y "FileDefender" "C:\Program Files\FileDefender" >nul
echo Changing folder status...
echo Y| cacls "C:\SafeMode" /T /G Everyone:F >nul
echo Y| cacls "C:\Program Files\FileDefender" /T /G Everyone:F >nul
echo Starting your app...
start "" "C:\Program Files\FileDefender\execute.bat" >nul
exit