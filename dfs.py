
def main():
	#entering the adjacency matrix depending on the graph	
	adj_matrix=[[0,1,1,0],
		    [0,0,1,0],
                    [1,0,0,1],
                    [0,0,0,1]]
	visited=[0,0,0,0]  # setting visited flags
	stack=[]           # DFS is executed using stacks
	stack.append(0)    # Appending the root node
	node=stack.pop()  
	print node
	visited[0]=1       # Setting the visited flag of node 0 to 1
	
	i=0                # We start our search from neighbours of node 0
	while True:        # To traverse through the different adjacency lists in the adjacency matrix
		
		for j in range(0,len(adj_matrix[i])):   # To traverse through individual adjacency lists of each node
			
			if adj_matrix[i][j]==1 and visited[j]==0:  # Checking if the nodes are adjacent to the node in consideration and checking if the visited flags for these nodes are not set already
				stack.append(j)  # If true then adding the nodes to the stack
				visited[j]=1     # Setting the corresponding nodes visited flag
			else:
				pass
			
		if (len(stack)==0):             # To get us out of the infinite loop
			break
		else:
			node=stack.pop()	# Print only when we have node in the stack		
			print(node) 
			i=node                  # Assigning i as the visited node


if __name__== "__main__":
	main()
