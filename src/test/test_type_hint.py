from typing import Any, Callable, Dict, List, Optional, Sequence, Union


def f(a: int, b: str) -> str:
    return str(a) + b

# f(3, 4)
f(3, 's')

def g(l: List[str], d: dict):
    for i in l:
        d[i] = 1
    return d

l = ['zh-cn', 'en-us', 'Uzbik', 'Kob', 'vit'] # it's ok
d = {'ss': 2}
g(l, d)
print(d)

# TypeError: unhashable type: 'list' if l likes below
# l = ['zh-cn', 'en-us', 'Uzbik', 'Kob', 'vit', [1, 2]]

# fix that by annotate l: list[str], under py3.9 use List[str] instead

def _sum(a: Sequence[int]): # list or tuple all ok
    return sum(a)

sum((1, 2, 3))
sum([1, 3, 4])

def k(d: Dict[str, Union[str, int]]):
    # dict k allows str, value allows str and int
    [print(i, d[i]) for i in d]
d1 = {'china': '1', 'Us': '2', 'India': '咖喱', 'Jp': int(4), 'French': 'white flag'}
# k(d1)


def f1(gend: Optional[str]):
    print(gend)

def f2(f: Callable[[str], None]):
    f('aaa')
f2(f1)