#!/usr/bin/env python3

from brain_gamess.games import calc_game
from brain_gamess.logic import games_result


def main():
    games_result(calc_game)


if __name__ == '__main__':
    main()
