class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        counter = 0
        if n == 0:
            return True
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            flowerbed[0] = 1 
            counter +=1 
        if counter == n:
            return True

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i == 0:
                    if flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        counter += 1
                elif i == len(flowerbed)-1:
                    if flowerbed[i-1] == 0:
                        flowerbed[i] = 1
                        counter += 1
                elif flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i]=1
                    counter += 1
            if counter == n:
                return True

        return False

        