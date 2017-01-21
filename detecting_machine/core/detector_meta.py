#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import ABCMeta
from abc import abstractmethod

__author__ = "Przemysław Wyszyński"

class IDetector(metaclass=ABCMeta):
    @abstractmethod
    def detect(self):
        pass