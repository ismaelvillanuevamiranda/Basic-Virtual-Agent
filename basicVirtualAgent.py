#Ismael Villanueva-Miranda
# Word Vectors
import numpy as np
import math
import time
from os import system

answers = [
	("we will have class today"),
	("if you refer to the final project presentation please check the course webpage"),
	("remember that the deadline for the final python project is december 5th"),
	("you have to turn in your assignment using blackboard"),
	("sorry we can not change our meetings"),
]

def loadGloveModel(gloveFile):
	print("Loading Glove Model")
	f=open(gloveFile,'r')
	model={}
	for line in f:
		splitLine=line.split()
		word=splitLine[0]
		embedding=np.array([float(val) for val in splitLine[1:]])
		model[word]=embedding
	print("Done.",len(model),"words loaded")
	return model

def distance(vec1,vec2):
	return math.sqrt(sum([(x-y)*(x-y) for x,y in zip(vec1,vec2)]))

def mostSimilar(query):
	distances=[distance(model[x],model[query]) for x in model.keys()[:200000]]
	minval=min(distances)
	print('for %s: min distance of %.2f found for %s' % (query, minval, model.keys()[distances.index(minval)]))

#======================================================
#Function to calculate the distance between two words
#======================================================
def isClosestTo(vec1,vec2):
	print('Distance between %s and %s is %.2f' % (vec1,vec2,distance(model[vec1],model[vec2])))

start = time.time()
model=loadGloveModel('/Users/ismaelvillanueva/Desktop/glove.6B/glove.6b.50d.txt')
end = time.time()

counter=0
ans = []
shorter = []
print("Hello student, I'm your virtual TA and I will do my best to help you")
print("[Type Bye to exit]")
while 1:
	questionStudent = raw_input('Question: ')
	questionStudent.replace(' ','-')
	if questionStudent == "Bye":
		break
	else:
		shorter = []
		for answer in answers:
			counter=counter+1
			splitAnswer = answer.split()
			splitQuestion = questionStudent.split('-')
			ans = []
			for word in splitAnswer:
				for wordq in questionStudent:
					ans.append(distance(model[word],model[wordq]))

			print(sum(ans))
			shorter.append(sum(ans))
	t = min(shorter)
	index=0
	for s in shorter:
		if(t == s):
			print(t)
			print(answers[index])
		index=index+1
