from point import Point
from vector import Vector, UniteVector

if __name__ == "__main__":
    print("main program started".center(45, "-"))
    A = Point("A", 15, 25)
    B = Point("", 0, 0)
    B.from_point("B", A)

    print(A)
    print(B)
    print(B.from_origin)
    print(A == B)
    print(A + B)
    print(A.addition(B))
    u = Vector("U", 3, 6)
    print(u)
    print(A.translation(u))
    w = UniteVector("W", 5, 5)
    print(w)
