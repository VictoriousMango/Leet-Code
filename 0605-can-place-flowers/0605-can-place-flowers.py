class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) >= 2:
            if n and flowerbed[0] == flowerbed[1] and flowerbed[0] == 0:
                flowerbed[0] = 1
                n -= 1
            if n and flowerbed[-2] == flowerbed[-1] and flowerbed[-1] == 0:
                flowerbed[-1] = 1
                n -= 1
        else:
            if flowerbed[0] == 0 and n == 1:
                return True
        for i in range(1, len(flowerbed)-1):
            if n<1:
                break
            if flowerbed[i-1]==0 and flowerbed[i] == 0 and flowerbed[i+1] == 0 and n:
                flowerbed[i] = 1
                n -= 1
        print(flowerbed)
        return True if n==0 else False