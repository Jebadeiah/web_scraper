dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

words = input().split()

ret = [x for x in words if x not in dictionary]
if not ret:
    print('OK')
else:
    print("\n".join(ret))
