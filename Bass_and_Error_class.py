from io import StringIO
from decimal import Decimal
from fractions import Fraction


class BaseClass():
    """
    Initial object.
    """

    def __init__(self):
        """
        Inheritance property.

        Args:
            self
        Returns:
            -
        Raises:
            -
        """

    @staticmethod
    def _tostring(obj, req=0):
        with StringIO() as s:
            for p, val in vars(obj).items():
                s.write("{2}{0}: {1}\n".format(p, val if not isinstance(val, BaseClass) else "", (req * '\t')))
                if isinstance(val, BaseClass):
                    s.write(BaseClass._tostring(val, req=req + 1))

            return s.getvalue()

    def __str__(self):
        """
        """
        return BaseClass._tostring(self)


class Error(BaseClass):
    """
    Stores errors and warnings.
    """

    def __init__(self):
        BaseClass.__init__(self)
        # self._message = None
        self._dictionery = {}
        self.isError = False
        self.isWarning = False
        self._warningdictionery = {}
        self.isException = False
        self._ExceptionMessage = None

    @staticmethod
    def _add(di, key, val):
        if key in di.keys():
            di[key].add(val)
        else:
            di[key] = set()
            if isinstance(val, list):
                for i in val:
                    di[key].add(i)
            else:
                di[key].add(val)

    @staticmethod
    def _tomessage(di):
        ifs = StringIO()
        for k, val in di.items():
            ifs.write("{0}: {1}\n".format(k, list(val)))
        return ifs.getvalue()

    @staticmethod
    def _dictmerge(d1, d2):
        for key, val in d2.items():
            Error._add(d1, key, val)

    @staticmethod
    def _to_serializable(d1):
        d = {}
        for key, val in d1.items():
            d[key] = list(val)
        return d

    # ERROR properties
    def addError(self, key, val):
        self.isError = True
        self._add(self._dictionery, key, val)

    @property
    def message(self):
        return Error._tomessage(self._dictionery)

    def errordict(self, dictionery_2):
        self._dictmerge(self._dictionery, dictionery_2)
        if len(self._dictionery) > 0:
            self.isError = True

    @property
    def dictionery(self):
        return Error._to_serializable(self._dictionery)

    # WARNING properties
    def addWarning(self, key, val):
        self.isWarning = True
        self._add(self._warningdictionery, key, val)

    @property
    def warningmessage(self):
        return self._tomessage(self._warningdictionery)

    def warningdict(self, dictionery_2):
        self._dictmerge(self._warningdictionery, dictionery_2)
        if len(self._warningdictionery) > 0:
            self.isWarning = True

    @property
    def warningdictionery(self):
        return Error._to_serializable(self._warningdictionery)


    # Exception properties
    def addException(self, ms):
        self.isException = True
        self._ExceptionMessage = ms

    @property
    def exceptionmessage(self):
        return self._ExceptionMessage

    def check_all_attr_for_negative(self):
        """
        checks all numeric attributes (float, int, Decimal, Fraction, and the real part of complex)
        to be grater then 0, if not adds Error.
        It has to be called specifically before return, since sometimes negative value is allowed.
        """
        for attr, value in vars(self).items():
            if isinstance(value, float) or isinstance(value, int) or \
               isinstance(value, Decimal) or isinstance(value, Fraction):
                if value < 0:
                    self.addError(attr, "{0} is negative ({1})".format(attr, value))

            elif isinstance(value, complex):
                if value.real < 0:
                    self.addError(attr, "{0} is negative ({1})".format(attr, value))

    def check_all_attr_not_none(self):
        """
        Checks all none private attributes to be not none.
        If it is None it adds an error.
        It has to be called specifically before return.
        """
        for attr, value in vars(self).items():
            if value is None and attr[0] != "_":
                self.addError(attr, "{0} is None)".format(attr))
