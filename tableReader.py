from disease import Disease

class TableReader:
    diseaseCategory = ""
    diseaseTag = ""
    diseaseName = ""
    index = 0

    numList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def read(self, line, list):
        if (line[0 : 4] == "Part"):#카테고리 입력
            self.diseaseCategory = line[line.find(' ') + 1 : line.find('\n')]
        elif (not line[0] in self.numList):#태그 생성
            self.diseaseTag = line[:line.find('\n')]
        else:
            name = line.split(". ")[1][:line.find('\n')]
            idx = 100
            for i in range(10):
                if (name.find(self.numList[i]) != -1 and idx > name.find(self.numList[i])):
                    idx = name.find(self.numList[i])
            self.diseaseName = name[:idx - 1]

            self.makeDisease(self, list)
        
        if (line[0 : 3] == "100"):#이 phase를 끝내기 위해
            return False
        return True
    
    def makeDisease(self, list):
        list.append(Disease(self.diseaseCategory, self.diseaseTag, self.diseaseName, self.index + 1))
        self.index += 1
    
        
    def show(self):
        print(self.diseaseCategory)




