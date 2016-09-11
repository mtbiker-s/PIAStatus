#!/usr/bin/python27

import os
import subprocess

class PIA:
    """
    This class will contain a quick script that will check the status
    of the PIA (Private Internet Access) via the command line
    """


    def __init__(self):
        self.scriptDir = os.path.curdir
        self.url = "https://www.privateinternetaccess.com"
        self.piaStatus = "piastatus"
        self.lookFor = "You are protected"

    def main(self):
        self.checkStatus()

    def checkStatus(self):

        piaStatusFile = os.path.join(self.scriptDir, self.piaStatus)

        if os.path.isfile(piaStatusFile):
            os.remove(piaStatusFile)

        curlCommand = []

        curlCommand.append("curl")
        curlCommand.append(self.url)
        curlCommand.append('-o')
        curlCommand.append(piaStatusFile)

        subprocess.call(curlCommand)

        if os.path.isfile(piaStatusFile):
            statusFileContents = self.getFileContents(piaStatusFile)

            if self.lookFor in str(statusFileContents):
                print "PIA is enabled :)"
            else:
                print "You need to enable VPN"




    def getFileContents(self, fileName):

        f = open(fileName, "r")

        fileLines = []

        for lines in f:
            fileLines.append(lines)

        return fileLines

if __name__ == '__main__':
    PIA().main()