1. 列表推导式

例如 
```python
a = [1, 2, 3, 4, 5, 6, 7]

b = [x for x in a if x%2==0 ]
结果
>>> b = [x for x in a if x%2==0 ]
>>> b
[2, 4, 6]

c = [x for x in a if x%2==0 else i]
结果
  File "<stdin>", line 1
    c = [x for x in a if x%2==0 else i]
                                   ^
SyntaxError: invalid syntax

d = [x  if x%2==0 else x**2 for x in a]
>>> d
[1, 2, 27, 4, 125, 6, 343]
```

总结：

①[x for x in data if condition]

此处if主要起条件判断作用，data数据中只有满足if条件的才会被留下，最后统一生成为一个数据列表


②[exp1 if condition else exp2 for x in data]

此处if...else主要起赋值作用，当data中的数据满足if条件时将其做exp1处理，否则按照exp2处理，最后统一生成为一个
数据列表