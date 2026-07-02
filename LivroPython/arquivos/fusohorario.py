from zoneinfo import ZoneInfo
from datetime import datetime

bruxelas = ZoneInfo('Europe/Brussels')
ny = ZoneInfo('America/ NovaYork')
tokio = ZoneInfo('Japan')
brasilia = ZoneInfo('Brazil/East')

agora = datetime.now()
print('*' *40)
print('Agora em:')
print('Bruxelas ', agora.astimezone(bruxelas))
print('Nova york: ', agora.astimezone(ny))
print('Tokio: ', agora.astimezone(tokio))
print('Brasil: ', agora.astimezone(brasilia))