# Python Build-In Function

[toc]

## 栈与队列 collections.deque([])

```
d = collections.deque([])
d.append ('a') # 在最右边添加一个元素，此时 d=deque ('a')
d.appendleft ('b') # 在最左边添加一个元素，此时 d=deque (['b', 'a'])
d.extend (['c','d']) # 在最右边添加所有元素，此时 d=deque (['b', 'a', 'c', 'd'])
d.extendleft (['e','f']) # 在最左边添加所有元素，此时 d=deque (['f', 'e', 'b', 'a', 'c', 'd'])
d.pop () # 将最右边的元素取出，返回 'd'，此时 d=deque (['f', 'e', 'b', 'a', 'c'])
d.popleft () # 将最左边的元素取出，返回 'f'，此时 d=deque (['e', 'b', 'a', 'c'])
d.rotate (-2) # 向左旋转两个位置（正数则向右旋转），此时 d=deque (['a', 'c', 'e', 'b'])
d.count ('a') # 队列中 'a' 的个数，返回 1
d.remove ('c') # 从队列中将 'c' 删除，此时 d=deque (['a', 'e', 'b'])
d.reverse () # 将队列倒序，此时 d=deque (['b', 'e', 'a'])
```



## 堆 heapq

堆是一种特殊的数据结构，它的通常的表示是它的根结点的值最大或者是最小。

```
heap = [] # 建立一个常见的堆
heappush(heap,item) # 往堆中插入一条新的值
item = heappop(heap) # 弹出最小的值
item = heap[0] # 查看堆中最小的值，不弹出
heapify(x) # 以线性时间将一个列表转为堆
item = heapreplace(heap,item) # 弹出一个最小的值，然后将 item 插入到堆当中。堆的整体的结构不会发生改变。
heappoppush() # 弹出最小的值，并且将新的值插入其中
merge() # 将多个堆进行合并
nlargest(n, iterbale, key=None) # 从堆中找出做大的 N 个数，key 的作用和 sorted ( ) 方法里面的 key 类似，用列表元素的某个属性和函数作为关键字
```

