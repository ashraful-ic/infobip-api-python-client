# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.api.model.sms.mo.logs.MOLog import MOLog


class MOLogsResponse(DefaultObject):
    @property
    @serializable(name="results", type=MOLog)
    def results(self):
        """
        Property is a list of: MOLog
        """
        return self.get_field_value("results")

    @results.setter
    def results(self, results):
        """
        Property is a list of: MOLog
        """
        self.set_field_value("results", results)

    def set_results(self, results):
        self.results = results
        return self