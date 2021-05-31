def validate_subsets(subsets, one_set):
	for sub in subsets:
		if not set(sub).issubset(one_set):
			return False
	return True

