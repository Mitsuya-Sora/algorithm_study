
import string


def get_edit_distance(s: str, t: str) -> int:
    min_cost = [[float('inf')] * (len(t) + 1) for j in range(len(s) + 1)]

    min_cost[0][0] = 0

    for i in range(len(s) + 1):
        for j in range(len(t) + 1):
            if i > 0 and j > 0:
                if s[i - 1] == t[j - 1]:
                    min_cost[i][j] = min([min_cost[i][j],
                                          min_cost[i - 1][j - 1]])
                elif s[i - 1] != t[j - 1]:
                    min_cost[i][j] = min([min_cost[i][j],
                                          min_cost[i - 1][j - 1] + 1])
            if i > 0:
                min_cost[i][j] = min([min_cost[i][j],
                                      min_cost[i - 1][j] + 1])
            
            if j > 0:
                min_cost[i][j] = min([min_cost[i][j],
                                      min_cost[i][j - 1] + 1])


    return min_cost[len(s)][len(t)]
                

if __name__ == "__main__":
    
    S = "bag"
    T = "big"
    print(get_edit_distance(S, T))
    # 1
    
    S = "ba"
    T = "bii"
    print(get_edit_distance(S, T))
    #2

    S = "logistic"
    T = "algorithm"
    print(get_edit_distance(S, T))
    # 6
    
    