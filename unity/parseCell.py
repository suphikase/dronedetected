from get.address import address as addr
from get.channel import channel as chann
from get.encryption import encryption as encry
from get.name import name as name
from get.quality import quality as qual
from get.signalLevel import signal_level as signal

rules = {
    "Name": name,
    "Quality": qual,
    "Channel": chann,
    "Encryption": encry,
    "Address": addr,
    "Signal": signal
    } 

def parse_cell(cell):
    parsed_cell = {}
    for key in rules:
        rule = rules[key]
        parsed_cell.update({key: rule(cell)})
    return parsed_cell