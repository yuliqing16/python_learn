def wai_hanshu():
  a = []
  def nei_hanshu(canshu):
    a.append(canshu)
    return a

  return nei_hanshu

a = wai_hanshu()
print(a(123))
print(a(321))

b = wai_hanshu()
print(b(123))
print(b(321))