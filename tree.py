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
		
	def generate(self, cnode, max_depth=5, depth=0, dir_name="/1"):
		if(depth < max_depth):
			i=0
			while(i<5):
				self.size+=1
				name = dir_name+"/"+str(self.size)
				cnode.sub_dirs.append(node(name))
				self.generate(cnode.sub_dirs[i],max_depth,depth+1,name)
				i+=1
				
		if(len(cnode.sub_dirs) == 0):
			self.num_leaves += 1
			self.leaves.update({dir_name+"/"+str(self.size):cnode})
