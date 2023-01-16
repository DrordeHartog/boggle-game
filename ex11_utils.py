from typing import List, Tuple, Iterable, Optional

Board = List[List[str]]
Path = List[Tuple[int, int]]

NON_COMBO_HITS = ['bx,', 'cj,', 'cv,', 'cx,', 'dx,', 'fq,', 'fx,', 'gq,', 'gx,', 'hx,', 'jc,', 'jf,', 'jg,', 'jq,', 'js,', 'jv,', 'jw,', 'jx,', 'jz,', 'kq,', 'kx,', 'mx,', 'px,', 'pz,', 'qb,', 'qc,', 'qd,', 'qf,', 'qg,',
                  'qh,', 'qj,', 'qk,', 'ql,', 'qm,', 'qn,', 'qp,', 'qs,', 'qt,', 'qv,', 'qw,', 'qx,', 'qy,', 'qz,', 'sx,', 'vb,', 'vf,', 'vh,', 'vj,', 'vm,', 'vp,', 'vq,', 'vt,', 'vw,', 'vx,', 'wx,', 'xj,', 'xx,', 'zj,', 'zq,', 'zx']


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
    x, y = (0, 0)
    path = []
    # start with first square and concotanate to word
    for x in range(len(board)):
        for y in range(len(board)):
            _find_length_n_paths_helper(n, board, words, x, y, path, result)
    return result


def _find_length_n_paths_helper(n: int, board: Board, words: Iterable[str], word, x, y, path, result):
    # def find_words(board, words, n, x, y, path, result):
    if x < 0 or x >= 4 or y < 0 or y >= 4:
        return
    if board[x][y] in path:
        return
    word += board[x][y]
    if word[:-2] in NON_COMBO_HITS:
        word = word[:-len(board[x][y])]
        return
    if word in words and len(path) == n:
        result.append(path)
    for dx, dy in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
        -_find_length_n_paths_helper(board, words,
                                     n, x + dx, y + dy, path, result)
    # after backtracking pop last addition
    word = word[:-len(board[x][y])]
    path.pop()


def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    x, y = (0, 0)
    result = []
    for x in range(len(board)):
        for j in range(len(board)):
            _find_length_n_words_helper(n, board, words, x, y, [], result)
    return result


def _find_length_n_words_helper(n: int, board: Board, words: Iterable[str], x, y, cur_path, result) -> List[Path]:
    # def dfs(board, x, y, n, path, words, result):
    if x < 0 or x >= len(board) or y < 0 or y >= len(board[x]) or (x, y) in cur_path:
        return
    cur_path.append((x, y))
    # base case
    if len(cur_path) == n:
        word = ""
        for step in cur_path:
            x, y = step
            word += board[x][y]
        if word in words:
            result.append(cur_path[:])
    else:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                      (1, 1), (-1, -1), (-1, 1), (1, -1)]
        for dx, dy in directions:
            _find_length_n_words_helper(
                n, board,  words, x+dx, y+dy, cur_path, result)
    cur_path.pop()


def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
    pass
