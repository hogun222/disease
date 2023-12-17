from matchChecker import check_paraphrase
from matchChecker import calculate_similarity
from diseaseAranger import getDiseaseData
from diseaseAranger import DiseaseData

def getPercentage(diseases, word):
    access_key = "c5dd01ba-7adb-4ae6-ae1e-3f494a9c29c6" 

    for disease in diseases:
        if (disease.symptom == None):
            disease.symptomAve = 0
        else:
            sum = 0
            for i in range(len(disease.symptom)):
                res = check_paraphrase(word, disease.symptom[i], access_key)
                if (res):
                    disease.symptomMatch[i] = calculate_similarity(word, disease.symptom[i])
                    sum += disease.symptomMatch[i]
                else:
                    disease.symptomMatch[i] = 0
            print(sum, len(disease.symptom))
            disease.symptomAve = sum / len(disease.symptom)
    
    return diseases

def pickThree(diseases):
    numList = [0, 0, 0]
    for i in range(len(diseases)):
        if (diseases[i].symptomAve > diseases[numList[0]].symptomAve):
            numList[0] = i
        elif (diseases[i].symptomAve > diseases[numList[1]].symptomAve):
            numList[1] = i
        elif (diseases[i].symptomAve > diseases[numList[2]].symptomAve):
            numList[2] = i
    return numList

diseases = getDiseaseData()
diseases = diseases[:10]
print(diseases[0].name, diseases[0].symptomAve)
word = input("단어 입력하세요 : ")
diseases = getPercentage(diseases, word)

print(diseases[0].name, diseases[0].symptomAve)

numList = pickThree(diseases)
print(numList)

for i in range(3):
    print(diseases[numList[i]].name, diseases[numList[i]].symptom, diseases[numList[i]].symptomMatch, diseases[numList[i]].symptomAve)





