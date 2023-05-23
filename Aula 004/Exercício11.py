"""Sabe-se que:
◼ 1 pé = 12 polegadas
◼ 1 jarda = 3 pés
◼ 1 milha = 1760 jardas
Faça um algoritmo que receba uma medida
em pés, faça as conversões a seguir e
mostre os resultados:
a) Polegadas
b) Jardas
c) milhas"""

pes = int(input("Medida em pés: "))
polegada = pes * 12
jarda = pes / 3
milha = jarda / 1760
print(f"===========Conversões==========\n"
      f"a) Polegadas: {polegada}\n"
      f"b) Jardas: {jarda}\n"
      f"c) Milhas: {milha:.4f}\n"
      f"===============================")
