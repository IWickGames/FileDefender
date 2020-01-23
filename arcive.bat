@echo off
set "folder=%*"
7za.exe a -bd "arcive.zip" %folder%\* >nul
exit /b