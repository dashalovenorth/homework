"""Calculates the three highest salaries and the percentage of all salaries to the top."""

def statistics(*divisions: tuple[str, dict[str, float]], limit: float | None = None) -> tuple[str, dict[str, float]]:
    """Extract top 3 salaries and percentage.

    Args:
        divisions: tuple(str, dict) - 
        limit: float | None = None - 

    Returns:
        tuple[str, dict[str, float]] -
    """    

    top_wages = []
    all_wages = []
    wages_limit = []


    for division in divisions:
        for wages in division[1].values():
            all_wages.append(wages)
            for wage in all_wages:
                if limit is not None:
                    if wage >= limit:
                        wages_limit.append(wage)
                else:
                    wages_limit.append(wage)

    top_wages = sorted(set(wages_limit), reverse = True)[:3] 
    percent = round(sum(top_wages) / sum(wages_limit) * 100, 2)

    return top_wages, percent

