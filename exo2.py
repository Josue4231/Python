#EXO2
#1)
votes = ["Alice", "Nour", "Alice", "Théo", "Nour", "Alice"]

dict_vote={}
for vote in votes:
    if vote in dict_vote:
        dict_vote[vote] += 1
    else :
        dict_vote[vote] = 1
print(dict_vote)

#2)
plus_vote = max(dict_vote, key=dict_vote.get)
print(f"Celui qui a  plus de vote est {plus_vote} avec {dict_vote[plus_vote]}.")