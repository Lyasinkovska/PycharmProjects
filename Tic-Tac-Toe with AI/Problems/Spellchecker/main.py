dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
words = input()
result = [word for word in words.split() if word not in dictionary]
if result == []:
    print("OK")
else:
    print("\n".join(result))
