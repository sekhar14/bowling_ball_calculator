#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "sekharbanarjee14@gmail.com"

from typing import List, Tuple

import logging

def score_calculator(user_input : List[Tuple[int, int]]) -> int:
    """
        Calculates the score of a full round of bowling,
        based on user input and pre-defined rule.

        @param: user_input
            array of tuple.
            one tuple represents on frame and consists of 2
            attempts and the number representing number of pins
            knocked down.

            Sample format :
                [(3, 7), (10, 0) ....... (10, 10, 10)]
                the len of list will be 10 i.e number of frames
                the last frame tuple size can be upto 3

        @return: final_score
            final score calculated based on the scoring rules.
    """
    # score sheet initialization
    final_score = 0
    for ind, frame in enumerate(user_input):
        logging.debug(f"score on frame {ind} : {final_score}")
        if ind == 9:
            # this is the 10th frame
            if frame[0] == 10:
                # strike in the first roll
                final_score += sum(frame)
            elif frame[0] + frame[1] == 10:
                # spare
                final_score += sum(frame)
            elif frame[0] + frame[1] < 10:
                final_score += frame[0] + frame[1]
        else:
            if frame[0] == 10:
                # this is a strike
                # score : 10 + pins knocked in next two rolls
                final_score += 10 + sum(user_input[ind + 1])
            elif sum(frame) == 10:
                # this is a spare
                final_score += 10 + user_input[ind + 1][0]
            elif sum(frame) < 10:
                final_score += sum(frame)
    return final_score


