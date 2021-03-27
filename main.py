#!/usr/bin/env python3

import sys
import logging
import random


logging.basicConfig(level=logging.INFO)


def check_num(arr):
    index = 0
    while index < len(arr):
        if type(arr[index] != float):
            return False
        index += 1

    return True


def get_solution(arr):
    if check_num(arr) is False:
        check = False
        no_copy = list(set(arr))
        arr = sorted(no_copy)

        if len(arr) == 0:
            return True

        if len(arr) == 1:
            return arr[0]

        if check is False:
            return arr[1]

    return True


def main():
    items = []
    index = 0
    while index < 60:
        a = round(random.uniform(0, 100), 2)
        items.append(a)
        index += 1

    logging.info(items)

    if get_solution(items) is True:
        logging.info("Something wrong with array")
        sys.exit(-1)

    item = str(get_solution(items))
    logging.info("Solution: %s", item)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info("До встречи!")
