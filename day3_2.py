from os import listdir
from os.path import isfile, join
from os import walk

co1 = "Bacterial Infections and Mycoses"
co2 = "Virus Diseases"
co3 = "Parasitic Diseases"
co4 = "Neoplasms"
co5 = "Musculoskeletal Diseases"
co6 = "Digestive System Diseases"
co7 = "Stomatognathic Diseases"
co8 = "Respiratory Tract Diseases"
co9 = "Otorhinolaryngologic Diseases"
co10 = "Nervous System Diseases"

co_list = [co5, co9, co1, co10, co3, co4, co2, co6, co8, co7]

trainData = []

mypath = "/home/ai8/Desktop/common/NLP/nlp3/Assignment 3"

# print(listdir(mypath))

co = 0

for directory in listdir(mypath)[1:11]:
    mynpath = mypath + '/' + directory
    # print(mynpath)
    for file_names in walk(mynpath):
        for each_file in file_names[2]:
            myfpath = mynpath + '/' + each_file
            # print(myfpath)
            f = open(myfpath, 'r')
            temp_str = f.read()
            tuple = temp_str, co_list[co]
            trainData.append(tuple)
    co += 1

f.close()

for content, category in trainData:
    print("content: " + content)
    print("category: " + category)
    print("-----------------------------------------------------------------")


from textblob.classifiers import NaiveBayesClassifier

classifier = NaiveBayesClassifier(trainData)

testData0 = """External fixation for type III open tibial fractures.
 An analysis of 51 type III open tibial fractures treated by external skeletal fixation is presented.
 The fractures are subdivided according to the classification of Gustilo, Mendoza and Williams (1984) into types IIIa, IIIb and IIIc.
 The different prognoses of these fracture subtypes is examined.
 The use of the Hoffmann and Hughes external fixators in the management of type III open tibial fractures is presented and it is suggested that the prognosis is independent of the type of fixator used."""

testData1 = """Possible role of leukotrienes in gastritis associated with Campylobacter pylori.
 This study was done to evaluate the role of leukotrienes (LTs) in gastritis associated with Campylobacter pylori.
 Biopsy specimens of gastric mucosa were obtained endoscopically from 18 patients with nonulcer dyspepsia for bacteriological and histological examination and extraction of LTs.
 There was correlation between the LTB4 level in the mucosa and the degree of gastritis evaluated histologically.
 The level was higher when infiltration of neutrophils in the gastric mucosa was more extensive.
 The LTB4 level in mucosa infected with C.
 pylori was higher than that in noninfected mucosa.
 These findings suggest that endogenous LTs may be related to the pathogenesis of gastritis associated with C.      
 pylori."""

print("testData0 belongs to:- ")
print(classifier.classify(testData0))
print("testData1 belongs to:- ")
print(classifier.classify(testData1))

			
