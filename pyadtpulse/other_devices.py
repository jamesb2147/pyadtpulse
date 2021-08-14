"""Python class representing an ADT Pulse other device."""

import logging
from pyadtpulse.const import ( ADT_ZONES_URI )

LOG = logging.getLogger(__name__)

def assert_is_dict(var):
    """Assert variable is from the type dictionary."""
    if var is None or not isinstance(var, dict):
        return {}
    return var


class ADTOtherDevice(object):
    """ADT Pulse other device implementation."""

    def __init__(self, name, attrs, adtpulse_session):
        """Initialize ADT other device object.
        :param name: other device name
        :param attrs: other device attributes
        :param adtpulse_session: PyADTPulse session
        """
        self.name = name
        self._attrs = attrs
        self._session = adtpulse_session

        # make sure self._attrs is a dict
        self._attrs = assert_is_dict(self._attrs)

    def __repr__(self):
        """Representation string of object."""
        return "<{0}: {1}>".format(self.__class__.__name__, self.name)
      
    def lockDoor(self):
        return {}
      
    def unlockDoor(self):
        return {}

    @property
    def attrs(self):
        """Return other device attributes."""
        return self._attrs

    @attrs.setter
    def attrs(self, value):
        """Override other device attributes."""
        self._attrs = value

    def update(self):
        """Update other device properties."""
        self._attrs = self._session.refresh_attributes(self.name)
        self._attrs = assert_is_dict(self._attrs)
