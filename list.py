jedi = []
print(type(jedi))

jedi = ["Yoda","Luke","Obi-Wan","Anakin"]

print(jedi)

jedi.append("Luminara")
print(f"Após a inserção a lista contém: \n {jedi}")

jedi.append(input("Insira o nome de um jedi: "))
print(f'Após a inserção a lista contém: \n{jedi}')

jedi.insert(1, "Cebolinha")

print(jedi[3])

print(jedi[-1])
print(jedi)

for nome in jedi:
    print(nome)

