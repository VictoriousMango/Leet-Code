from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        # Find S and assign an index to every L
        start_r = start_c = -1
        litter_id = {}

        for r in range(m):
            for c in range(n):
                ch = classroom[r][c]

                if ch == 'S':
                    start_r, start_c = r, c

                elif ch == 'L':
                    litter_id[(r, c)] = len(litter_id)

        k = len(litter_id)

        if k == 0:
            return 0

        full_mask = (1 << k) - 1

        # best[r][c][mask] = maximum energy with which
        # we have reached (r,c) having collected 'mask'
        #
        # Since k <= 10:
        # number of masks <= 1024
        best = [
            [
                [-1] * (1 << k)
                for _ in range(n)
            ]
            for _ in range(m)
        ]

        q = deque()

        # r, c, mask, remaining_energy
        q.append((start_r, start_c, 0, energy))
        best[start_r][start_c][0] = energy

        directions = (
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        )

        moves = 0

        while q:
            # BFS level-by-level
            for _ in range(len(q)):
                r, c, mask, curr_energy = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    # Cannot move if energy is already 0
                    if curr_energy == 0:
                        continue

                    new_energy = curr_energy - 1
                    new_mask = mask

                    cell = classroom[nr][nc]

                    # Collect litter
                    if cell == 'L':
                        idx = litter_id[(nr, nc)]
                        new_mask |= 1 << idx

                        # We can immediately return because BFS
                        # processes states in increasing distance.
                        if new_mask == full_mask:
                            return moves + 1

                    # Reset energy
                    if cell == 'R':
                        new_energy = energy

                    # Dominance optimization:
                    #
                    # If we have already reached this exact
                    # (position, collected-litter-mask) with
                    # >= energy, this state can never be better.
                    if new_energy <= best[nr][nc][new_mask]:
                        continue

                    best[nr][nc][new_mask] = new_energy

                    q.append(
                        (nr, nc, new_mask, new_energy)
                    )

            moves += 1

        return -1