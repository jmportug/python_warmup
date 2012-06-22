
# General comments:
# - In general, code looks good! It's cool that you essentially implemented the
# beginnings of a shell program. Though I think the point of the excercise was
# to create a command that traverses the actual file system rather than creating
# it's own tree structure. Maybe the task description was a little unclear.
# - Some comments would have been nice. Even if things seem obvious when writing
# them, that may not be the case to someone reading it (or to yourself, when you
# return to the code after a few months).
# - Regarding spaces vs. tabs for indentation: When you start writing code for
# go-storage, set your text editor to expand tabs to four spaces. I prefer tabs
# as well, fwiw, but it's important to stay consistent within a project.

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
			
        # It's great that you check that the input params are sane. But it's
        # better to raise an exception than to return a string error message.
        # One reason for this is that it becomes more immediately obvious when
        # looking at the code that you're handling an error condition. Another
        # is that if you just return a string the error may go unnoticed
        # (suppose that the calling function just passes the result along rather
        # than try to do something with it, for instance).
        #
        # (A general principle of error handling is that when something goes 
        # wrong things should blow up as early as possible.)
		if(num1 > 1 or num2 > 1): return "To many brackets"
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
				
	if(files==[]):
        # Here I think you should just return the empty array; a search that
        # doesn't find anything is not really an error condition.
		return "Not Found"
	else:
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
			
	if(files==[]):
		return "Not Found"
	else:
		return files
		
		
def find_specified(search, ctree):
	files = []
	for name in search:
		for n in ctree.leaves:
			ndir = n.split('/')
			
			if(not(name in files) and name == ndir[-1]):
				files.append(name)
				
	if(files==[]):
		return "Not Found"
	else:
		return files
	
		
def find_exact(search, ctree):
	for n in ctree.leaves:
		name = n.split('/')
		if(search == name[-1]):
			return ctree.leaves[n].value
			
	return "Not Found"
	
	
	
def find_dir(search_param, ctree):
	if('?' in search_param):
		search = search_param.split('?')
		return find_dir_single(search, ctree, [])
	elif('*' in search_param):
		search = search_param.split('*')
		return find_dir_multiple(search, ctree, [])
	elif('[' in search_param and ']' in search_param):
		num1 = num2 = 0
		
		for char in search_param:
			if(char == '['): num1 += 1
			elif(char == ']'): num2 += 1
			
		if(num1 > 1 or num2 > 1): return "To many brackets"
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
			
		return find_dir_specified(search, ctree, [])
	else:
		return find_dir_exact(search_param, ctree)
		

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
		
	if(dirs==[]):
		return "Not Found"
	else:
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
		
	if(dirs==[]):
		return "Not Found"
	else:
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
		
	if(dirs==[]):
		return "Not Found"
	else:
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
	ndir = cnode.value.split('/')[-1]
	
	if(ndir == search): return cnode
	
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
			return temp
			
		i+=1
		
	
def make_dir(add, cnode, ctree):
	name = cnode.value+"/"+add
	nd = node(name)
	
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
	
	
