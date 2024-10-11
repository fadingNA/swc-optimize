from django.db import models

# Mappings for stat and set IDs
STAT_TYPE_CHOICES = {
    1: 'HP flat',
    2: 'HP%',
    3: 'ATK flat',
    4: 'ATK%',
    5: 'DEF flat',
    6: 'DEF%',
    7: 'SPD',
    8: 'CRI Rate%',
    9: 'CRI Dmg%',
    10: 'RES%',
    11: 'ACC%',
}

RUNE_SET_CHOICES = {
    1: 'Energy',
    2: 'Guard',
    3: 'Swift',
    4: 'Blade',
    5: 'Rage',
    6: 'Focus',
    7: 'Endure',
    8: 'Fatal',
    10: 'Despair',
    11: 'Vampire',
    13: 'Violent',
    14: 'Nemesis',
    15: 'Will',
    16: 'Shield',
    17: 'Revenge',
    18: 'Destroy',
    19: 'Fight',
    20: 'Determination',
    21: 'Enhance',
    22: 'Accuracy',
    23: 'Tolerance',
}

class Rune(models.Model):
    rune_id = models.BigIntegerField(primary_key=True)
    wizard_id = models.BigIntegerField()
    occupied_type = models.IntegerField()
    occupied_id = models.BigIntegerField()
    slot_no = models.IntegerField()
    rank = models.IntegerField()
    rune_class = models.IntegerField()
    set_id = models.IntegerField()
    upgrade_limit = models.IntegerField()
    upgrade_curr = models.IntegerField()
    base_value = models.IntegerField()
    sell_value = models.IntegerField()
    pri_eff = models.JSONField()
    prefix_eff = models.JSONField()
    sec_eff = models.JSONField()
    extra = models.IntegerField()

    def __str__(self):
        return f"Rune {self.rune_id} Slot {self.slot_no}"

    def get_primary_effect(self):
        stat_id, value = self.pri_eff
        stat_name = STAT_TYPE_CHOICES.get(stat_id, 'Unknown')
        return f"{stat_name} +{value}"

    def get_set_name(self):
        return RUNE_SET_CHOICES.get(self.set_id, 'Unknown')

    def get_secondary_effects(self):
        effects = []
        for eff in self.sec_eff:
            stat_id, value, _, _ = eff
            stat_name = STAT_TYPE_CHOICES.get(stat_id, 'Unknown')
            effects.append(f"{stat_name} +{value}")
        return effects