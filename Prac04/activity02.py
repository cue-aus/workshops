__author__ = 'Cue'

scores = []
score = int(input("Score: "))
while score >= 0:
    scores.append(score)
    score = int(input("Score: "))
print(scores)
if scores != []:
    print("Your highest score is", max(scores))