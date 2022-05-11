from typing import List
from PBSclasses.Ability import AbilityV15
from PBSclasses.BerryPlant import BerryPlantV16

from src import Exception as ex
from src.parser import parser as pr
from PBSclasses.Connection import ConnectionV15

from PBSclasses.Encounter import EncounterV15
from PBSclasses.EncounterMethod import get_default_encounter_method_list
from PBSclasses.Item import ItemV15
from PBSclasses.MetaData import MetaDataV15
from PBSclasses.Move import MoveV15
from PBSclasses.Phone import PhoneV15
from PBSclasses.ShadowPokemon import ShadowPokemonV15
from PBSclasses.Species import SpeciesV15
from PBSclasses.TownMap import TownMap
from PBSclasses.TrainerTypes import TrainerTypeV15
from PBSclasses.Trainers import TrainerV15
from PBSclasses.Type import TypeV15


class Environment:
    trainer_type_list: List[TrainerTypeV15] = []
    species_list: List[SpeciesV15] = []
    move_list: List[MoveV15] = []
    item_list: List[ItemV15] = []
    trainer_list: List[TrainerV15] = []
    encounter_list: List[EncounterV15] = []
    ability_list: List[AbilityV15] = []
    connection_list: List[ConnectionV15] = []
    shadow_list: List[ShadowPokemonV15] = []
    berry_plant_list: List[BerryPlantV16] = []
    type_list: List[TypeV15] = []
    townmap_list: List[TownMap] = []
    metadata_list: List[MetaDataV15] = []
    phone: PhoneV15 = None

    def __init__(self):
        pass

    def load_metadata(self, equal_metadata, version):
        self.metadata_list = pr.parse_metadata(equal_metadata, version)

    def load_townmap(self, equal_townmap):
        self.townmap_list = pr.parse_townmap(equal_townmap)

    def load_type(self, equal_type):
        self.type_list = pr.parse_type(equal_type)

    def load_phone(self, csv_phone):
        self.phone = pr.parse_phone(csv_phone)

    def load_ability_list(self, csv_ability):
        self.ability_list = pr.parse_ability(csv_ability)

    def load_trainer_type_list(self, csv_trainer_type, version):
        self.trainer_type_list = pr.parse_trainer_types(csv_trainer_type, version)

    def load_species_list(self, equal_pokemon_species, version):
        self.species_list = pr.parse_pokemon(equal_pokemon_species, version)

    def load_move_list(self, csv_move):
        self.move_list = pr.parse_move(csv_move)

    def load_item_list(self, csv_item, version):
        self.item_list = pr.parse_item(csv_item, version)

    def load_connection_list(self, csv_connection):
        self.connection_list = pr.parse_connection(csv_connection)

    def load_encounter_list(
        self, csv_encounter, encounter_method_list=get_default_encounter_method_list()
    ):
        self.encounter_list = pr.parse_encounter(csv_encounter, encounter_method_list)

    def load_shadow_list(self, equal_pokemon_shadow):
        self.shadow_list = pr.parse_shadow_pokemon(equal_pokemon_shadow)

    def load_berry_plant_list(self, equal_berry_plant):
        self.berry_plant_list = pr.parse_berry_plant(equal_berry_plant)

    def load_trainer_list(self, csv_trainer, version):
        self.trainer_list = pr.parse_trainer_list(csv_trainer, version)

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
        version,
        encounter_method_list=get_default_encounter_method_list(),
    ):
        self.load_ability_list(csv_ability)
        self.load_trainer_type_list(csv_trainer_type, version)
        self.load_species_list(equal_pokemon_species, version)
        self.load_move_list(csv_move)
        self.load_item_list(csv_item, version)
        self.load_trainer_list(csv_trainer, version)
        self.load_encounter_list(csv_encounter, encounter_method_list)
        self.load_connection_list(csv_connection)
        self.load_shadow_list(equal_pokemon_shadow)
        self.load_berry_plant_list(equal_berry_plant)
        self.load_phone(csv_phone)
        self.load_type(equal_type)
        self.load_townmap(equal_townmap)
        self.load_metadata(equal_metadata, version)
