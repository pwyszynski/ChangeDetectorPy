#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import urllib.request

import time

from bs4 import BeautifulSoup

from logger.logger import l
from detecting_machine.core.detector_meta import IDetector
from difflib import SequenceMatcher

__author__ = "Przemysław Wyszyński"

class WebChangeDetector(IDetector): # KOMPONENT KOMPOZYTU
    def __init__(self, **kwargs):
        self.target = kwargs.get("target")
        self.interval = kwargs.get("interval", 60*60)
        self.change_ratio = kwargs.get("ratio", 0.8)

    def detect(self):
        l.info_message("Looking for changes to site {}".format(self.target))
        old = ""

        while True:
            current = self._get_current_page_contents()
            if old == "":
                l.info_message("No previous data to compare for site {}, waiting for {} seconds.".format(self.target, self.interval))
                old = current
            else:
                if self._is_new_content_different(old, current, self.change_ratio):
                    l.update_message("Site {} has changed!".format(self.target))
                    old = current
                else:
                    l.info_message("Site {} hasn't changed. Waiting for {} seconds.".format(self.target, self.interval))

            time.sleep(self.interval)

    def _get_current_page_contents(self):
        def visible(element):
            if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
                return False
            elif re.match('<!--.*-->', str(element)):
                return False
            return True

        with urllib.request.urlopen(self.target) as page:
            source = page.read()
            soup = BeautifulSoup(source, "html.parser")
            [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
            visible_text = soup.getText()

        return visible_text

    def _is_new_content_different(self, old, new, min_ratio):
        ratio = SequenceMatcher(None, old, new).ratio()

        if ratio < min_ratio:
            return True
        else:
            return False
