class Solution:
    MOD = 10**9 + 7

    def mat_mul(self, A, B):
        n = len(A)
        C = [[0] * n for _ in range(n)]

        for i in range(n):
            for k in range(n):
                if A[i][k] == 0:
                    continue

                a = A[i][k]

                for j in range(n):
                    if B[k][j] == 0:
                        continue

                    C[i][j] = (C[i][j] + a * B[k][j]) % self.MOD

        return C

    def mat_vec_mul(self, A, v):
        n = len(A)
        res = [0] * n

        for i in range(n):
            cur = 0
            row = A[i]

            for j in range(n):
                cur = (cur + row[j] * v[j]) % self.MOD

            res[i] = cur

        return res

    def apply_power(self, M, vec, exp):
        while exp:
            if exp & 1:
                vec = self.mat_vec_mul(M, vec)

            M = self.mat_mul(M, M)
            exp >>= 1

        return vec

    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1

        if n == 1:
            return m

        K = 2 * m

        # Base vector for length = 2
        base = [0] * K

        for i in range(m):
            base[i] = i               # up[i]
            base[m + i] = m - 1 - i   # down[i]

        # Transition matrix
        M = [[0] * K for _ in range(K)]

        # up'[i] = sum(down[j]) for j < i
        for i in range(m):
            for j in range(i):
                M[i][m + j] = 1

        # down'[i] = sum(up[j]) for j > i
        for i in range(m):
            for j in range(i + 1, m):
                M[m + i][j] = 1

        vec = self.apply_power(M, base, n - 2)

        return sum(vec) % self.MOD
        