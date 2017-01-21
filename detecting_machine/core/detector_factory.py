#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from detecting_machine.specific_detectors.web_change_detector import WebChangeDetector

__author__ = "Przemysław Wyszyński"

class WebDetectorFactory(object):
    @staticmethod
    def get_factory(factory):
        if factory == 'Wykop':
            return WykopDetectorFactory()
        elif factory == 'Onet':
            return OnetDetectorFactory()
        elif factory == 'Pracuj':
            return PracujDetectorFactory()
        raise TypeError('Nieznana firma.')

# Obiekty konkretnych fabryk tworzone przez fabrykę abstrakcyjną.
class WykopDetectorFactory(object):
    def __init__(self):
        self.target = "http://www.wykop.pl/mikroblog"

    def get_detector(self, interval = 10, ratio = 0.95):
        return WebChangeDetector(target = self.target, interval=interval, ratio=ratio)

class OnetDetectorFactory(object):
    def __init__(self):
        self.target = "http://www.onet.pl"

    def get_detector(self, interval = 10, ratio = 0.95):
        return WebChangeDetector(target = self.target, interval=interval, ratio=ratio)


class PracujDetectorFactory(object):
    def __init__(self):
        self.target = "https://www.pracuj.pl/praca/developer;kw/Gda%c5%84sk;wp"

    def get_detector(self, interval = 10, ratio = 0.95):
        return WebChangeDetector(target=self.target, interval=interval, ratio=ratio)
