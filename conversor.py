from pickle import TRUE

print("\n*******************************************")
print("**************Badge Mexican****************")
print("*******************************************\n")

iso = {"EUR": 20.81, "USD": 20.39, "JPY": 0.15, "RUB": 0.34, "CNY": 3.02}
catalog = list(iso.keys())
print("-------------options of badge--------------\n")
print(catalog, "\n")
badge = input("\nwhat badge coding iso selected: ").upper()

total = int(input("\nwhat cash conversion: "))


def searchBadge(badge, listIso):
    for i in listIso:
        if (i == badge):
            return True
    return False


def changeBadge(iso, badge, total):
    validation = searchBadge(badge, iso)
    if (validation == True):
        value = iso.get(badge)
        operation = value * int(total)
        print("\ntotal of conversion", operation, badge)
    else:
        print("\nincorrect iso coding")


changeBadge(iso, badge, total)
