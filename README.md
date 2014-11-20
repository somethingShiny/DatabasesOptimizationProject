DatabasesOptimizationProject
============================

Currently the format of the queries is as nested lists. There is a single list called queries. Each element of that list is then a list of lines in the query. For example, with the query: 
```
Select *
From Boats
Where bid = 1
```
the list would look like `[['Select *', 'From Boats', 'Where bid = 1'], [{other query}], [{other query}]]`



## Useful things

[Python Tutorial](https://docs.python.org/2/tutorial/index.html)

[Python Language Reference](https://docs.python.org/2/reference/index.html)

[Python Standard Library Documentation](https://docs.python.org/2/library/index.html)

[Python Coding Standards](https://www.python.org/dev/peps/pep-0008)

[Good (free) Python IDE](https://www.jetbrains.com/pycharm/)

[Information on using graphviz from python](https://pypi.python.org/pypi/graphviz)

Once I look more closely at the assignment, I'll add more to the README to make things clearer.

### Notes on committing

1 There will be two (possibly more) branches. One will be master, one will be devel. Commit to __devel__.

2 If you want to create your own branch and push everything to that, go for it.

3 Remember to pull the most recent changes before you start working. It would be a waste of time if I already made the changes you spent hours working on.

4 Remember to push your work when you finish.
