test_dict = json.loads(input())

min_value = min(test_dict.values())
min_key = [key for key in test_dict if test_dict[key] == min_value]
max_value = max(test_dict.values())
max_key = [key for key in test_dict if test_dict[key] == max_value]
print(f"min: {str(min_key[0])}")
print(f"max: {str(max_key[0])}")
