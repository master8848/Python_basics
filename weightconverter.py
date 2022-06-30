weight_type=input("what weight to convert'kg or pound: ")
weight =float(input("input weight: "))
if weight_type.upper()=="KG":
	print(weight * 2.20462)
else:
	print(weight /2.20462)