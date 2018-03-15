import re
import os

# test = "what if i told 789 you that there are 432 12 15 things to do"

# f = open(os.path.expanduser("~/UMich/PythonForWeb/Week2/regex_sum_42.txt"))
f = open(os.path.expanduser("~/UMich/PythonForWeb/Week2/regex_sum_81414.txt"))


text = f.read()

x = re.findall('[0-9]+', text)

total = 0
for vals in x:
	total = int(vals) + total
	

print(total)
