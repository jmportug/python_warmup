# It's generally better to be explicit about your imports, e.g:
# from find import get_dir_list, delete_dir, (etc...)
#
# This makes it much easier to see out what's going on in the code, for instance
# when you call get_dir_list it's easy to figure out that it's a function found in the
# find module.
from find import *

ctree = tree()
ctree.generate(ctree.root)
print(ctree.size)
print(ctree.num_leaves)

sub_dir = ctree.root
sub_name = sub_dir.value.split('/')
sub_name = sub_name[-1]

while(True):
	command = raw_input("\n/"+sub_name+" Command: ")
	command = command.split()
	if(command == []): continue
	
	if(command[0] == "f"):
		if(len(command) < 2):
			print("Give Search Parameter")
			
		else:
			print(find(command[1], ctree))
				
	elif(command[0] == "fa"):
		if(len(command) < 2):
			print("Give Search Parameter")
		else:
			temp = find_dir(command[1], ctree.root)
			if(temp == None): print("Not Found")
			else: print(temp)
			
	elif(command[0] == "fd"):
		if(len(command) < 2):
			print("Give Searh Parameter")
		else:
			temp = find_dir(command[1], sub_dir)
			if(temp == None): print("Not Found")
			else: print(temp)
			
	elif(command[0] == "g"):
		if(len(command) < 2):
			print("Give Search Parameter")
		else:
			temp = get_sub_dir(command[1], ctree.root)
			if(temp == None): print("Not Found")
			else:
				sub_dir = temp
				sub_name = sub_dir.value.split('/')
				sub_name = sub_name[-1]
				
	elif(command[0] == "cd"):
		if(len(command) < 2):
			print("Give Search Parameter")
		else:
			temp = change_dir(command[1], sub_dir)
			if(temp == None): print("Not Found")
			else:
				sub_dir = temp
				sub_name = sub_dir.value.split('/')
				sub_name = sub_name[-1]
				
	elif(command[0] == "ls"):
		print(get_dir_list(sub_dir))
		
    # I think it would have been better to call these rm and mkdir. standard > non-standard.
	elif(command[0] == "d"):
		if(len(command) < 2):
			print("Give Delete Parameter")
		else:
			temp = delete_dir(command[1], sub_dir, ctree)
			if(temp == None): print("Not Found")
			
	elif(command[0] == "m"):
		if(len(command) < 2):
			print("Gave Directory Name")
		else:
			make_dir(command[1], sub_dir, ctree)
			
	elif(command[0] == "q"):
		break
	else:
		print("Command not Recognized")
