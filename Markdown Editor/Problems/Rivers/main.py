# work with these variables
rivers = set(input().split())
states = set(input().split())
no_overlap = rivers - states
print(no_overlap)
