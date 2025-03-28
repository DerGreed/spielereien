import random

inventory_list = [
    "⚔️ Rostiges Eisenschwert",
    "🥋 Klapprige Holzrüstung",
    "🛡️ Durchlöchertes Holzschild",
    "🔪 Stumpfes Messer",
    "🧪 Abgelaufener Lebenstrank",
    "⚗️ Schimmeliger Zaubertrank",
    "❤️‍🩹 Stinkender Heiltrank"
]

poss = {
  "m": {"m": "sein", "f": "seine", "n": "sein", "p": "seine"},
  "f": {"m": "ihr", "f": "ihre", "n": "ihr", "p": "ihre"},
  "n": {"m": "sein", "f": "seine", "n": "sein", "p": "seine"},
  "p": {"m": "ihr", "f": "ihre", "n": "ihr", "p": "ihre"}
}

class character:
  def __init__(self, name, gender):
    self.name = name
    self.nameS = name + ("'" if name[-1] in ["s", "z"] else "s")
    self.poss = poss[gender]

def attack(attacker, target):
  print(f"{attacker.name} greift {target.name} mit ")

class weapons:
  def __init__(self, name, dmg_min, dmg_max, accuracy):
    self.name = name
    self.dmg_min = dmg_min
    self.dmg_max = dmg_max
    self.accuracy = accuracy
  def __str__(self):
    print(f"{self.name} ({self.dmg_min} - {self.dmg_max} dmg, {self.accuracy:.1%} %)")
  def attack(self, target):
    if random.random() > self.accuracy:
      print("Du hast verfehlt!")

class character:
  pass


def create_character():
  print("🎭 Erstelle deinen Charakter")
  name = input("Wie heißt dein Held? ")
  klasse = input("Was ist deine Klasse? ")
  spezies = input("Was ist deine Spezies? ")
  character = {
      "Name": name,
      "Klasse": klasse,
      "Spezies": spezies,
      "Angriff": random.randint(5, 20),
      "HP": 20,
      "Inventar": random.choices(inventory_list, k=2)
  }
  #print(f"Dein Charakter wurde erstellt!")
  return character

player = create_character()
# print(f"Mein Name ist {player['Name']}, dabei bin ich von der Klasse {player['Klasse']} und habe {player['Stärke']} Stärke")
#print(player["Name"])
print("\nDein Charakter:")
for key, value in player.items():
  print(f"{key}: {value}")

  import random

enemy_list = [
  {"Name": "👹 stinkender Ork", "Angriff": random.randint(5,15), "HP": random.randint(5,20)},
  {"Name": "🐍 windige Schlange", "Angriff": random.randint(5,15), "HP": random.randint(5,20)},
  {"Name": "🐗 runzeliges Warzenschwein", "Angriff": random.randint(5,15), "HP": random.randint(5,20)},
  {"Name": "🧌 winziger Goblin", "Angriff": random.randint(5,15), "HP": random.randint(5,20)}
   ]

def create_enemy():
  enemy = random.choice(enemy_list).copy()
  return enemy

enemy1 = create_enemy()
for key, value in enemy1.items():
  print(f"{key}: {value}")

  import random

def dice(sides):
  return random.randint(1,sides)

seiten = 8
print(dice(seiten))

def kampf(character, enemy):
  print(f"Du kämpfst gegen {enemy['Name']}")

  while character["HP"] > 0 and enemy["HP"] > 0:
    # charakter greift an
    input("Drücke ENTER zum würfelnss")
    schaden = dice(6)
    print(f"{character['Name']} würfelt: {schaden}")
    print(f"{enemy['Name']} nimmt {schaden} Schaden")

    enemy["HP"] -= schaden
    print(f"{enemy['Name']} hat nun {enemy['HP']} HP")

    # Überprüfen ob der Gegner besiegt wurde
    if enemy["HP"] <= 0:
      print("Du hast gewonnen")
      break

    schaden_gegner = dice(4)
    character["HP"] -= schaden_gegner
    print(f"Dein {character['Name']} hat nun {character['HP']} HP")
    print(f"{enemy['Name']} würfelt: {schaden}")
    print(f"{character['Name']} nimmt {schaden} Schaden")
    print("-------------------")

    if character["HP"] <= 0:
      print("Charakter wurde besiegt!")
      break
