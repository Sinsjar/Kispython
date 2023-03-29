def main(*list):
	l = set(list)
	return [i for i in range(len(l))
	         if not(len(l[i] - l))][0]

list = []
for i in range(5):
	list.append(input())
print(list)

print(main(list))
