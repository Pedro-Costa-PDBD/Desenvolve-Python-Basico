import datetime
from datetime import date
data = date.today()
data_br = data.strftime('%d/%m/%Y')
print(f"Data: {data_br}")

from datetime import datetime
hora = datetime.now()
hora_br = hora.strftime('%H:%M')
print(f"Hora: {hora_br}")