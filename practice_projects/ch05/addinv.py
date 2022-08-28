# 演習プロジェクト 5.6.3

from inventory import display_inventory

def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1

inv = {'金貨': 42, 'ロープ': 1}
dragon_loot = ['金貨', '手裏剣', '金貨', '金貨', 'ルビー']
add_to_inventory(inv, dragon_loot)
display_inventory(inv)
