class A:
    def foo(self) -> None:
        print("A.foo")

class B(A):
    def foo(self) -> None:
        print("B.foo")
        super().foo()

class C(A):
    def foo(self) -> None:
        print("C.foo")
        super().foo()

class D(A):
    def foo(self) -> None:
        print("D.foo")
        super().foo()

class E(B, C):
    def foo(self) -> None:
        print("E.foo")
        super().foo()

class F(C, D):
    def foo(self) -> None:
        print("F.foo")
        super().foo()

class G(E, F):
    def foo(self) -> None:
        print("G.foo")
        super().foo()

def main() -> None:
    g = G()
    g.foo()
    print(G.__mro__)

if __name__ == "__main__":
    main()
