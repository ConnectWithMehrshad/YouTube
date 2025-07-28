from datetime import datetime, timedelta
from collections.abc import Iterator

class DateRange:
    def __init__(self, start_date: datetime, end_date: datetime):
        self.start_date = start_date
        self.end_date = end_date
    
    def __iter__(self) -> Iterator[datetime]:
        current_date = self.start_date
        while current_date < self.end_date:
            yield current_date
            current_date += timedelta(hours=1)

for date in DateRange(datetime(2025, 1, 1, 5), datetime(2025, 1, 1, 8)):
    print(date)

# 2025-01-01 05:00:00
# 2025-01-01 06:00:00
# 2025-01-01 07:00:00