# Задача 9: Очистка адресов

addresses = [
    "  г. Москва, ул. Ленина, д. 10  ",
    "г.Казань,ул.Баумана,д.15",
    "  г. Санкт-Петербург, ул. Невский, д. 100  "
]

def clean(addr):
    addr = addr.strip()
    addr = addr.replace("г.", "г. ")
    addr = addr.replace("ул.", "ул. ")
    addr = addr.replace("д.", "д. ")
    while "  " in addr:
        addr = addr.replace("  ", " ")
    return addr

print("=== ОЧИСТКА АДРЕСОВ ===")
for i, addr in enumerate(addresses, 1):
    print(f"{i}. ДО: '{addr}'")
    print(f"   ПОСЛЕ: '{clean(addr)}'")