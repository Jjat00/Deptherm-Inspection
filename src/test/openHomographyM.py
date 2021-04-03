import json

def openFile(pathFile):
        with open(pathFile) as jsonFile:
                data = json.load(jsonFile)
        return data

def getHomography(path):
    data = openFile(path)
    homographyMatrix = data['homographyMatrix']
    print(homographyMatrix)


getHomography('hThermal2rgb.json')
