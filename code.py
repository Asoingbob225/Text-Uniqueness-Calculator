#UNIHACKS 2021
#Ryan Kalo, Jimin Yu, Nitin Chinthapalli, Brandon Tucker
#Calculates a score up to 100 of how unique your text is based on the frequency of words in the English language


#IMPORT-------------------------------------------------------------
import statistics
import pandas as pd

#FUNCTIONS------------------------------------------------------------
#removes punctuation
def punct_remove(text, LETTERS ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    cleaned_text = '' 
    for character in text:
        if character.upper() in LETTERS:
            cleaned_text += character.lower()
    return cleaned_text

#removes stop words from array of words
def remove_stops(wordArr):
    no_articles_list = []
    for z in range(0, len(wordArr)):
        no_articles_list.append(wordArr[z])
    stopWords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "youre", "youve", "youll", "youd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "shes", 'her', 'hers', 'herself', 'it', "its", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "thatll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "shouldve", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "arent", 'couldn', "couldnt", 'didn', "didnt", 'doesn', "doesnt", 'hadn', "hadnt", 'hasn', "hasnt", 'haven', "havent", 'isn', "isnt", 'ma', 'mightn', "mightnt", 'mustn', "mustnt", 'needn', "neednt", 'shan', "shant", 'shouldn', "shouldnt", 'wasn', "wasnt", 'weren', "werent", 'won', "wont", 'wouldn', "wouldnt"]
    for n in range(0, len(no_articles_list)):
        for s in no_articles_list:
            if s in stopWords:
                no_articles_list.remove(s)
    return no_articles_list

#return the frequency of one word
#searches previous words then full list
def find_freq(word, arr):
    i = binary_search(arr, word)
    if i >= 0:
        return dataTable.loc[i, 'count']
    return -1

#return the rank of one word
#searches previous words then full list
def find_rank(word, arr):
    i = binary_search(arr, word)
    if i > 0:
        return i
    return -1
	
#returns index of x in arr if present, else -1 
def binary_search(array, element):
    mid = 0
    start = 0
    end = len(array)
    step = 0

    while (start <= end):
        step = step+1
        mid = (start + end) // 2

        if element == array[mid]:
            return mid

        if element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


#CALCULATE SCORE----------------------------------------------------

print("Importing Data...")
#import word frequency data
dataTable = pd.read_csv("unigram_freq.csv")

#import text file, each word as item in array
with open("text.txt", "r") as file:
    content = file.read()
    content_list = content.split()
content_list = [punct_remove(x) for x in content_list]
no_articles = remove_stops(content_list)

print("Analyzing Data...")
#make array of frequencies and ranks
wordsList = []
for i in range(0, 333333):
	wordsList.append(dataTable.loc[i, 'word'])

#-------------------
#Unfiltered

frequencies1 = []
ranks1 = []
for i in range(0, len(content_list)):
    num1 = find_freq(content_list[i], wordsList)
    num2 = find_rank(content_list[i], wordsList)
    if(num1 >= 0):
        frequencies1.append(num1)
    if(num2 >= 0):
        ranks1.append(num2)

#prints scaled means
if(len(frequencies1) > 0):
	print("Your unfiltered uniqueness score is: " + str(100 - (statistics.mean(frequencies1)*10000/(5.88*(10**11)))))
else:
	print('No Words Found')



#---------------------------------
#Filtered
frequencies2 = []
ranks2 = []
for i in range(0, len(no_articles)):
    num1 = find_freq(no_articles[i], wordsList)
    num2 = find_rank(no_articles[i], wordsList)
    if(num1 >= 0):
        frequencies2.append(num1)
    if(num2 >= 0):
        ranks2.append(num2)
1
#prints scaled means
if(len(frequencies2) > 0):
	print("Your filtered uniqueness score is: " + str(100 - (statistics.mean(frequencies2)*10000/(5.88*(10**11)))))
else:
	print('No Words Found')
