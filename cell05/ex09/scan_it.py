import sys
import re
if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    string_to_search = sys.argv[2]
    found_matches = re.findall(keyword, string_to_search)
    if not found_matches:
        print("none")
    else:
        print(len(found_matches))