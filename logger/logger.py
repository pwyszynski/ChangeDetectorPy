#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

__author__ = "Przemysław Wyszyński"

import threading


class Logger(object):
    __lock = threading.Lock()
    __instance = None

    @classmethod
    def instance(cls):
        if not cls.__instance:
            with cls.__lock:
                if not cls.__instance:
                    cls.__instance = cls()

        return cls.__instance



    def update_message(self, message):
        self._log_message(self._get_current_time(), "| UPDATE |", message)

    def error_message(self, message):
        self._log_message(self._get_current_time(), "| ERROR! |", message)

    def info_message(self, message):
        self._log_message(self._get_current_time(), "| INFORM |", message)

    def _log_message(self, *messages):
        print(*messages)

    def _get_current_time(self):
        return time.strftime("%H:%M:%S")

l = Logger.instance()