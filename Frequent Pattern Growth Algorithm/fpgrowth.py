import operator

class FP_node():
	def __init__(self, item , count = 1):
		self.item = item
		self.count = count 
		self.neighbor = None
		self.children = {}

	def add_child(self, l1, cnt=1):

		for item in l1:
			child = FP_node(item)

			if not isinstance(child, FP_node):
				raise TypeError("Add FP_node as children")


			if not child.item in self.children:
				self.children[child.item] = child				
				child.parent = self
				child.count = cnt
				self = child
			else:
				self = self.children[child.item]
				self.count += cnt 
		

	def traverse(self, con_fp):
		print(self.item , self.count , end = " -> ") ;
		con_fp.append((self.item , self.count))
		for child in self.children:
			self.children[child].traverse(con_fp)


	def depth_traversal(self, src,  dst, nodes, node):
		nodes.append(src)
		if(src == dst):
			nodes.append(self.count)
			node.append(nodes.copy())
			nodes.pop()
		else:
			for child in self.children:
				self.children[child].depth_traversal(self.children[child].item, dst, nodes, node)
		nodes.pop()
		return nodes

		


def Read_data():
	file = open("inputfp" , 'r')
	lines = file.read().splitlines()

	len_trans = len(lines)

	items = lines[0].split(' ')
	no_items = len(items)

	d = {}

	for l in items:
		d[l] = 0 

	for i in range(1, len_trans):
		items = lines[i].split(' ')
		for l in items:
			d[l] += 1  
	return d, lines ;






def sort_items(l, min_sup_item):
	size = len(l) 
	for sets in l:
		size = len(sets)
		for i in range(0, size):
			for j in range(0 , size-i-1):
				if(min_sup_item[sets[j]] < min_sup_item[sets[j+1]]):
					temp = sets[j]
					sets[j] = sets[j+1]
					sets[j+1] = temp
	return l








min_support_thres = 3
min_support, trans = Read_data()

min_sup_item = {}
freq_one = {}
l_set = []

for i in min_support.keys():
	if(min_support[i] >=  min_support_thres):
		min_sup_item[i] = min_support[i]

print(min_sup_item)


l = []
k = 0
for line in trans[1:]:
	l.append([])
	items = line.split(' ')
	no_items = len(items)
	for i in items:
		if(i in min_sup_item.keys()):
			l[k].append(i)
	k += 1 

trans = sort_items(l, min_sup_item)

print(trans)



n_node = FP_node(None)
	

for l in trans:
	n_node.add_child(l)
# n_node.traverse()



#  sorting min_sup_item


# applying dfs to traverse the node

sorted_x = sorted(min_sup_item.items(), key=operator.itemgetter(1))
print('\n',sorted_x) 



# Conditional Pattern Base
print("\nConditional Pattern Base")

nodes = {}
node = []
for l in sorted_x[:-1]:
	nodes[l[0]]  = []
	node = []
	n_node.depth_traversal(n_node.item, l[0], nodes[l[0]], node)
	nodes[l[0]] = node

print(nodes)

# Conditional FP tree
print("\nConditional FP Tree")




con_fp_tree = {}

for k in nodes.keys():
	n_node = FP_node(None)
	con_fp_tree[k] = []
	for l in nodes[k]:
		n_node.add_child(l[1:-2], l[-1])
	n_node.traverse(con_fp_tree[k])
	print()

print(con_fp_tree)


# Removing the items with not satisfying min_threshold criteria

for k in con_fp_tree.keys():
	for s in con_fp_tree[k]:
		if(s[1] < min_support_thres):
			con_fp_tree[k].remove(s)



print(con_fp_tree)







