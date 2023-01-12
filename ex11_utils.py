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

    pass

# not


def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    '''search recursively for all words in the length of n on the board'''
    # base case: len(word) = n
    # start with first square and concotanate to word
    # if last two in non_hit_combos backtrack
    # else move to next
    pass


def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:

    pass


def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
    pass
