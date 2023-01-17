from typing import List, Tuple, Iterable, Optional

Board = List[List[str]]
Path = List[Tuple[int, int]]

NON_COMBO_HITS = ['bx,', 'cj,', 'cv,', 'cx,', 'dx,', 'fq,', 'fx,', 'gq,', 'gx,', 'hx,', 'jc,', 'jf,', 'jg,', 'jq,', 'js,', 'jv,', 'jw,', 'jx,', 'jz,', 'kq,', 'kx,', 'mx,', 'px,', 'pz,', 'qb,', 'qc,', 'qd,', 'qf,', 'qg,',
                  'qh,', 'qj,', 'qk,', 'ql,', 'qm,', 'qn,', 'qp,', 'qq', 'qs,', 'qt,', 'qv,', 'qw,', 'qx,', 'qy,', 'qz,', 'sx,', 'vb,', 'vf,', 'vh,', 'vj,', 'vm,', 'vp,', 'vq,', 'vt,', 'vw,', 'vx,', 'wx,', 'xj,', 'xx,', 'zj,', 'zq,', 'zx']


# def sub_in_words(word, words):
#     return any(w.lower().startswith(word.lower()) for w in words)


def sub_in_words(word, words):
    for w in words:
        if w.lower().startswith(word.lower()):
            return True
    return False


def in_board(board, x, y) -> bool:
    '''check that a set of given coordinates are within a given boggle board, returns True if in and False if out'''
    if x < 0 or x >= len(board) or y < 0 or y >= len(board[x]):
        return False
    return True


def is_valid_path(board: Board, path: Path, words: Iterable[str]) -> Optional[str]:
    '''checks two things. 1) that path is logical path in which all tuples are connected squares.
    2) that the word is a valid word'''
    # for each tuple check that in board, and within previous tuple range
    # if valid tuple concotanate to word
    # when finished with all tuples check word
    word = ''
    previous_coor = None
    for step in path:
        # check that step is in board
        for coor in step:
            # if not in board return none
            if not 0 <= coor <= len(board) - 1:
                return
        if previous_coor:
            if not check_adj(previous_coor, step):
                return
        previous_coor = step
        # for each step, updateword
        word += board[step[0]][step[1]]
    # after iterating over all steps check if final word is in words dict
    if word in words:
        return word


def check_adj(previous_coor, coor) -> bool:
    '''checks that coordinates are adjascent to the last value in path'''
    return abs(previous_coor[0] - coor[0]) in [0, 1] and abs(previous_coor[1] - coor[1]) in [0, 1]


def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    '''search recursively for all words in the length of n on the board'''
    result = []
    # path = []
    # start with first square and concotanate to word
    for x in range(len(board)):
        for y in range(len(board)):
            # if len(path) == 0:
            #     _find_length_n_paths_helper(
            #         n, board, words, '', x, y, path, result)
            # elif check_adj(path[-1], (x, y)):
            _find_length_n_paths_helper(
                n, board, words, '', x, y, [], result)

    return result


def _find_length_n_paths_helper(n: int, board: Board, words: Iterable[str], word, x, y, path, result):
    ''' from a given square search for all paths of valid words length of n that continue or begin from a
    certain square (depends on length of path).
    n: length of path
    board: boggle board
    words: iterable of words
    word: current substring consisting of the letters from the board in the current path
    x: row
    y: col
    path: list of tuple representing coordinates of steps taken so far on the board
    result: a list of paths length of n that are valid words on the board
    '''
    if not in_board(board, x, y) or (x, y) in path:
        return
    word += board[x][y]
    # if len(word) >= 2 and word[-2:].lower() in NON_COMBO_HITS:
    if len(word) >= 2 and not sub_in_words(word, words):
        word = word[:-len(board[x][y])]
        return
    path.append((x, y))
    if len(path) >= n:
        if word in words:
            result.append(path[:])
        path.pop()
        word = word[:-len(board[x][y])]
        return
    for dx, dy in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
        _find_length_n_paths_helper(n, board, words,
                                    word, x + dx, y + dy, path, result)
    # # after backtracking pop last addition
    word = word[:-len(board[x][y])]
    path.pop()


def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    '''search recursively for all words with paths that are the length of n on the board'''
    x, y = (0, 0)
    result = []
    # begin searching from every square on board
    for x in range(len(board)):
        for y in range(len(board)):
            _find_length_n_words_helper(
                n, board, words, '', x, y, [], result)
    return result


def _find_length_n_words_helper(n: int, board: Board, words: Iterable[str], word, x, y, path, result) -> None:
    ''' from a given square search for all paths of valid words length of n that continue or begin from a
    certain square (depends on length of path).
    n: length of word
    board: boggle board
    words: iterable of words
    word: current substring consisting of the letters from the board in the current path 
    x: row
    y: col
    path: list of tuple representing coordinates of steps taken so far on the board
    result: a list of paths that are valid words length of n on the board
    '''
    # check that (x, y) is on board
    if not in_board(board, x, y) or (x, y) in path:
        return
    # add current letter to word
    word += board[x][y]
    # check if word is a possible word or substring of word (there are certain 2 letter combos that arent possible in english)
    if len(word) >= 2 and word[-2:].lower() in NON_COMBO_HITS:
        word = word[:-len(board[x][y])]
        return
    # if possible substring then add current step to path
    path.append((x, y))
    # base case of path length of n
    if len(path) == n:
        # if good word add path to list
        if word in words:
            result.append(path[:])
        # in any case continue searching for other paths
        path.pop()
        word = word[:-len(board[x][y])]
        return
    else:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                      (1, 1), (-1, -1), (-1, 1), (1, -1)]
        for dx, dy in directions:
            _find_length_n_words_helper(
                n, board,  words, word, x+dx, y+dy, path, result)
    path.pop()


def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
    # dict of tuple keys and list values where the tuple is a word and its score, the value its path
    # the backtracking function finds words from length 2 until length 16 (longest possible word), checks
    # their score and adds them to the dict (filtering for max score)
    # returns a list of the dict
    paths: dict[str, Path] = {}
    cur_path = []
    for x in range(len(board)):
        print("x= ", x)
        for y in range(len(board)):
            print("y= ", y)
            _max_score_paths_helper(board, words, "", [], x, y, paths)
    result = []
    for key in paths:
        result.append(paths[key])
    return result


def _max_score_paths_helper(board: Board, words: Iterable[str], word: str, path, x: int, y: int, word_paths) -> None:
    if not in_board(board, x, y) or (x, y) in path:
        return
    word += board[x][y]
    if len(word) >= 2 and not sub_in_words(word, words):
        # word[-2:].lower() in NON_COMBO_HITS:
        word = word[:-len(board[x][y])]
        return
    path.append((x, y))
    # if word already exists in word_path dict then compare length of path and keep longest path
    if word in word_paths:
        if len(path) > len(word_paths[word]):
            word_paths[word] = path
    # if not in eord_path dict then add
    if word in words:
        word_paths[word] = path[:]
        # keep iterating through board
        # path.pop()
        # word = word[:-len(board[x][y])]
        # return
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                  (1, 1), (-1, -1), (-1, 1), (1, -1)]
    for dx, dy in directions:
        _max_score_paths_helper(board, words,
                                word, path, x + dx, y + dy, word_paths)
    # # after backtracking pop last addition
    word = word[:-len(board[x][y])]
    path.pop()
