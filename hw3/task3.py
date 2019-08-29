"""
    * Hanoi tower
"""


def hanoi(n, source, helper, target, cnt):
    print('hanoi( ', n, 's -> ', source, 'h -> ', helper, 't -> ', target, ' called')
    if n > 0:
        # move tower of size n - 1 to helper:
        cnt = hanoi(n - 1, source, target, helper, cnt)
        # move disk from source peg to target peg
        if source[0]:
            disk = source[0].pop()
            cnt += 1
            print(str(cnt) +
                " moving " +
                str(disk) +
                " from " +
                source[1] +
                " to " +
                target[1])
            if cnt % 1000 == 0:
                print(str(cnt))
            target[0].append(disk)

        # move tower of size n-1 form helper to target
        cnt = hanoi(n - 1, helper, source, target, cnt)
    return cnt
