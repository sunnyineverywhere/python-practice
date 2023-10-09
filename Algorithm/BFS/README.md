## 문제풀이 목록
**백준 13549 / 숨박꼭질 3**
- 간선의 길이가 다양한 그래프에서 BFS를 하고 있기 때문에 처음 찾은 경로가 최단이 아닐 수 있습니다.
- 역대 최단 거리보다 지금보다 가까울 때를 우선적으로 처리해야 합니다. 그런 의미에서 순서를 조정하여 항상 최단거리이게끔 문제풀이를 했을 뿐이지, 최적의 풀이는 아닐 수 있다고 생각합니다.
```python
if 0 < x*2 <= MAX and array[x*2] == -1:
    array[x*2] = array[x]
    q.appendleft(x*2)
for nx in (x - 1, x + 1):
    if 0 <= nx <= MAX and array[nx] == -1:
        array[nx] = array[x] + 1
        q.append(nx)
```