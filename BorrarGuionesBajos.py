import os
import sys


def scanRoot():
    '''
    Scan the root of the current folder in order to get the files that starts with ._
    '''
    folder='.'
    scanned = []

    for path, subdirs, files in os.walk(folder):
            for name in files:
                filePath = os.path.join(os.getcwd(), path[2:], name)
                print("Analyzing the file: ",path,"/",name, sep='')
                scanned.append(filePath)
    return scanned

def renameFiles(files):
    '''
    Make a copy of the files returned in scanRoot, delete the ._ files and contains the new files without ._ 
    '''

    escaneados = scanRoot()
    guionesBajos = []

    #Change the name removing the ._
    for file in escaneados:
        copy = file
        try:
            while True:
                slash = copy.index('/')
                copy = copy[(slash + 1):]
        except:
            file = file[len(os.getcwd()) + 1:]
            if copy[:2] == '._':
                guionesBajos.append(file)
                os.remove(file)
    return guionesBajos

def cleanFolder():
    '''
    function to let know if current directory has ._ files or not
    '''
    root = scanRoot()
    changedFiles = renameFiles(root)

    if len(changedFiles) == 0:
        print("There were not any '._' files :)")
    else:
        print("The next '._' files have been deleted!")
        print(changedFiles)



if __name__ == "__main__":
    cleanFolder()