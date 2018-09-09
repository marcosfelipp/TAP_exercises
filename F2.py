def find_circle(element, dic_dominace, visited_nodes):
	visited_nodes.append(element)
	
	for children in dic_dominace[element]:
		if children in visited_nodes:
			print("There is a dominating circle.")
			exit();
		else:
			find_circle(children, dic_dominace, visited_nodes)


n = int(input())
vector_strings = []
dic_dominace = {}
elements = []

for j in range(n):
	vector_strings.append(input())
	elements.append(vector_strings[j].split()[0])
	dic_dominace[vector_strings[j].split()[0]] = [vector_strings[j].split()[i+2] for i in range(int(vector_strings[j].split()[1]))]


for element in elements:
	find_circle(element, dic_dominace, [])
	

print("There is no dominating circle.")