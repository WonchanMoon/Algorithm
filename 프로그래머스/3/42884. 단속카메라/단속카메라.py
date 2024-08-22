def solution(routes):
    answer = 1
    
    routes.sort(key = lambda route : min(route))

    now = routes[0]
    for route in routes:
        if now[0] <= route[0] <= now[1]:
            now = [route[0], min(now[1], route[1])]
        else:
            answer += 1
            now = route
        
    return answer