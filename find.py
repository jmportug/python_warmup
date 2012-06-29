from tree import *

def find(search_param, ctree):
	
	if('?' in search_param):
		search = search_param.split('?')
		return find_single(search, ctree)
	elif('*' in search_param):
		search = search_param.split('*')
		return find_multiple(search, ctree)
	elif('[' in search_param and ']' in search_param):
		num1 = num2 = 0
		
		for char in search_param:
			if(char == '['): num1 += 1
			elif(char == ']'): num2 += 1
			
#		if(num1 > 1 or num2 > 1): return "To many brackets"
		if(num1 > 1 or num2 > 1): raise RuntimeError, "To many brackets"
		temp = search_param.split('[')
		
		if(']' in temp[0]):
			return "Incorrect use of brackets"
			
		if(temp[1][-1] == ']'):
			param = temp[1][:-1]
		else:
			param = temp[1].split(']')[0]
			
		if(len(param) == 0): return "Put additional parameters within brackets"
		temp[1] = temp[1].split(']')[1]
		
		search = []
		for char in param:
			search.append(temp[0]+char+temp[1])
			
		return find_specified(search, ctree)
	else:
		return find_exact(search_param, ctree)
		
def find_single(search, ctree):
	files = []

	for n in ctree.leaves:
		ndir = n.split("/")
		name = ndir[-1]

		if(len(name) == len(search[0]+search[1])+1):
			if(search[0] != name[:len(search[0])]):
				continue
			elif(search[1] == name[len(search[0])+1:len(search[0])+len(search[1])+1]):
				files.append(name)
				
	return files
			
def find_multiple(search, ctree):
	files = []
	for n in ctree.leaves:
		ndir = n.split("/")
		name = ndir[-1]
		
		if(search[0] != name[:len(search[0])]):
			continue
		elif(search[1] == '' or search[1] == name[-len(search[1]):]):
			files.append(name)
			
	return files
		
		
def find_specified(search, ctree):
	files = []
	for name in search:
		for n in ctree.leaves:
			ndir = n.split('/')
			
			if(not(name in files) and name == ndir[-1]):
				files.append(name)
				
	return files
	
		
def find_exact(search, ctree):
	for n in ctree.leaves:
		name = n.split('/')
		if(search == name[-1]):
			return ctree.leaves[n].value
	

	
	
def find_dir(search_param, cnode):
	if('?' in search_param):
		search = search_param.split('?')
		return find_dir_single(search, cnode, [])
	elif('*' in search_param):
		search = search_param.split('*')
		return find_dir_multiple(search, cnode, [])
	elif('[' in search_param and ']' in search_param):
		num1 = num2 = 0
		
		for char in search_param:
			if(char == '['): num1 += 1
			elif(char == ']'): num2 += 1
			
#		if(num1 > 1 or num2 > 1): return "To many brackets"
		if(num1 > 1 or num2 > 1): raise RuntimeError, "To many brackets"
		temp = search_param.split('[')
		
		if(']' in temp[0]):
			return "Incorrect use of brackets"
			
		if(temp[1][-1] == ']'):
			param = temp[1][:-1]
		else:
			param = temp[1].split(']')[0]
			
		if(len(param) == 0): return "Put additional parameters within brackets"
		temp[1] = temp[1].split(']')[1]
		
		search = []
		for char in param:
			search.append(temp[0]+char+temp[1])
			
		return find_dir_specified(search, cnode, [])
	else:
		return find_dir_exact(search_param, cnode)
		

def find_dir_single(search, cnode, dirs):
	name = cnode.value.split('/')[-1]
	
	if(len(name) == len(search[0]+search[1])+1):
		if(search[0] != name[:len(search[0])]):
			pass
		elif(search[1] == name[len(search[0])+1:len(search[0])+len(search[1])+1]):
			dirs.append(name)
			
	num_dirs = len(cnode.sub_dirs)
	if(num_dirs == 0): return
	
	i=0
	while(i<num_dirs):
		find_dir_single(search, cnode.sub_dirs[i], dirs)
		i+=1
		
	return dirs
		
		
def find_dir_multiple(search, cnode, dirs):
	name = cnode.value.split('/')[-1]
	
	if(search[0] != name[:len(search[0])]):
		pass
	elif(search[1] == '' or search[1] == name[-len(search[1]):]):
		dirs.append(name)
		
	num_dirs=len(cnode.sub_dirs)
	if(num_dirs == 0): return
	
	i=0
	while(i<num_dirs):
		find_dir_multiple(search, cnode.sub_dirs[i], dirs)
		i+=1
		
	return dirs
		
		
def find_dir_specified(search, cnode, dirs):
	ndir = cnode.value.split('/')[-1]
	
	for name in search:
		if(not(name in dirs) and name == ndir):
			dirs.append(name)
			
	num_dirs=len(cnode.sub_dirs)
	if(num_dirs == 0): return
	
	i=0
	while(i<num_dirs):
		find_dir_specified(search, cnode.sub_dirs[i], dirs)
		i+=1
		
	return dirs
		
		
def find_dir_exact(search, cnode):
	ndir = cnode.value.split('/')[-1]
	
	if(ndir == search): return cnode.value
	
	num_dirs = len(cnode.sub_dirs)
	if(num_dirs == 0): return
	i=0
	while(i<num_dirs):
		if(cnode.sub_dirs[i] == None): return
		fdir = find_dir_exact(search, cnode.sub_dirs[i])
		if(fdir != None): return fdir
		i+=1
		
	return fdir
	
	
def get_sub_dir(search, cnode):
#	ndir = cnode.value.split('/')[-1]
	if(search == cnode.value): return cnode	
#	if(ndir == search): return cnode
	
	num_dirs=len(cnode.sub_dirs)
	if(num_dirs == 0): return
	
	i=0
	while(i<num_dirs):
		subdir = get_sub_dir(search, cnode.sub_dirs[i])
		i+=1
		if(subdir!=None): return subdir
		
	return subdir
	
	
def change_dir(search, cnode):
	dirs = get_dir_list(cnode)
	
	num_dirs = len(dirs)
	i=0
	while(i<num_dirs):
		if(search == dirs[i]): return cnode.sub_dirs[i]
		i+=1
		
		
def get_dir_list(cnode):
	dirs = []
	
	for n in cnode.sub_dirs:
		name = n.value.split('/')[-1]
		
		dirs.append(name)
		
	return dirs
	

def delete_dir(search, cnode, ctree):
	num_dirs = len(cnode.sub_dirs)
	
	i=0
	while(i<num_dirs):
		name = cnode.sub_dirs[i].value.split('/')[-1]
		
		if(name == search):
			temp = cnode.sub_dirs[i]
			temp_dir = temp.value
			
			delete_list = []
			for n in ctree.leaves:
				if(temp_dir in ctree.leaves[n].value):
					delete_list.append(n)
					
			for n in delete_list:
				del ctree.leaves[n]
				
			del cnode.sub_dirs[i]
			if(len(cnode.sub_dirs) == 0):
				ctree.leaves.update({cnode.value:cnode})
			return temp
			
		i+=1
		
	
def make_dir(add, cnode, ctree):
	name = cnode.value+"/"+add
	nd = node(name, cnode)
	
	if(len(cnode.sub_dirs) == 0):
	
		for n in ctree.leaves:
			if(n == cnode.value):
				del ctree.leaves[n]
				break
				
	else:
		for n in cnode.sub_dirs:
			if(n.value.split('/')[-1] == name):
				print("Directory already exists")
				return
				
	cnode.sub_dirs.append(nd)
	ctree.leaves.update({nd.value:nd})
	return nd


def add_node(add, cnode, ctree):
	for n in ctree.leaves:
		if(n == cnode.value):
			del ctree.leaves[n]
			break

	cnode.sub_dirs.append(add)
	update_leaves(add, ctree)


def update_leaves(cnode, ctree):
	if(len(cnode.sub_dirs) == 0):
		ctree.leaves.update({cnode.value:cnode})
	else:
		for n in cnode.sub_dirs:
			update_leaves(n, ctree)




