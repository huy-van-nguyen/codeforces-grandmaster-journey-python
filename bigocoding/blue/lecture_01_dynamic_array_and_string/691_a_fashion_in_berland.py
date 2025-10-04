import sys
input = sys.stdin.readline

def check_jacket(v: list[int]) -> bool:
    n = len(v)
    if n == 1:
        return v[0] == 1
    return v.count(0) == 1

def solve() -> None:
    n = int(input())
    v = list(map(int, input().split()))
    print("YES" if check_jacket(v) else "NO")

if __name__ == "__main__":
    solve()
