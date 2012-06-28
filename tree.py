class node:
	def __init__(self, value = ""):
		self.value = value
		self.sub_dirs = []
		
		
class tree:
	def __init__(self, root=node("/1")):
		self.root = root
		self.size = 1
		self.num_leaves=0
		self.leaves={}
#		self.generate(root, 2)

	def generate(self, cnode, max_depth=7, depth=0, dir_name="/1"):
		if(depth < max_depth):
			i=0
			while(len(cnode.sub_dirs)<3):
				self.size+=1
				name = dir_name+"/"+str(self.size)
				cnode.sub_dirs.append(node(name))
				self.generate(cnode.sub_dirs[i],max_depth,depth+1,name)
				i+=1
				
		if(len(cnode.sub_dirs) == 0):
                        self.num_leaves += 1
			self.leaves.update({dir_name+"/"+str(self.size):cnode})


	def print_tree(self):
		tree_list = []
		tree_list = self.print_tree_main(self.root, 1, [])
		for n in tree_list:
			print(n)


	def print_tree_main(self, cnode, depth=1, tree_list=[]):
		if(depth > len(tree_list)): tree_list.append('')
		tree_list[depth-1] += self.print_sub_dirs(cnode)

		i=0
		while(i<len(cnode.sub_dirs)):
			self.print_tree_main(cnode.sub_dirs[i], depth+1, tree_list)
			i+=1
			
		return tree_list


	def print_sub_dirs(self, cnode):
		temp = '['
		for n in cnode.sub_dirs:
			temp += n.value.split('/')[-1]
			temp += ' '

		temp += ']'
		if(temp != "[]"):
			return temp
		return ''

