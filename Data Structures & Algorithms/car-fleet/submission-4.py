class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_cars = sorted([(pos, speed) for (pos, speed) in zip(position, speed)], key=lambda x: -x[0])
        fleet = len(speed) if len(sorted_cars) else 0
        prev = (target - sorted_cars[0][0]) / sorted_cars[0][1]
        curr = None
        for i in range(1, len(sorted_cars)):
            curr = (target - sorted_cars[i][0]) / sorted_cars[i][1]
            if curr <= prev:
                fleet -= 1
            else:
                prev = curr
        return fleet #3, 