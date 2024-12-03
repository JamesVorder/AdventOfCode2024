from typing import List

def parse_input_file():
    with open('input.txt') as f:
        return f.readlines()
    
def check_report(report: List[int]):
    increasing: bool = None

    for i in range(1, len(report)):
        # establish the direction of the report
        if increasing is None and report[i] > report[i-1]:
            increasing = True
        elif increasing is None and report[i] < report[i-1]:
            increasing = False
        elif increasing is None and report[i] == report[i-1]:
            return 0

        # Check the report for safety
        difference: int = report[i] - report[i-1]
        if not (
            (
                (increasing and report[i] > report[i-1]) 
                or (not increasing and report[i] < report[i-1])
            )
            and abs(difference) in [1, 2, 3]
        ):
            return 0
        
    return 1

def check_report_dampener(report: List[int]):
    """
    This function tests the report, but with the "problem dampener" enabled.
    The problem dampener is capable of tossing out one bad state.
    """
    dampened: bool = False  # Have we used the dampener yet?
    increasing: bool = None  # What direction are the numbers going?
    # Instead of just stepping through, we need two pointers.
    start: int = 0
    end: int = 1
    while end < len(report):
        unsafe: bool = False
        difference: int = report[end] - report[start]
        if 0 < abs(difference) <=3:
            if increasing is None:
                increasing = difference > 0
            elif (increasing and difference < 0) or (not increasing and difference > 0):
                # Then we were going the wrong direction
                unsafe = True
        else:
            unsafe = True
       
        if dampened and unsafe:
            return 0
        elif unsafe:
            dampened = True
        elif not unsafe:
            start += 1
        end += 1
    return 1
            

if __name__ == "__main__":
    lines: List[str] = parse_input_file()
    reports: List[List[int]] = []
    for line in lines:
        reports.append(list(map(int, line.split(' '))))
    
    num_safe_reports: int = 0
    for report in reports:
        # check if the report is safe
        # reports are safe if they either monotonically increase or decrease
        # and also if the difference between the numbers is at least 1 but less than 3
        # I think my best possible time complexity is O(NM) where N is the number of reports and M is the number of numbers in each report
        num_safe_reports += check_report(report)
    print(f"Number of safe reports: {num_safe_reports}")
