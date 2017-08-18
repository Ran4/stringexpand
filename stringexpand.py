from typing import List, Tuple
from functools import wraps

def find_braces(s: str) -> Tuple:
    return (s.index("{"), s.index("}"))

def string_contains_set_of_braces(s: str) -> bool:
    return s.find("}") > s.find("{") >= 0

def split_brace_contents(s: str) -> List[str]:
    return s.split(",")

def expand(s: str) -> List[str]:
    if not string_contains_set_of_braces(s):
        return [s]

    expanded_strings = []
    begin_brace, end_brace = find_braces(s)
    brace_contents = s[begin_brace+1:end_brace]
    
    for content in split_brace_contents(brace_contents):
        expanded_string = "{before_brace}{content}{after_brace}".format(
            before_brace=s[:begin_brace],
            content=content,
            after_brace=s[end_brace+1:],
        )
                
        expanded_strings.append(expanded_string)
            
    # There might still be more strings to expand
    new_list = []
    for expanded_string in expanded_strings:
        if string_contains_set_of_braces(expanded_string):
            new_list += expand(expanded_string)
        else:
            new_list.append(expanded_string)
    return new_list
