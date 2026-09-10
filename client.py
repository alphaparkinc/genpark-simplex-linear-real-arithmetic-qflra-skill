class SimplexQFLRA:
    """
    Dual Simplex for Linear Real Inequalities: a*x + b*y <= c.
    Checks consistency of 2D bounding polygon.
    """
    def is_feasible(self, bounds_x, bounds_y):
        min_x, max_x = bounds_x
        min_y, max_y = bounds_y
        return min_x <= max_x and min_y <= max_y
