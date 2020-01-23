Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c selfProtection.bat"
oShell.Run strArgs, 0, false