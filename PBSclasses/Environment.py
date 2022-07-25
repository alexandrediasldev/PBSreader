from typing import List
from PBSclasses.Ability import AbilityV15
from PBSclasses.BerryPlant import BerryPlantV16
from PBSclasses.Tm import TmV15

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
from src.parser.parser import parse_tm


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
    tm_list: List[TmV15] = []
    phone: PhoneV15 = None

    def __init__(self):
        pass

    def load_metadata(self, equal_metadata, version):
        self.metadata_list = pr.parse_metadata(equal_metadata, version)

    def load_townmap(self, equal_townmap):
        self.townmap_list = pr.parse_townmap(equal_townmap)

    def load_type(self, equal_type, version):
        self.type_list = pr.parse_type(equal_type)

    def load_phone(self, csv_phone):
        self.phone = pr.parse_phone(csv_phone)

    def load_ability_list(self, csv_ability, version):
        self.ability_list = pr.parse_ability(csv_ability, version)

    def load_trainer_type_list(self, csv_trainer_type, version):
        self.trainer_type_list = pr.parse_trainer_types(csv_trainer_type, version)

    def load_species_list(self, equal_pokemon_species, version):
        self.species_list = pr.parse_pokemon(equal_pokemon_species, version)

    def load_move_list(self, csv_move, version):
        self.move_list = pr.parse_move(csv_move, version)

    def load_item_list(self, csv_item, version):
        self.item_list = pr.parse_item(csv_item, version)

    def load_connection_list(self, csv_connection):
        self.connection_list = pr.parse_connection(csv_connection)

    def load_encounter_list(self, csv_encounter, version):
        self.encounter_list = pr.parse_encounter(csv_encounter, version)

    def load_shadow_list(self, equal_pokemon_shadow, version):
        self.shadow_list = pr.parse_shadow_pokemon(equal_pokemon_shadow, version)

    def load_berry_plant_list(self, equal_berry_plant, version):
        self.berry_plant_list = pr.parse_berry_plant(equal_berry_plant, version)

    def load_trainer_list(self, csv_trainer, version):
        self.trainer_list = pr.parse_trainer_list(csv_trainer, version)

    def load_tm_list(self, equal_tm, version):
        self.tm_list = parse_tm(equal_tm, version)

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
        equal_tm,
        version,
    ):
        self.load_ability_list(csv_ability, version)
        self.load_trainer_type_list(csv_trainer_type, version)
        self.load_species_list(equal_pokemon_species, version)
        self.load_move_list(csv_move, version)
        self.load_item_list(csv_item, version)
        self.load_trainer_list(csv_trainer, version)
        self.load_encounter_list(csv_encounter, version)
        self.load_connection_list(csv_connection)
        self.load_shadow_list(equal_pokemon_shadow, version)
        self.load_berry_plant_list(equal_berry_plant, version)
        self.load_phone(csv_phone)
        self.load_type(equal_type, version)
        self.load_townmap(equal_townmap)
        self.load_metadata(equal_metadata, version)
        self.load_tm_list(equal_tm, version)
