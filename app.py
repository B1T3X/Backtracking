playing_board = [
    ['a', 'q', 'e', 't', 'o'],
    ['s', 'o', 't', 'a', 'm'],
    ['n', 'o', 'w', 'k', 'e'],
    ['c', 'v', 'a', 'h', 'h'],
    ['t', 'u', 'i', 'z', 'b']
]


def check_left(board, row, column, letter):
    if column != 0:
        if board[row][column - 1] == letter:
            print("found " + letter + " to the left")
            return True
    else:
        return False


def check_right(board, row, column, letter):
    if column != 4:
        if board[row][column + 1] == letter:
            print("found " + letter + " to the right")
            return True
    else:
        return False


def check_up(board, row, column, letter):
    if row != 0:
        if board[(row - 1)][column] == letter:
            print("found " + letter + " up")
            return True
    else:
        return False


def check_down(board, row, column, letter):
    if row != 4:
        if board[(row + 1)][column] == letter:
            print("found " + letter + " down")
            return True
    else:
        return False


def check_no_step_back(current_indexes, last_indexes):
    #TODO - fix!
    if current_indexes in last_indexes:
        print(current_indexes + " in " + last_indexes)
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
        print(index_in_word)
        if index_in_word != len(word):
            print(board[row_index][column_index])
            if board[row_index][column_index] == word[index_in_word]:
                return_word += word[index_in_word]
                print(last_indexes)
                index_in_word += 1
                if return_word == word:
                    return True
                elif check_left(board, row_index, column_index, word[index_in_word]) and not check_no_step_back([row_index, column_index], last_indexes):
                    last_indexes.append([row_index, column_index])
                    column_index -= 1
                elif check_right(board, row_index, column_index, word[index_in_word]) and not check_no_step_back([row_index, column_index], last_indexes):
                    last_indexes.append([row_index, column_index])
                    column_index += 1
                elif check_up(board, row_index, column_index, word[index_in_word])\
                        and not check_no_step_back([row_index, column_index], last_indexes):
                    last_indexes.append([row_index, column_index])
                    row_index -= 1
                elif check_down(board, row_index, column_index, word[index_in_word]):
                    last_indexes.append([row_index, column_index])
                    row_index += 1
                else:
                    return False
            elif column_index != 4:
                column_index += 1
            else:
                row_index += 1
                column_index = 0


print(is_word_on_board(playing_board, "snow"))
