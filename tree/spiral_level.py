def printSpiralLevelOrder(root):
    # Code here
    q = [root]
    s = []
    count = 2
    while q or s:
        if q:
            for x in q:
                print(x.data)
        if s:
            for x in s:
                print(x.data)

        if count % 2 == 0:
            while q:
                # print(q, end= ' ')
                if q[-1].left:
                    s.append(q[-1].left)
                if q[-1].right:
                    s.append(q[-1].right)
                del (q[-1])
        else:
            while s:
                # print(s, end= ' ')
                if s[-1].right:
                    q.append(s[-1].right)
                if s[-1].left:
                    q.append(s[-1].left)
                s.pop()
        count += 1