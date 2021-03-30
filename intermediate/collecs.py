from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

# Counter
name = 'Sekardayu Hana Pradiani'
counter = Counter(name)
print(counter)
print(counter.keys())
print(counter.values())
print(counter.most_common(1))
print(list(counter.elements()))

# namedtuple
Point = namedtuple('Point', 'x,y')
pt = Point(1, 2)
print(pt)

# OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 0
ordered_dict['b'] = 1
ordered_dict['c'] = 2
print(ordered_dict)

# defaultdict
dd = defaultdict(float)
print(dd)
dd['a'] = 1.2
dd['b'] = 2.1
dd['c'] = 'sekar'
print(dd)

# deque
dq = deque()

dq.append(1)
dq.append(2)
print(dq)
dq.appendleft(3)
print(dq)
dq.pop()
dq.popleft
dq.clear
dq.extend([1, 2, 3])
dq.extendleft([1, 2, 3])
dq.rotate(1)
dq.rotate(-1)