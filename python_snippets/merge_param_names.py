missing_params = IN[0]
counts = len(missing_params)

merged = []
for i, p in enumerate(missing_params):
	if i == 0:
		merged.append(p + ",\n")
	elif i == counts - 1:
		merged[0] = merged[0] + p
	elif i > 0:
		merged[0] = merged[0] + p + ",\n"

OUT = merged