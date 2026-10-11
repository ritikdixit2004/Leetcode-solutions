class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        if not points:
            return 0

        # Sort balloons primarily by their end coordinates
        points.sort(key=lambda x: x[1])

        arrows = 1
        current_arrow_pos = points[0][1]

        for start, end in points[1:]:
            # If the current balloon starts after the previous arrow position,
            # a new arrow must be shot at this balloon's end coordinate.
            if start > current_arrow_pos:
                arrows += 1
                current_arrow_pos = end

        return arrows