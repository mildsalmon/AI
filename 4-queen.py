def init():
    queen_count = 4
    queen_list = make_list(queen_count)
    draw(queen_list)

    return queen_count, queen_list

def make_list(queen_count):

    queen_list = [0]*queen_count*queen_count

    #
    # for i in range(queen_count):
    #     row = [0]*queen_count
    #
    #     queen_list.append(row)

    return queen_list

def draw(queen_list):
    print("------------------------")

    for i, queen in enumerate(queen_list):
        len_queen_count = int(len(queen_list) ** 0.5)

        print(queen, end="")

        if (i % len_queen_count) != (len_queen_count - 1):
            print(" | ", end="")
        elif (i % len_queen_count) == (len_queen_count - 1):
            print("\n--------------")

    # for i, queens in enumerate(queen_list):
    #     len_queen_list = len(queen_list)
    #
    #     for j, queen in enumerate(queens):
    #         len_queens = len(queens)
    #         print(queen, end="")
    #
    #         if j != len_queens-1:
    #             print(" | ", end="")
    #
    #     if i != len_queen_list-1:
    #         print("\n--------------")

def choice_queen(input_error):
    try:
        i = input("\nQueen을 위치할 자리를 선택하세요 (0~(4*n-1)) : ")
        i = int(i)

        input_error = False
    except Exception as e:
        print("에러가 발생했습니다. 다시 입력해주세요")
        print(e)
        input_error = True

    return input_error, i

def play_game():
    queen_count, queen_list = init()
    dump_queen_list = queen_list[:]
    input_error = True
    total_queen_count = queen_count*queen_count
    round_queen_game = queen_count

    while(round_queen_game > 0):
        if (dump_queen_list.count(0) == 0):
            print("더 이상 Queen을 둘 자리가 없습니다. 게임에서 지셨습니다.")
            break

        # Queen 자리 입력 받는 반복문 (올바른 숫자 값을 얻을 때까지)
        while(input_error):
            input_error, loc_num = choice_queen(input_error)
            try:
                if loc_num >= total_queen_count:
                    print("정해진 Queen 자리보다 큰 수입니다. 다시 입력해주세요.")
                    input_error = True
            except:
                pass

        input_error = True

        if dump_queen_list[loc_num] == 1:
            print("선택한 위치는 Queen 규칙에 따라 배치할 수 없는 위치입니다.")
            continue

        # Queen 문제 규칙이 적용된 Queen list
        row_start = loc_num - (loc_num % queen_count)
        row_end = (((loc_num + queen_count) // queen_count) * queen_count)

        # 선택한 Queen 자리와 같은 행을 추출해서 1로 채움
        for i in range(row_start, row_end):
            dump_queen_list[i] = 1

        # 선택한 Queen 자리와 같은 열을 추출해서 1로 채움
        col_start = loc_num % queen_count
        col_list = [col_start]

        for i in range(queen_count):
            if (col_start + queen_count) < (total_queen_count):
                col_start = col_start + queen_count
                col_list.append(col_start)
            else:
                break

        # 기울기가 -인 대각선
        minus_gradient_start = loc_num
        minus_gradient_list = []

        for i in range(queen_count):
            if minus_gradient_start // queen_count != 0:
                if (minus_gradient_start - queen_count) % queen_count != 0:
                    minus_gradient_start = minus_gradient_start - queen_count - 1
                else:
                    break

        minus_gradient_list.append(minus_gradient_start)

        for i in range(queen_count):
            if (minus_gradient_start + queen_count + 1) < (total_queen_count):
                if ((minus_gradient_start + queen_count) % queen_count) != (queen_count - 1):
                    minus_gradient_start = minus_gradient_start + queen_count + 1
                    minus_gradient_list.append(minus_gradient_start)
                else:
                    break

        # 기울기가 +인 대각선
        plus_gradient_start = loc_num
        plus_gradient_list = []

        for i in range(queen_count):
            if plus_gradient_start // queen_count != 0:
                if ((plus_gradient_start - queen_count) % queen_count) != (queen_count - 1):
                    plus_gradient_start = plus_gradient_start - queen_count + 1
                else:
                    break

        plus_gradient_list.append(plus_gradient_start)

        for i in range(queen_count):
            if (plus_gradient_start + queen_count - 1) < (total_queen_count):
                if (plus_gradient_start + queen_count) % queen_count != 0:
                    plus_gradient_start = plus_gradient_start + queen_count - 1
                    plus_gradient_list.append(plus_gradient_start)
                else:
                    break


        # 규칙에 따라 1을 채움
        for i in range(4):
            len_col_list = len(col_list)
            len_minus_gradient_list = len(minus_gradient_list)
            len_plus_gradient_list = len(plus_gradient_list)

            if i < len_col_list:
                dump_queen_list[col_list[i]] = 1
            if i < len_minus_gradient_list:
                dump_queen_list[minus_gradient_list[i]] = 1
            if i < len_plus_gradient_list:
                dump_queen_list[plus_gradient_list[i]] = 1

        # 사용자에게 출력될 Queen list
        round_queen_game = round_queen_game - 1
        queen_list[loc_num] = 1

        draw(dump_queen_list)

if __name__ == "__main__":
    # while(1):
    play_game()