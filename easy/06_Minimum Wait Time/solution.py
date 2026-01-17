def minimumWaitingTime(queries):
    queries.sort()
    min_wait_time = 0

    for idx,query in enumerate(queries):
        queries_left = len(queries) - (idx+1)
        min_wait_time += (queries_left * query)
    return min_wait_time