from typing import List, Generator
import unittest

from stringexpand import expand, string_contains_set_of_braces

def _parse_test_cases(lines: List[str]) -> Generator:
    INDENT = 4
    input = None
    expected_outputs = []
    for line in lines:
        if line.strip().startswith("#") or line.strip() == "":
            continue

        if line.startswith(" "*INDENT):
            if input is None:
                raise Exception("First line can't be indented!")
            expected_outputs.append(line[INDENT:])
        else:
            if input is not None:
                yield (input, expected_outputs)
            input = line
            expected_outputs = []
    yield (input, expected_outputs)
            
def get_test_cases_from_file():
    with open("tests/test_cases.txt") as f:
        lines = f.read().split("\n")
    return [x for x in _parse_test_cases(lines)]

class TestExpand(unittest.TestCase):
    def setUp(self):
        self.test_cases = get_test_cases_from_file()
        
    def test_expand(self):
        for input, expected_output in self.test_cases:
            print("{} -> {}".format(input, expected_output))
            self.assertEqual(
                expand(input),
                expected_output,
                "\nError on input '{}'".format(input))
            
class TestExpandHelpFunctions(unittest.TestCase):
    def test_string_contains_set_of_braces(self):
        ok_values = ["{}", "{  }", " { }", "foo {} bar", "foo { {} } bar"]
        bad_values = ["", "}{", "{   {", "}  }", " } } } "]
        for ok_value in ok_values:
            self.assertTrue(string_contains_set_of_braces(ok_value))
        for bad_value in bad_values:
            self.assertFalse(string_contains_set_of_braces(bad_value))
