# -*- coding: utf-8 -*-
"""Tests all the solutions for all the problems. Invoke the file as:

    python test_problems.py
"""


from unittest import main, TestCase
from glob import glob
import sys
import os.path as op

# Set the name here
SOLUTIONS_DIR = '../solutions/'

PYTHON_NAMES = dict([
    ('p3', 'p3_basic_backtracking.py'),
])

# Add the src directory
sys.path.append('../src')


class TestProblems(TestCase):
    def setUp(self):
        pass


def _remove_spaces(str):
    return '\n'.join([line.strip() for line in str.strip().split('\n')])


def test_generator(test_module, python_file, infile, outfile):
    def test(self):
        with open(infile, 'r') as f:
            input = f.read()

        with open(outfile, 'r') as f:
            output = f.read()

        actual = test_module.run_code_from(python_file, input)
        self.assertEqual(_remove_spaces(output), _remove_spaces(actual))

    return test


for problem_dir in glob('../problems/p3'):
    problem = op.basename(problem_dir)
    for infile in glob(op.join(problem_dir, '../p6/in', 'input*.txt')):
        input_name = op.splitext(op.basename(infile))[0]
        outfile = op.join(problem_dir, '../p6/out', 'output' + input_name.split('input')[-1] + '.txt')
        name = '%s_%s' % (problem, input_name)

        python_file = op.join(op.abspath(SOLUTIONS_DIR), PYTHON_NAMES[problem])

        # Load the test file
        sys.path.append(op.abspath(problem_dir))
        test_module = __import__('test_%s' % problem)
        setattr(TestProblems, 'test_%s' % name, test_generator(test_module, python_file, infile, outfile))
        sys.path.remove(op.abspath(problem_dir))

if __name__ == '__main__':
    main()
