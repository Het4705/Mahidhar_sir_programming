
#^ METHOD RESOLUTION ORDER

class A:pass
class B:pass
class C:pass
class D:pass
class E(A,D,B):pass
class F(C,D):pass
class G(E,F):pass






print(C.mro)
print(C.__mro__)