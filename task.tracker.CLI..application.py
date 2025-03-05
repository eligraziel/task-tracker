import argparse
import json
import os

def load_tasks():
    # Check if tasks .json exists , return[] or load tasks
    pass

def save_tasks(tasks):
    # save tasks to tasks .json
    pass

# define other functions here.
def main():
    parser = argparse.ArgumentParser(description='Task Tracker')
    subparsers = parser.add_subparsers(dest='command')
    add_parser = subparsers.add_parser('add', help='Add a new task')

    # add subparsers for each command
    args = parser.parse_args()
    load_tasks()
    if args.command == "add":
        pass
    # save tasks if modified

if __name__ == "__main__":
    main()