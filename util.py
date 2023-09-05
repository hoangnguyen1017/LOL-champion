def isIDvalid(input):
    if input.isdigit():
        return input
    else:
        print("The ID format must be a number")

def isNamevalid(input):
    if input.isalpha():
        return input
    else:
        print("The Name format must be character")
def isRolevalid(input):
    if input.isalpha():
        return input
    else:
        print("The Role format must be character")
def isHealthvalid(input):
    if input.isdigit():
        return input
    else:
        print("The Heal format must be a number")
def isAttackvalid(input):
    if input.isdigit():
        return input
    else:
        print("The Attack format must be a number")
def isDefensevalid(input):
    if input.isdigit():
        return input
    else:
        print("The Defense format must be a number")
def isAttackSpeed(input):
    if ('.' in input):
        f, l = input.split('.')
        if f.isdigit() and l.isdigit():
            return input
    else:
        print("The Attack Speed format must be a decimal")

def isIdUserValid(input):
    if input.isdigit():
        return input
    else:
        print("The ID format must be a number")

def isNameUserValid(input):
    if input.isalpha():
        return input
    else:
        print("The Name format must be character")


def isNameloginAccountValid(input):
    if (' ' in input):
        f, l = input.split(" ", 1)
        if f.isalpha and l.isalpha():
            return input
    else:
        print("The Login account format must be First_name Surname")


def isPassValid(input):
    if len(input) > 10:
        return input
    else:
        print("The Password format must be greater than 10 characters")

def champion_outcome(champions):
    battle_result = []

    for champion1 in champions:
        for champion2 in champions:
            if champion1 != champion2:
                effective_damage_champ1 = (int(champion1.attack) * 3 - int(champion2.defense) * 2) * float(champion1.attackSpeed)
                hits_required_champ1 = int(champion2.health) / int(effective_damage_champ1)

                effective_damage_champ2 = (int(champion2.attack) * 3 - int(champion1.defense) * 2) * float(champion2.attackSpeed)
                hits_required_champ2 = int(champion1.health) / int(effective_damage_champ2)

                if int(hits_required_champ1) < int(hits_required_champ2):
                    winner = [champion1.name]
                else:
                    winner = [champion2.name]

                battle_result.append((champion1.name, champion2.name, winner))

    return battle_result

