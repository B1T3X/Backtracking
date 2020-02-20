def check_left(board, row, column, letter):
    """
    Function to check if the given letter is to the left in the playing board
    :param board: Playing board - list of lists
    :type board: list
    :param row: Index of list in playing board (list of lists)
    :type row: int
    :param column: Index of individual square in playing board, in an individual row list
    :type column: int
    :param letter: Given letter to check on the playing board
    :type letter: str
    :return: True if next letter is to the left anf False if not
    :rtype: bool
    """
    if column != 0:
        if board[row][column - 1] == letter:
            # print("found " + letter + " to the left")
            return True
    else:
        return False


def check_right(board, row, column, letter):
    """
    Function to check if the given letter is to the right in the playing board
    :param board: Playing board - list of lists
    :type board: list
    :param row: Index of list in playing board (list of lists)
    :type row: int
    :param column: Index of individual square in playing board, in an individual row list
    :type column: int
    :param letter: Given letter to check on the playing board
    :type letter: str
    :return: True if next letter is to the left anf False if not
    :rtype: bool
    """
    if column != 4:
        if board[row][column + 1] == letter:
            # print("found " + letter + " to the right")
            return True
    else:
        return False


def check_up(board, row, column, letter):
    """
    Function to check if the given letter is above in the playing board
    :param board: Playing board - list of lists
    :type board: list
    :param row: Index of list in playing board (list of lists)
    :type row: int
    :param column: Index of individual square in playing board, in an individual row list
    :type column: int
    :param letter: Given letter to check on the playing board
    :type letter: str
    :return: True if next letter is to the left anf False if not
    :rtype: bool
    """
    if row != 0:
        if board[(row - 1)][column] == letter:
            # print("found " + letter + " up")
            return True
    else:
        return False


def check_down(board, row, column, letter):
    """
    Function to check if the given letter is below in the playing board
    :param board: Playing board - list of lists
    :type board: list
    :param row: Index of list in playing board (list of lists)
    :type row: int
    :param column: Index of individual square in playing board, in an individual row list
    :type column: int
    :param letter: Given letter to check on the playing board
    :type letter: str
    :return: True if next letter is to the left anf False if not
    :rtype: bool
    """
    if row != 4:
        if board[(row + 1)][column] == letter:
            # print("found " + letter + " down")
            return True
    else:
        return False


def check_no_step_back(current_indexes, last_indexes):
    if current_indexes in last_indexes:
        return True
    else:
        return False


def is_word_on_board(board, word):
    return_word = ""
    index_in_word = 0
    row_index = 0
    column_index = 0
    last_indexes = []
    while word != return_word:
        if index_in_word != len(word):
            if board[row_index][column_index] == word[index_in_word]:
                return_word += word[index_in_word]
                index_in_word += 1
                if return_word == word:
                    return True
                elif check_left(board, row_index, column_index, word[index_in_word])\
                        and not check_no_step_back([row_index, column_index], last_indexes):
                    last_indexes.append([row_index, column_index])
                    column_index -= 1
                elif check_right(board, row_index, column_index, word[index_in_word])\
                        and not check_no_step_back([row_index, column_index], last_indexes):
                    last_indexes.append([row_index, column_index])
                    column_index += 1
                elif check_up(board, row_index, column_index, word[index_in_word])\
                        and not check_no_step_back([row_index, column_index], last_indexes):
                    last_indexes.append([row_index, column_index])
                    row_index -= 1
                elif check_down(board, row_index, column_index, word[index_in_word])\
                        and not check_no_step_back([row_index, column_index], last_indexes):
                    last_indexes.append([row_index, column_index])
                    row_index += 1
                else:
                    return False
            elif column_index != 4:
                column_index += 1
            else:
                row_index += 1
                column_index = 0


if __name__ == "__main__":
    playing_board = [
        ['a', 'q', 'e', 't', 'o'],
        ['s', 'o', 't', 'a', 'm'],
        ['n', 'o', 'w', 'k', 'e'],
        ['c', 'v', 'a', 'h', 'h'],
        ['t', 'u', 'i', 'z', 'b']
    ]
    print(is_word_on_board(playing_board, "snow"))
    print(is_word_on_board(playing_board, "hawk"))
    print(is_word_on_board(playing_board, "carrot"))
