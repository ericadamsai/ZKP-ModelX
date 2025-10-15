import sys
import json
from src.sovereign_core import ZKVSNodePrime

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Run AXIOMHIVE ZKVSNodePrime mandate.")
    parser.add_argument('--intent', type=str, required=True, help='User intent string')
    parser.add_argument('--context', type=str, default='', help='Context for mandate')
    args = parser.parse_args()
    framework = {"intent": args.intent, "context": args.context}
    node = ZKVSNodePrime()
    result = node.execute_mandate(framework)
    print(result)

if __name__ == "__main__":
    main()
