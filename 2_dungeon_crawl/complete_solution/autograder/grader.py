import subprocess
import csv
# Compares the expected output to the actual based on naming convention
# Test Name: test{name}_{map/coord}.txt
# Sol Name: test{name}_{stack/queue}.txt
# Student output Name: student{name}_{stack/queue}.txt
# A test can have both stack and queue solutions available to compare
def compare_testcase(test_name, stack=True, queue=True):
    pass


# Runs the test based on the nameing convention. Can be run for both
# Input modes and both data structure types
def run_test(test_name, map=True, coord=True, stack=True, queue=True):
    pass


def main():
    test_list = open("test_list.csv", "r")
    reader = csv.DictReader(test_list)
    test_dict = {}
    for test in reader:
        if test['valid'] == "True":
            run_test(\
                test['name'], \
                bool(test['map']), \
                bool(test['coord']), \
                bool(test['stack']), \
                bool(test['queue']) \
            )
            point_possible += int(test['points'])
            if compare_testcase(test['name'], bool(test['stack'], bool(test['queue']):
                pass
                # add to dict
