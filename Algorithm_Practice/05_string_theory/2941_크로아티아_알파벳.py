# 크로아티아 알파벳	변경
# č	c=
# ć	c-
# dž	dz=
# đ	d-
# lj	lj
# nj	nj
# š	s=
# ž	z=
croatia_word = input()
for i in ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]:
    croatia_word = croatia_word.replace(i, "a")
print(len(croatia_word))

# 0.20
