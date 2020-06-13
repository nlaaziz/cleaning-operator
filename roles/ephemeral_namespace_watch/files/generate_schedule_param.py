import sys
from datetime import datetime,timedelta, date

namespace_creation_date = datetime.strptime(sys.argv[1], '%Y-%m-%dT%H:%M:%SZ')
namespace_exiry = sys.argv[2]
end_date = namespace_creation_date + timedelta(days=int(namespace_exiry))

print(end_date.strftime('%M %H %d %m %d'))
