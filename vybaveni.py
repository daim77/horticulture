# generuje seznam nutneho vybaveni na zvolene cinnosti
senam_cinnosti = {
    1: (
        'kul', 'tlouk', 'palice', 'hnojivo', 'pilka', 'pricka', 'hrebik_60_mm', 'hrebikovacka', 'uvazy', 'ryc',
        'krumpac', 'obaleni_kmenu', 'nuzky', 'nuz', 'strom', 'nahradni_kul', 'nahradni_pricka', 'lopata_srdcovka',
        'hrabe_svedske', 'hrabe_kovove', 'koste', 'pasmo', 'sprej'
    ),
    2: (
        'lopatka', 'hrabe_svedske', 'hrabe_kovove', 'hnojivo', 'lopata_srdcovka', 'koste', 'ryc', 'krumpac', 'nuzky',
        'nuz', 'trvalka', 'konev', 'mulc', 'pasmo', 'spej'
    ),
    3: (
        'provazek', 'sprej', 'palice', 'metr', 'pasmo', 'koliky', 'kolecko_kovove', 'vodovaha_velka', 'vodovaha_mala',
        'ryc', 'krumpac', 'nuz', 'strom', 'nahradni_kul', 'lopata_srdcovka', 'hrabe_svedske', 'hrabe_kovove', 'koste'
    ),
    4: 'stavba_zdi',
    5: (
        'valec', 'hrabe_kovove', 'hrabe_svedske', 'kolecko_kovove', 'semeno', 'pasmo', 'sprej'
    ),
    6: 'koseni_travniku',
    7: 'udrzba_zahonu',
    8: 'strihani_stromu',
    9: 'ostatni'
}
# seznamy materialu
strihani_stromu = {}
ostatni = {}
# VSTUPY
print('=' * 20)
print('Zvol planovane cinnosti na pracovni den. Napr.: 1 nebo 123 atd...')
print('=' * 20)
print(
    '''
        1    |    sazeni stromu
        2    |    sazeni trvalek
        3    |    stavba cesty
        4    |    stavba zdi
        5    |    travnik
        6    |    koseni travniku
        7    |    udrzba zahonu
        8    |    strihani stromu
        9    |    ostatni
    '''
)
print('=' * 20)
volba = input('Zadej tvuj plan na dnesni den: ')
print('=' * 20)
if not volba.isdigit():
    exit()
volba_list = list(volba)
for i in range(len(volba)):
    kompletni_seznam = set(seznam_cinnosti[int(volba_list.pop())])
    print(kompletni_seznam)
# OUTPUT

