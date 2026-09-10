from client import SimplexQFLRA

def main():
    print("=== Testing Simplex QF_LRA Solver ===")
    simplex = SimplexQFLRA()

    # Feasible box: 0 <= x <= 10, -5 <= y <= 5
    box_ok = simplex.is_feasible((0.0, 10.0), (-5.0, 5.0))
    # Contradictory bounds: 10 <= x <= 5
    box_conflict = simplex.is_feasible((10.0, 5.0), (0.0, 1.0))

    print(f"Feasible box check: {box_ok}")
    print(f"Conflicting box check: {box_conflict}")

    assert box_ok is True
    assert box_conflict is False
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
