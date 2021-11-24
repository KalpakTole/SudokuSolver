def display_board(board):
	print('\n\n')
	for i in range(81):
		if i!=0 and not i%27:
			print()
			print('-'*21,end='')
		if i!=0 and i%9 and not i%3:
			print('|',end=' ')
		if i!=0 and not i%9:
			print()
		print(board[i],end=' ')
	print('\n\n')
		
def get_row(x,board):
	si = (x//9)*9
	return board[si:si+9]

def get_col(x,board):
	si = x%9
	return [board[i] for i in range(si,81,9)]

def get_box(x,board):
	v1 = (x//27)*3
	v2 = ((x%9)//3)*3
	pos = 9*v1+v2
	box = [board[pos],board[pos+1],board[pos+2],board[pos+9],board[pos+1+9],board[pos+2+9],board[pos+18],board[pos+1+18],board[pos+2+18]]
	return box

def is_valid(num,ind,board):
	if num not in get_row(ind,board) and num not in get_col(ind,board) and num not in get_box(ind,board):
		return True
	return False

def is_placeable(vis,ind):
	if vis[ind]:
		return True
	return False

def get_previous_placeable_index(all_placeable_indices,ind):
	return all_placeable_indices[all_placeable_indices.index(ind) - 1]

def solve(vis,all_placeable_indices,board):
	ind = 0
	while ind >=0 and ind<=80:
		if is_placeable(vis,ind):
			f = True
			for i in range(board[ind]+1,10):
				if is_valid(i,ind,board):
					board[ind] = i
					f = False
					ind += 1
				if not f:
					break
			if f:
				board[ind] = 0
				ind = get_previous_placeable_index(all_placeable_indices,ind)
		else:
			ind += 1
	return board

def main():
	# board = [0]*81
	# board = [0,0,0,2,6,0,7,0,1,6,8,0,0,7,0,0,9,0,1,9,0,0,0,4,5,0,0,8,2,0,1,0,0,0,4,0,0,0,4,6,0,2,9,0,0,0,5,0,0,0,3,0,2,8,0,0,9,3,0,0,0,7,4,0,4,0,0,5,0,0,3,6,7,0,3,0,1,8,0,0,0]
	# board = [0,0,0,6,0,0,4,0,0,7,0,0,0,0,3,6,0,0,0,0,0,0,9,1,0,8,0,0,0,0,0,0,0,0,0,0,0,5,0,1,8,0,0,0,3,0,0,0,3,0,6,0,4,5,0,4,0,2,0,0,0,6,0,9,0,3,0,0,0,0,0,0,0,2,0,0,0,0,1,0,0]
	board = [0,2,0,0,0,0,0,0,0,0,0,0,6,0,0,0,0,3,0,7,4,0,8,0,0,0,0,0,0,0,0,0,3,0,0,2,0,8,0,0,4,0,0,1,0,6,0,0,5,0,0,0,0,0,0,0,0,0,1,0,7,8,0,5,0,0,0,0,9,0,0,0,0,0,0,0,0,0,0,4,0]
	vis = [True if ele==0 else False for ele in board]
	all_placeable_indices = [i for i in range(81) if vis[i]]
	print('--------------- QUESTION ---------------')
	display_board(board)
	newboard = solve(vis,all_placeable_indices,board)
	print('---------------- ANSWER ----------------')
	display_board(newboard)

main()
