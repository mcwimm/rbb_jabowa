#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@date: 2023-Today
@author: https://github.com/mcwimm
"""


class Jabowa:
    def __init__(self, b2, b3, max_growth, max_dbh, max_height, initial_dbh, time_step_length):
        self.b2 = b2
        self.b3 = b3
        self.max_growth = max_growth
        self.max_dbh = max_dbh
        self.max_height = max_height
        self.dbh = initial_dbh
        self.time = time_step_length

    def updateGeometry(self, f_resources, f_competition):
        self.height = (137 + self.b2 * self.dbh - self.b3 * self.dbh**2)
        self.growth = (
            self.max_growth * self.dbh *
            (1 - (self.dbh * self.height) / (self.max_dbh * self.max_height))
            /
            (274 + 3 * self.b2 * self.dbh - 4 * self.b3 * self.dbh**2) *
            f_resources * f_competition)
        self.dbh = self.dbh + self.growth * self.time / (3600 * 24 * 365.25)

    def getOutput(self):
        return {"height": self.height,
                "dbh": self.dbh,
                "growth": self.growth}
