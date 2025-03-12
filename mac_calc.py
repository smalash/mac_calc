mac = "DE331323334353637"

# делим MAC на пары значений
split_mac = []
for i in range(0, 16, 2):
    split_mac.append(mac[i:i + 2])

# добавляем дополнительные статичные пары значений не зависящие от MAC
start = ["1", "1A", "1A"]
end = ["FF", "FF", "36", "34", "37", "37", "2E", "30", "34", "39", "2D", "30", "34", "5B", "38", "5D", "FF", "FF"]
h = start + split_mac + end

# переводим каждую пару в двоичную систему с добавлением нулей слева
hex_to_bin = []
for i in h:
    a = bin(int(i, 16))[2:]
    hex_to_bin.append(f"{a:0>8}")

# тут я хз что происходит
# наверняка у этого есть математическое название или какая-то короткая формула
# я же сделал просто по аналогии с примером расчёта
polinom = [0, 0, 0, 0, 0, 1, 1, 1]
hz = []
for x in hex_to_bin:
    hz.extend(map(int, x))
else:
    hz.extend(map(int, "0" * 8))
check = hz[:8]
for i in range(1, 233):
    g = []
    for j in range(8):
        if j == 7:
            x = hz[j + i]
        else:
            x = check[j + 1]
        if check[0] == 0:
            g.append(x)
        else:
            g.append(x ^ polinom[j])

    check = g

# переводим вычисленные значения обратно в шестнадцатеричную систему
A = "".join(map(str, check[:4]))
C = "".join(map(str, check[4:]))
A_hex = hex(int(A, 2))[2:].capitalize()
C_hex = hex(int(C, 2))[2:].capitalize()

# объединяем все части итоговой комманды
a1 = "$AA$01$1A$1A$"
a2 = "$".join(split_mac)
a3 = "$FF$FF$36$34$37$37$2E$30$34$39$2D$30$34$5B$38$5D$FF$FF$"
a4 = A_hex + C_hex
command = "".join((a1, a2, a3, a4))
print(command)
