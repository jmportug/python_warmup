from find import (	find,
			find_dir,
 
			get_sub_dir, 
			change_dir, 
			get_dir_list, 
			delete_dir, 
			make_dir,

			tree )
  

ctree = tree()
ctree.generate(ctree.root, 2, 0, "/1")
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
		
	elif(command[0] == "rm"):
		if(len(command) < 2):
			print("Give Delete Parameter")
		else:
			temp = delete_dir(command[1], sub_dir, ctree)
			if(temp == None): print("Not Found")
			
	elif(command[0] == "mkdir"):
		if(len(command) < 2):
			print("Gave Directory Name")
		else:
			make_dir(command[1], sub_dir, ctree)
	
	elif(command[0] == "p"):
		ctree.print_tree()
	
	elif(command[0] == "q"):
		break
	
	else:
		print("Command not Recognized")
