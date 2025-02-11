# Rechnungssumme:
while True:
  try:
    bill = float(input("Wie hoch war die Rechnung in Euro? "))
    if bill >= 0:
      break
    print("Der Wert kann nicht negativ sein.")
  except:
    print("Bitte gib eine gültige Zahl ein (0-9 und Kommastelle mit '.')")
# Umrechnung in Cent:
bill = round(bill * 100)
# Ausgabe als Vollbetrag oder mit 2 Nachkommastellen: 
def euro(cents):
    if cents % 100 == 0:
        return str(int(cents/100))
    return str(cents // 100) + "." + str(cents % 100)
print(f"Die Rechnung beträgt {euro(bill)} Euro.")
# Servicequalitäten:
service_list = [
  {"quality": "schlecht", "percent": 0,  "round": 10},
  {"quality": "gut",      "percent": 10, "round": 100},
  {"quality": "super",    "percent": 20, "round": 500}
]
quality_list = str([s["quality"] for s in service_list])[1:-1]
# Abfrage Service:
service_dict = {}
found = False
while True:
  service_str = input(f"Wie war der Service? ({quality_list}): ")
  for service in service_list:
    if service["quality"] == service_str:
      service_dict = service.copy()
      found = True
      break
  if found:
    break
  print(f"'{service_str}' nicht gefunden. Es werden nur folgende Inputs akzeptiert:")
  print(quality_list)
  print()

print(f"Der Service war {service_dict["quality"]}.")
# Trinkgeld:
print(f"Deswegen geben wir ein Trinkgeld von {service_dict["percent"]} %.")
tip = round(bill * service_dict["percent"] / 100)
print(f"Das Trinkgeld beträgt {euro(tip)} Euro.")
total = bill + tip
print(f"In Summe macht das {euro(total)} Euro.")
# Aufrunden:
rounding = service_dict["round"]
print(f"Wir runden auf die nächsten {euro(rounding)} Euro.")
total = rounding * (total // rounding + (total % rounding > 0))
print(f"Wir bezahlen insgesamt {euro(total)} Euro.")
