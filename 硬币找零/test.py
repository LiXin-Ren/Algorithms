

N = int(input())
M = int(input())
maps = []
for i in range(N):
    maps.append([map(input(), int)])

# def findMinRoad(N, M, maps):
#     minMaps = []
#     for i in range(len(maps)):
#         minMaps.append(min(maps[i]))
#     return min(minMaps)

def Solve(N, M, maps):
     res = []
     if M == 2:
         for i in range(N):
             res.append(min(maps[i]))
     else:


