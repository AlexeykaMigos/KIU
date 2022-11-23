max_score = -1
max_score_name = ""
max_avg = -1
max_avg_name = ""
inp = input()
while inp != "end":
    inp = inp.split()
    name = inp[0]
    scores = list(map(int, inp[1:]))
    if max(scores) > max_score:
        max_score = max(scores)
        max_score_name = name
    if sum(scores) / len(scores) > max_avg:
        max_avg = sum(scores) / len(scores)
        max_avg_name = name
    inp = input()
print(max_score_name)
print(max_avg_name)