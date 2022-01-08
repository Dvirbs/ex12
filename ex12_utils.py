def is_valid_path(board, path, words):
    if len(path) == 0:
        return
    current_cell = path[0]
    c_row, c_col = current_cell
    # check if we are in the board
    if not(0 <= c_row < len(board) and 0 <= c_col < len(board[0])):
        return
    word = board[c_row][c_col]
    # check if the cell in the board is legal and add the letter to the word
    for i, next_cell in enumerate(path[1:]):
        if next_cell in path[:i]:
            return
        c_row, c_col = current_cell
        n_row, n_col = next_cell
        if not(0<= n_row < len(board) and 0<= n_col < len(board[0])):
            return
        if not (0 <= abs(c_row - n_row) <= 1 and 0 <= abs(c_col - n_col) <= 1):
            return
        word += board[n_row][n_col]
        current_cell = next_cell
    if word in words:
        return word
    return


def find_length_n_paths_helper(board, words, n, y, x, path, paths):
    # checks if we are on board
    if not(0 <= y < len(board) and 0 <= x < len(board[0])):
        return
    # checks if the path's length is n
    if n == 0:
        # checks if the path represents a word on board
        if is_valid_path(board, path, words):
            paths.append(path)
        return True
    path.append((y, x))
    # finds cells on board to add to path
    for u in range(-1, 2):
        for v in range(-1, 2):
            if u == v == 0:
                continue
            next_path = path[:]
            if find_length_n_paths_helper(board, words, n - 1, y + u, x + v, next_path, paths):
                return


def find_length_n_paths(n, board, words):
    paths = []
    # finds cells to start a path on board and do the recursive help function with it
    for y in range(len(board)):
        for x in range(len(board[0])):
            find_length_n_paths_helper(board, words, n, y, x, [], paths)
    return paths


def find_length_n_words_helper(board, words, n, y, x, path, paths):
    # checks if the word is too long
    if n < 0:
        return
    # checks if the word's length is n
    if n == 0:
        # checks if the path represents a word on board
        if is_valid_path(board, path, words):
            paths.append(path)
        return True
    path.append((y, x))
    # finds cells to add to the path and continue the recursion
    for u in range(-1, 2):
        for v in range(-1, 2):
            if u == v == 0:
                continue
            next_path = path[:]
            if 0 <= y+u < len(board) and 0 <= x+v < len(board[0]):
                if find_length_n_words_helper(board, words, n - len(board[y][x]), y + u, x + v, next_path, paths):
                    return


def find_length_n_words(n, board, words):
    # checks if n is too long for the board
    if n > len(board) * len(board[0]):
        return []
    paths = []
    # finds cells to start the path on board and do the recursive help function with it
    for y in range(len(board)):
        for x in range(len(board[0])):
            find_length_n_words_helper(board, words, n, y, x, [], paths)
    return paths


def path_find_word(board, path):
    # returns word by the given path
    word = ""
    for y, x in path:
        word += board[y][x]
    return word


def max_score_paths(board, words):
    words_score = dict()
    # words_score: {word: core}
    for n in range(len(max(words)) + 1):
        for path in find_length_n_paths(n, board, words):
            path_word = path_find_word(board, path)
            path_score = len(path) ** 2
            if path_word in words_score:
                if words_score[path_word] < path_score:
                    words_score[path_word] = path_score
            else:
                words_score[path_word] = path_score
    return sum(words_score.values())