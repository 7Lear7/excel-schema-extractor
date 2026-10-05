import sys, json
from .extractor import extract_columns

if __name__ == "__main__":
    print(json.dumps(extract_columns(sys.argv[1]), indent=2, ensure_ascii=False))
