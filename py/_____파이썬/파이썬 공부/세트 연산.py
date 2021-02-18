# a|b 랑 set.union(a,b)는 결과가 같다.
# a&b 랑 set.intersection(a,b)는 결과가 같다.
# a-b 랑 set.difference(a,b)는 결과가 같다.
# a^b 랑 set.symmetric_difference(a,b)는 결과가 같다.

# a |= {5} 와 a.update({5}) 와 a.add(5) 는 같다
# a &= {2,3,4} 와 a.intersection_update({2,3,4}) 는 같다
# a -= {3} 와 a.difference_update({3}) 와 a.remove(3)? 와 a.discard(3) 는 같다
# a ^= {3,4,5,6} 와 a.symmetric_difference_update({3,4,5,6}) 는 같다

