#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading

from detecting_machine.core.detector_factory import WebDetectorFactory
from detecting_machine.core.detector_meta import IDetector

__author__ = "Przemysław Wyszyński"

class DetectingEngine(IDetector): # KOMPOZYT
    def __init__(self):
        self.detectors = []
        self.running_detectors = []

    def add_detector(self, detector):
        self.detectors.append(detector)

    def remove_detector(self, detector):
        self.detectors.remove(detector)

    def detect(self):
        for i in self.detectors:
            t = threading.Thread(target=i.detect)
            self.running_detectors.append(t)
            t.start()


if __name__ == "__main__":
    de = DetectingEngine()

    detector_factory = WebDetectorFactory()
    w1 = WebDetectorFactory.get_factory('Wykop').get_detector(11, 0.95)
    w2 = WebDetectorFactory.get_factory('Onet').get_detector()
    w3 = WebDetectorFactory.get_factory('Pracuj').get_detector(12)

    de.add_detector(w1)
    de.add_detector(w2)
    de.add_detector(w3)
    de.detect()