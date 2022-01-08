from typing import List
from PBSclasses.Ability import Ability
from PBSclasses.BerryPlant import BerryPlant

from src import Exception as ex
from src.parser import parser as pr
from PBSclasses.Connection import Connection

from PBSclasses.Encounter import Encounter
from PBSclasses.EncounterMethod import get_default_encounter_method_list
from PBSclasses.Item import Item
from PBSclasses.MetaData import MetaData
from PBSclasses.Move import Move
from PBSclasses.Phone import Phone
from PBSclasses.ShadowPokemon import ShadowPokemon
from PBSclasses.Species import Species
from PBSclasses.TownMap import TownMap
from PBSclasses.TrainerTypes import TrainerType
from PBSclasses.Trainers import Trainer
from PBSclasses.Type import Type


class Environment:
    trainer_type_list: List[TrainerType] = []
    species_list: List[Species] = []
    move_list: List[Move] = []
    item_list: List[Item] = []
    trainer_list: List[Trainer] = []
    encounter_list: List[Encounter] = []
    ability_list: List[Ability] = []
    connection_list: List[Connection] = []
    shadow_list: List[ShadowPokemon] = []
    berry_plant_list: List[BerryPlant] = []
    type_list: List[Type] = []
    townmap_list: List[TownMap] = []
    metadata_list: List[MetaData] = []
    phone: Phone = None

    def __init__(self):
        pass

    def load_metadata(self, equal_metadata):
        self.metadata_list = pr.parse_metadata(equal_metadata)

    def load_townmap(self, equal_townmap):
        self.townmap_list = pr.parse_townmap(equal_townmap)

    def load_type(self, equal_type):
        self.type_list = pr.parse_type(equal_type)

    def load_phone(self, csv_phone):
        self.phone = pr.parse_phone(csv_phone)

    def load_ability_list(self, csv_ability):
        self.ability_list = pr.parse_ability(csv_ability)

    def load_trainer_type_list(self, csv_trainer_type):
        self.trainer_type_list = pr.parse_trainer_types(csv_trainer_type)

    def load_species_list(self, equal_pokemon_species):
        self.species_list = pr.parse_pokemon(equal_pokemon_species)

    def load_move_list(self, csv_move):
        self.move_list = pr.parser_move(csv_move)

    def load_item_list(self, csv_item):
        self.item_list = pr.parse_item(csv_item, 15)

    def load_connection_list(self, csv_connection):
        self.connection_list = pr.parse_connection(csv_connection)

    def load_encounter_list(
        self, csv_encounter, encounter_method_list=get_default_encounter_method_list()
    ):
        self.encounter_list = pr.parse_encounter(csv_encounter, encounter_method_list, self)

    def load_shadow_list(self, equal_pokemon_shadow):
        self.shadow_list = pr.parse_shadow_pokemon(equal_pokemon_shadow, self)

    def load_berry_plant_list(self, equal_berry_plant):
        self.berry_plant_list = pr.parse_berry_plant(equal_berry_plant)

    def load_trainer_list(self, csv_trainer):
        self.trainer_list = pr.parse_trainer_list(csv_trainer, self)

    def load_environment(
        self,
        csv_trainer_type,
        equal_pokemon_species,
        csv_move,
        csv_item,
        csv_trainer,
        csv_encounter,
        csv_ability,
        csv_connection,
        equal_pokemon_shadow,
        equal_berry_plant,
        csv_phone,
        equal_type,
        equal_townmap,
        equal_metadata,
        encounter_method_list=get_default_encounter_method_list(),
    ):
        self.load_ability_list(csv_ability)
        self.load_trainer_type_list(csv_trainer_type)
        self.load_species_list(equal_pokemon_species)
        self.load_move_list(csv_move)
        self.load_item_list(csv_item)
        self.load_trainer_list(csv_trainer)
        self.load_encounter_list(csv_encounter, encounter_method_list)
        self.load_connection_list(csv_connection)
        self.load_shadow_list(equal_pokemon_shadow)
        self.load_berry_plant_list(equal_berry_plant)
        self.load_phone(csv_phone)
        self.load_type(equal_type)
        self.load_townmap(equal_townmap)
        self.load_metadata(equal_metadata)
