def check(dict1, dict2, key_ch):
	return key_ch in dict1 and key_ch not in dict2 and "One's empty" or \
		key_ch in dict2 and key_ch not in dict1 and "One's empty" or\
		dict1[key_ch] == dict2[key_ch] \
		or not dict1[key_ch] == dict2[key_ch] and "Not the same"
