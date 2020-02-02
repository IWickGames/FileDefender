import os
import sys
import time
import urllib.request

import monitorReg
import sendComputerID

#Remove Temp Files(If program was killed before there deletion)
def cleanUp():
    if os.path.exists("dir.tmp"):
        os.remove("dir.tmp")
    if os.path.exists("files.save"):
        os.remove("files.save")

cleanUp()

#Settings-------------------

#Protection settings
maxChanges = 10
waitTimer = 10

backUpRerollEnable = True #You can set this to False if you just want the program to take the computer offline when an attack is detected

version = '1.2.1.5 Alpha'
monitorDirs = ['%userprofile%\Desktop','%userprofile%\Documents','%userprofile%\Music','%userprofile%\Pictures','%userprofile%\Videos']

#Get Extenchions
f = open("fileExt.ini")
fileExt = f.read().splitlines()
f.close()

#Convert python variables to windows variables
for dir in monitorDirs:
    os.system('if exist "' + dir + '" echo ' + dir + '>>scan.tmp')
monitorDirs = []
f = open("scan.tmp")
monitorDirs = f.read().splitlines()
f.close()
os.remove("scan.tmp")
#---------------------------

#Title----------------------
print("       FileDefender " + version)
print("       Created by @IWickGames#7827")
print("----------------------------------------\n")
print("Starting your protection...")

#---------------------------


#Filter out files that do not have the extention
def filterNoExt(files):
    filterOutputExt = []
    filterOutputNoExt = []
    #Output your data into a file
    with open("files.tmp",'a') as f:
        for item in files:
            f.write(item + "\n")

    #Get all files that have the extention
    print("Removing whitelisted files...")
    for ext in fileExt:
        os.system('type files.tmp | findstr /e /c:"' + ext + '">>files.saveExt')

    #Get all files with extentions
    f = open("files.saveExt")
    filterItTmp = f.read().splitlines()
    f.close()
    for item in filterItTmp:
        filterOutputExt.append(item)
    
    #Get all the files without whitelisted extentions
    f = open("files.tmp")
    filterItNoTmp = f.read().splitlines()
    f.close()
    for item in filterItNoTmp:
        if item not in filterOutputExt:
            filterOutputNoExt.append(item)

    os.remove("files.saveExt")
    os.remove("files.tmp")

    return filterOutputNoExt;

#Get all files in your protected folders
def index(useExtFilter):
    for direct in monitorDirs:
        print("Indexing " + str(direct))
        os.system('dir /b /s "' + direct + '">>dir.tmp')

    if useExtFilter:
        #Use Ext filter set
        for ext in fileExt:
            print("Loading " + ext + " files")
            os.system('type dir.tmp | findstr /c:"' + ext + '">>files.save')

        f = open("files.save")
        filesSaved = f.read().splitlines()
        f.close()
    else:
        #Get non filter Ext files
        f = open("dir.tmp")
        filesSaved = f.read().splitlines()
        f.close()
        filesSaved = filterNoExt(filesSaved)

    #Get formatted file list
    if useExtFilter:
        f = open("files.save")
        filesSaved = f.read().splitlines()
        f.close()
        os.remove("files.save")

    os.remove("dir.tmp")

    return filesSaved;

#Backup all dirs
def backup():
    if not os.path.exists("back"):
        os.mkdir("back")
    for direct in monitorDirs:
        print("Backing up " + direct)
        os.system("arcive.bat " + direct + ">nul")
        os.rename("arcive.zip", "back/" + str(monitorDirs.index(direct)) + ".zip.dll")
    return;

def rollback(removeFiles):
    #Roll back files that where created and restore old ones
    if removeFiles != "No":
        for item in removeFiles:
            try:
                os.remove(item)
            except:
                try:
                    os.rmdir(item)
                except:
                    try:
                        os.system('rd /s /q "' + item + '"')
                    except:
                        pass
    for directory in monitorDirs:
        #Extract all files back to there dirs
        os.rename("back/" + str(monitorDirs.index(directory)) + ".zip.dll", "arcive.zip")
        os.system('extract.bat ' + directory)
        os.rename("arcive.zip", "back/" + str(monitorDirs.index(directory)) + ".zip.dll")

#Undo a attack
if backUpRerollEnable:
    if os.path.exists("AttackSave"):
        #Attack detected rollback changes
        if not os.path.exists("AttackSave/attack.save"):
            removeFilesAS = "No"
        else:
            f = open("AttackSave/attack.save")
            removeFilesAS = f.read().splitlines()
            f.close()

        rollback(removeFilesAS)

        if removeFilesAS != "No":
            os.remove("AttackSave/attack.save")
    
        os.rmdir("AttackSave")

        os.system('start "" "attackMSG.vbs"')

#Remove Old backups
if os.path.exists("back"):
    os.system("rd /s /q back")

#Backup for the first time or create fresh backups
if backUpRerollEnable:
    backup()
#Index for the first time
indexedFiles = index(False)


#Protection
print("Protection started...")
while True:
    try:
        time.sleep(waitTimer)

        #Check Shell for changes
        statusVar = monitorReg.checkShell()
        if statusVar:
            print("Registry Check --- Pass")
        else:
            print("Registry Check --- Failed")
            print("Recovering Registry...")

            #Write to log
            with open("filedefender.log", "a") as f:
                f.write("Registry Check Failed\n")

            monitorReg.recoverReg()

        createdFiles = []
        removedFiles = []
        allChanges = []
        #Check for file changes
        tmpIndex = index(False)

        #New Files
        for item in tmpIndex:
            if item not in indexedFiles:
                createdFiles.append(item)
                allChanges.append(item)
        #Removed items
        for item in indexedFiles:
            if item not in tmpIndex:
                removedFiles.append(item)
                allChanges.append(item)

        if len(allChanges) == 0:
            #No changes found
            print("No changes found")
        else:
            #Changes found seeing if its over the limit
            if len(allChanges) > maxChanges:
                #Change count reached the limit rollback!
                print("Max changed detected!")

                needRemovedFiles = allChanges

                for items in createdFiles:
                    needRemovedFiles.append(items)

                if os.path.exists("AttackSave"):
                    os.remove("AttackSave/attack.save")
                    os.rmdir("AttackSave")
                
                os.mkdir("AttackSave")
                f = open("AttackSave/attack.save", 'a')
                for files in needRemovedFiles:
                    f.write(files + "\n")
                f.close()

                #Write a attack message to the log file
                with open("filedefender.log", "a") as f:
                    f.write("Attack was detected\n")

                #Check 
                if backUpRerollEnable:
                    os.system("shutdown /l")
                else:
                    os.system("shutdown /s /t 00")
            else:
                #Change count did not reach the limit
                indexedFiles = createdFiles
    except Exception as err:
        sendComputerID.sendReport(err)
        pass
    except KeyboardInterrupt:
        print("\n\n\n\nStopping protection...")
        cleanUp()
        temp = input("\nPress any key to exit...")
        sys.exit()