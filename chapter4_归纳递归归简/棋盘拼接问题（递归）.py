#board棋盘矩阵，size边长，tr方格左上行数，tc方格左上列数，dr缺失格子行数，dc缺失格子列数
def chessboard(board, size, tr, tc, dr, dc):
	lable = 0
	lable += 1
	size //= 2
	#缺失格子位于第一象限
	if dr < tr + size and dc < tc + size:
		chessboard(board, size, tr, tc, dr, dc)
	else:
		board[tr + size - 1][tc + size - 1] = lable
		chessboard(board, size, tr, tc, tr + size - 1, tc + size - 1)
	#第二象限
	if dr < tr + size and dc >= tc + size:
		chessboard(board, size, tr, tc + size, dr, dc)
	else:
		board[tr + size - 1][tc + size] = lable
		chessboard(board, size, tr, tc + size, tr + size - 1, tc + size)
	#第三象限
	if dr >= tr + size and dc < tc + size:
		chessboard(board, size, tr + size, tc, dr, dc)
	else:
		board[tr + size][tc + size - 1] = lable
		chessboard(board, size, tr + size, tc, tr + size, tc + size - 1)
	#第四象限
	if dr >= tr + size and dc >= tc + size:
		chessboard(board, size, tr + size, tc + size, dr, dc)
	else:
		borad[tr + size][tc + size] = lable
		chessboard(board, size, tr + size, tc + size, tr + size, tc + size)

size = 8
board = [[0 for i in range(size)] for j in range(size)]
chessboard(board, size, 0, 0, 0, 7)	#右上角缺失的8*8方格
print(board)
