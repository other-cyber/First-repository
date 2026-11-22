import json
with open("quiz.json", "r", encoding="utf-8") as f:
    list_question =json.load(f)

count = 0
for d in list_question:
    for j in d.keys():
        print(j)   
        answer = input("Введите ответ: ")
        try:
            answer = int(answer)
        except ValueError:
            answer = answer
        for l in d.values():
            if answer == l:
                count+=1
print(count)
                