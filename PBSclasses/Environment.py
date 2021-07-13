from typing import List
import Parser as pr
from PBSclasses.Ability import Ability
from PBSclasses.EncounterMethod import *
import Exception as ex

from PBSclasses.Encounter import Encounter
from PBSclasses.Item import Item
from PBSclasses.Move import Move
from PBSclasses.Species import Species
from PBSclasses.TrainerTypes import TrainerType
from PBSclasses.Trainers import Trainer


class Environment:
    trainer_type_list: List[TrainerType] = None
    species_list: List[Species] = None
    move_list: List[Move] = None
    item_list: List[Item] = None
    trainer_list: List[Trainer] = None
    encounter_list: List[Encounter] = None
    ability_list: List[Ability] = None

    def __init__(self):
        pass
    def load_ability_list(self,csv_ability):
        self.ability_list = pr.parse_ability(csv_ability)

    def load_trainer_type_list(self, csv_trainer_type):
        self.trainer_type_list = pr.parse_trainer_types(csv_trainer_type)

    def load_species_list(self, equal_pokemon_species):
        self.species_list = pr.parse_pokemon(equal_pokemon_species)

    def load_move_list(self, csv_move):
        self.move_list = pr.parser_move(csv_move)

    def load_item_list(self, csv_item):
        self.item_list = pr.parse_item(csv_item)

    def load_encounter_list(self, csv_encounter,
                          encounter_method_list=get_default_encounter_method_list()):
        if (self.species_list):
            self.encounter_list = pr.parse_encounter(csv_encounter, encounter_method_list, self)
        else:
            raise ex.EnvironmentLoadingException("Need to load species list before encounter list")

    def load_trainer_list(self, csv_trainer):
        if (not self.trainer_type_list):
            raise ex.EnvironmentLoadingException("Need to load trainer type list before trainer list")
        elif (not self.species_list):
            raise ex.EnvironmentLoadingException("Need to load species list before trainer list")
        elif (not self.move_list):
            raise ex.EnvironmentLoadingException("Need to load move list before trainer list")
        elif (not self.item_list):
            raise ex.EnvironmentLoadingException("Need to load item list before trainer list")
        else:
            self.trainer_list = pr.parse_trainer_list(csv_trainer, self)

    def load_environment(self, csv_trainer_type, equal_pokemon_species, csv_move, csv_item, csv_trainer, csv_encounter,
                        csv_ability,
                        encounter_method_list=get_default_encounter_method_list()):
        self.load_ability_list(csv_ability)
        self.load_trainer_type_list(csv_trainer_type)
        self.load_species_list(equal_pokemon_species)
        self.load_move_list(csv_move)
        self.load_item_list(csv_item)
        self.load_trainer_list(csv_trainer)
        self.load_encounter_list(csv_encounter, encounter_method_list)
