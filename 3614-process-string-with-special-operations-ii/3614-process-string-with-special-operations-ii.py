class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)

        lengths = [0] * n
        cur = 0

        # Forward pass: compute lengths
        for i, ch in enumerate(s):
            if 'a' <= ch <= 'z':
                cur += 1
            elif ch == '*':
                if cur > 0:
                    cur -= 1
            elif ch == '#':
                cur *= 2
            else:  # '%'
                pass

            lengths[i] = cur

        if k >= cur:
            return '.'

        # Backward pass
        for i in range(n - 1, -1, -1):
            ch = s[i]

            before = lengths[i - 1] if i > 0 else 0
            after = lengths[i]

            if 'a' <= ch <= 'z':
                if k == before:
                    return ch

            elif ch == '*':
                # deleted last char; surviving indices unchanged
                pass

            elif ch == '#':
                if before > 0:
                    k %= before

            else:  # '%'
                if before > 0:
                    k = before - 1 - k

        return '.'