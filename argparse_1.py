import argparse

parser = argparse.ArgumentParser()
parser.add_argument('name')
parser.add_argument('num', type=int)

args = parser.parse_args()

for _ in range(args.num):
    print(f"I'm sorry {args.name}")