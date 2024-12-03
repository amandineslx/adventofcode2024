import copy

INPUT_FILE = "02-input.txt"

def is_safe(report):
    increase = None
    if len(set(report)) != len(report):
        print(report)
        print("unsafe for repetition")
        return False
    sorted_report = copy.deepcopy(report)
    sorted_report.sort()
    sorted_report_reverse = copy.deepcopy(report)
    sorted_report_reverse.sort(reverse=True)
    if report != sorted_report and report != sorted_report_reverse:
        print(report)
        print("unsafe for sign")
        return False
    for i in range(len(report)-1):
        diff = report[i] - report[i+1]
        if abs(diff) > 3:
            print(report)
            print("unsafe for gap")
            return False
    #print("safe")
    return True

def is_a_sub_report_safe(report):
    for i in range(len(report)-1):
        sub_report = copy.deepcopy(report)
        sub_report.pop(i)
        #print(sub_report)
        if is_safe(sub_report):
            return True
    return False

def main():
    safe_reports = 0
    with open(INPUT_FILE, 'r') as f:
        for line in f.readlines():
            report = [int(x) for x in line[:-1].split(" ")]
            #print(report)
            if is_safe(report):
                safe_reports += 1
    print(safe_reports)

main()
