@echo off
set "output=%*"
7za x -bd -y -o%output% "arcive.zip"
exit /b