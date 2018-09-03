from collections import Counter
t = int(input().strip())
for i in range(t):
	s = input().strip()
	shmeep = Counter(s)
	x = 0
	y = 0
	w = []
	z = []
	f = 0
	t = "t"
	ext = 5
	counter = 0
	for letter in shmeep:
		if shmeep[letter] % 2 == 1:
			counter += 1

	if counter > 1:
		print ("-1")
		t = "f"

	for letter in shmeep:
		y = 0
		if shmeep[letter] % 2 == 0:
			x = shmeep[letter]/2
			for e in range(len(s)):
				if s[e] == letter:
					if y < x:
						w.append(e + 1)
						y += 1
					else:
						z.append(e + 1)
		if shmeep[letter] % 2 == 1:
			x = shmeep[letter]/2
			for e in range(len(s)):
				if s[e] == letter:
					if y < x:
						w.append(e + 1)
						y += 1
					elif y > x:
						z.append(e + 1)
					elif y == x:
						ext =  e + 1
						y += 1
	if ext != 5:
		z.append(ext)
	z = z[::-1]
	if t == "t":
		for e in w:
			print(e),
		for o in z:
			print (o),
		print ("")
