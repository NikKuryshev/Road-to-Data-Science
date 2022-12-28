"""

"""



drop_item = ('C3.DI9999', 'C3.DI9998', 'C3.DL0000', 'C3.DL0001', 'C3.DL0002', 'C3.DL0003', 'C3.DL0004', \
	'C3.DL0005', 'C3.DL0006', 'C3.AD9999', 'C3.TP9999', 'C3.MM9999', 'C3.SP9999', 'C3.CX9999', 'C3.IX9999', 'C3.UP9999', \
	'C3.WARRANTY2Y', 'C3.WARRANTY3Y', 'C3.WARRANTY4Y', 'C3.WARRANTY5Y', 'C3.DI9998', 'C3.DI9999', 'C3.DL0001', 'C3.DL0002', 'C3.DL0003', 'C3.DL0004', 'C3.DL0005')
rack = ('C3.RF', 'C3.RL', 'C3.RS', 'C3.RZ', 'C3.RP', 'C3.RB', 'C3.BS', 'C3.RW', 'C3.IP', 'C3.RW', 'C3.RP', 'C3.RB', 'C3.RO', 'C3.RI')
pdu_basic = ('C3.PH', 'C3.PA', 'C3.PV')
pdu_smart = ('C3.PM4', 'C3.PM3', 'C3.PM5', 'C3.PS4', 'C3.PS3')
pdu_sensor = ('C3.PM0001', 'C3.PM0002', 'C3.PM0003''C3.PM0004', 'C3.PM0005')
conditioner = ('C3.IX', 'C3.CX', 'C3.IW', 'C3.CW','C3.30SCA')
ats = ('C3.PS3001', 'C3.PS3002', 'C3.PS3003''C3.PS3004', 'C3.PS3005', 'C3.PS3006')
ups = ('C3.UP', 'C3.UPB', 'C3.UM')
tray = ('C3.TR', 'C3.TS', 'C3.TP')
aisle = ('C3.AD', 'C3.AB', 'C3.AR', 'C3.SD', 'C3.SE', 'C3.SC', 'C3.ST', 'C3.SR', 'C3.AX')
monitoring = ('C3.MM', 'C3.ME', 'C3.MS')

aggregation = {'Наименование':'first', 'Количество':'sum', 'Единица измерения':'first','Цена для конечного пользователя, руб.':'sum',
               'Стоимость для конечного пользователя, руб.':'sum', 'Проектная скидка':'mean', 'Цена с проектной скидкой,\n  руб.':'sum', 'Стоимость с проектной скидкой,\n  руб.':'sum'}
categories = {
	'Шкафы C3': rack,
	'Базовые БРП': pdu_basic,
	'БРП с мониторингом/управлением': pdu_smart,
	'Датчики БРП': pdu_sensor,
	'Кондиционеры': conditioner,
	'ИБП': ups,
	'АВР': ats,
	'Лотки': tray,
	'Изоляция': aisle,
	'Мониторинг AKCP': monitoring
}
