def TopTen():
    yield 5

val = TopTen()
print(val)

def PerfectSq(n):
    for i in range(1,n):
        sq = i**2
        yield sq


values = PerfectSq(11)
for i in values:
    print(i)

# generators are used to create iterators.
# yield is used for generators.
# it will automatically generate iter and next function and raise StopIteration.
