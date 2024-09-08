def solution(friends, gifts):
    friends_len = len(friends)
    answer = [0]*friends_len
    
    friends_dict = {}
    for i, name in enumerate(friends):
        friends_dict[name] = i

    pyo = []
    gift_degree = []
    for i in range(friends_len):
        pyo.append([0]*friends_len)
        gift_degree.append([0,0])
    
    for gift in gifts:
        A, B = gift.split()
        A, B = friends_dict[A], friends_dict[B]
        pyo[A][B] += 1
        gift_degree[A][0] += 1
        gift_degree[B][1] += 1
    
    for i in range(friends_len):
        for j in range(friends_len):
            if i >= j: continue
            result = pyo[i][j] - pyo[j][i]
            if result > 0:
                answer[i] += 1
            elif result < 0:
                answer[j] += 1
            else:
                gift_degree_i = gift_degree[i][0] - gift_degree[i][1]
                gift_degree_j = gift_degree[j][0] - gift_degree[j][1]
                result_2 = gift_degree_i - gift_degree_j
                if result_2 > 0:
                    answer[i] += 1
                elif result_2 < 0:
                    answer[j] += 1
    return max(answer)