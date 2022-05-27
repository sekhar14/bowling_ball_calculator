#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scorer import score_calculator 

test_data = [
    {
        "score" : 100,
        "input" : [
            (5, 2),
            (3, 5),
            (5, 0),
            (4, 1),
            (9, 1),
            (5, 1),
            (7, 1),
            (10, 0),
            (5, 2),
            (10, 10, 2)
        ]
    }
]

def test_scorer():
    for test_instance in test_data:
        assert test_instance["score"] == \
            score_calculator(test_instance["input"])
