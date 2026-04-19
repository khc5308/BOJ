L,A,B,C,D=int(input()),int(input()),int(input()),int(input()),int(input())
print(L-max(A//C if A/C == int(A/C) else A//C+1,B//D if B/D == int(B/D) else B//D+1))