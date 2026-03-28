import re

from dataclasses import dataclass
from datetime import timedelta


TS_RE = re.compile(r"^(\d{1,2}):(\d{1,2})(?::(\d{1,2}))?$")


def is_valid_timestamp(ts: str) -> bool:
    return bool(TS_RE.match(ts))

@dataclass(frozen=True)
class Timestamp:
    hour: int = 0
    minute: int = 0
    second: int = 0

    def __post_init__(self):
        """
        Validate the Timestamp after dataclass initialization.

        Dataclasses do not enforce type hints at runtime, so __post_init__
        provides a safe place to verify that all fields contain the correct
        types. 
        
        Because this class is frozen (immutable), validation must happen here
        to guarantee that a Timestamp can never be created in an invalid state.
        """
        if not isinstance(self.hour, int):
            raise TypeError("Timestamp hour must be of type int")
        
        if not isinstance(self.minute, int):
            raise TypeError("Timestamp minute must be of type int")
        
        if not isinstance(self.second, int):
            raise TypeError("Timestamp second must be of type int")
    
    @classmethod
    def from_string(cls, ts: str):
        if is_valid_timestamp(ts):
            parts = ts.split(":")

            # MM:SS
            if len(parts) == 2:
                m, s = parts
                return cls(0, int(m), int(s))

            # HH:MM:SS
            elif len(parts) == 3:
                h, m, s = parts
                return cls(int(h), int(m), int(s))

        raise ValueError(f"Invalid timestamp format: {ts}")

    def to_timedelta(self) -> timedelta:
        return timedelta(hours=self.hour, minutes=self.minute, seconds=self.second)
             
    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"

    def __repr__(self):
        return f"Timestamp({self.__str__()})"