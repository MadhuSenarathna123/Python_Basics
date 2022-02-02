# word = "python programming"

# ------------count characters (length)

# x = len(word)
# print(x)

# print(len("python programming"))

# -----------print paragraph
#
# para1 = "Video provides a powerful way to help you prove your point. " \
#         "When you click Online Video, you can " \
#         "paste in the embed code for the video you want to add. "
#
# print(para1)

# para2 = """Video provides a powerful way to help you prove your point.
#         When you click Online Video, you can
#         paste in the embed code for the video you want to add."""
#
# print(para2)

# -------------------add string
# x = "python"
# y = "programming"
#
# print(x + y)
# print(x + " " + y)
# print(x, y)

# ------------------------------------
# word = "python programming"
# a = word[17]
# b = word[-1]
# print(a)
# print(b)
# print(word[0:6])
# print(word[7:])
# print(word[:])

# --------------------------------
# a = "cat"
# print("r" + a[1:3])
# print(a[0:2] + "r")
# print(a[0] + "u" + a[2])

# ---------lower & upper
# word = "Python Programming"
#
# print(word.lower())
# print(word.upper())

# ------------remove space

# back-----(rstrip)
# word = "python   "
# print(word)
# y = word.rstrip()
# print(y)
#
# word2 = "pythonzzzz"
# print(word2)
# y2 = word2.rstrip("z")
# print(y2)

# front-----(lstrip)
# word = "     python"
# y = word.lstrip()
# print(y)

# word = "llllllpython"
# y = word.lstrip("l")
# print(y)

# both---(strip)
# word = "..........python......"
# y = word.strip(".")
# print(y)

# check

#start
# w1 = "Project"
# w2 = "Programming"
# w3 = "java"
#
# print(w1.startswith("P"))
# print(w2.startswith("p"))
# print(w3.startswith("ja"))

# end
w1 = "Project"
w2 = "Programming"
w3 = "java"

print(w1.endswith("ct"))
print(w2.endswith("ing"))
print(w3.endswith("A"))