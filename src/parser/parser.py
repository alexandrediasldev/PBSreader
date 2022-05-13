from PBSclasses.Ability import AbilityV15
from PBSclasses.Encounter import (
    EncounterV15,
    EncounterPokemonV15,
    EncounterByMethodV15,
    EncounterV19,
)
from PBSclasses.Item import ItemV15, ItemV16
from PBSclasses.Move import MoveV15
from PBSclasses.PokemonForm import PokemonFormV17, PokemonFormV18, PokemonFormV19
from PBSclasses.RegionalDexes import RegionalDexV19
from PBSclasses.Ribbon import RibbonV19
from PBSclasses.Species import SpeciesV15, SpeciesV17, SpeciesV16, SpeciesV18, SpeciesV19
from PBSclasses.SpeciesEvolution import SpeciesEvolution
from PBSclasses.BerryPlant import BerryPlantV16
from PBSclasses.Connection import ConnectionV15
from PBSclasses.MetaData import MetaDataV15, PlayerMetaData, HomeMetaData, MetaDataV18
from PBSclasses.Phone import PhoneV15
from PBSclasses.ShadowPokemon import ShadowPokemonV15
from PBSclasses.SpeciesStats import SpeciesStats
from PBSclasses.Tm import TmV15

from PBSclasses.TownMap import TownMap, TownPoint
from PBSclasses.TrainerPokemon import TrainerPokemonV15
from PBSclasses.TrainerTypes import TrainerTypeV15, TrainerTypeV16
from PBSclasses.Trainers import TrainerV15
from PBSclasses.Type import TypeV15
from src.parser.parse_utils import parse_bracket_header, parse_one_line_coma, append_value_kwargs
from src.parser.schema import (
    separate_equal,
    separate_trainers,
    separate_encountersv15,
    separate_encountersv19,
)

# single line parsing
from src.parser.section import (
    parse_bracket_section_header,
    parse_one_line_coma_section_body,
    parse_equal_section_body,
    parse_all_section,
    parse_metadata_section_body,
    parse_townmap_section_body,
    parse_pokemon_section_body,
    parse_pokemon_form_section_header,
    parse_full_section_header,
    parse_encounter_map_section_headerv15,
    parse_encounter_map_section_bodyv15,
    parse_encounter_map_section_bodyv19,
    parse_bracket_coma_section_header,
    parse_encounter_map_section_headerv19,
)
from src.parser.single_line_files import (
    attr_list_to_object,
    attr_name_and_str_list_to_object,
    get_kwargs_from_line_csv,
    parse_csv,
    parse_csv_after_equal,
)


# ---- CSV


def parse_ability(csv_output) -> list[AbilityV15]:
    type = AbilityV15
    return parse_csv(csv_output, type)


def parse_move(csv_output) -> list[MoveV15]:
    type = MoveV15
    return parse_csv(csv_output, type)


def parse_berry_plant(csv_output) -> list[BerryPlantV16]:
    type = BerryPlantV16
    return parse_csv(csv_output, type)


def parse_connection(csv_output) -> list[ConnectionV15]:
    type = ConnectionV15
    return parse_csv(csv_output, type)


def parse_trainer_types(csv_output, version) -> list[TrainerTypeV15]:
    if version == 15:
        type = TrainerTypeV15
    else:
        type = TrainerTypeV16
    return parse_csv(csv_output, type)


def parse_item(csv_output, version) -> list[ItemV15]:
    if version == 15:
        itemType = ItemV15
    else:
        itemType = ItemV16
    return parse_csv(csv_output, itemType)


def parse_ribbon(csv_output, version) -> list[RibbonV19]:
    type = RibbonV19
    return parse_csv(csv_output, type)


def parse_shadow_pokemon(csv_output) -> list[ShadowPokemonV15]:
    type = ShadowPokemonV15
    return parse_csv_after_equal(csv_output, type)


def parse_tm(lines, version):
    type = TmV15
    lines_separated = separate_equal(lines)
    return parse_all_section(
        lines_separated, type, parse_bracket_section_header, parse_one_line_coma_section_body
    )


def parse_regional_dex(lines, version):
    type = RegionalDexV19
    lines_separated = separate_equal(lines)
    return parse_all_section(
        lines_separated, type, parse_bracket_section_header, parse_one_line_coma_section_body
    )


# ------ Equal


def parse_type(lines):
    type = TypeV15
    lines_separated = separate_equal(lines)
    return parse_all_section(
        lines_separated, type, parse_bracket_section_header, parse_equal_section_body
    )


def parse_townmap(lines):
    type = TownMap
    lines_separated = separate_equal(lines)
    return parse_all_section(
        lines_separated, type, parse_bracket_section_header, parse_townmap_section_body
    )


def parse_metadata(lines, version):
    if version <= 17:
        type = MetaDataV15
    else:
        type = MetaDataV18
    lines_separated = separate_equal(lines)
    return parse_all_section(
        lines_separated, type, parse_bracket_section_header, parse_metadata_section_body
    )


def parse_pokemon(lines, version):
    if version == 15:
        type = SpeciesV15
    elif version == 16:
        type = SpeciesV16
    elif version == 17:
        type = SpeciesV17
    elif version == 18:
        type = SpeciesV18
    else:
        type = SpeciesV19

    lines_separated = separate_equal(lines)
    return parse_all_section(
        lines_separated, type, parse_bracket_section_header, parse_pokemon_section_body
    )


def parse_pokemon_form(lines, version):
    if version == 17:
        type = PokemonFormV17
    elif version == 18:
        type = PokemonFormV18
    else:
        type = PokemonFormV19
    lines_separated = separate_equal(lines)
    return parse_all_section(
        lines_separated, type, parse_pokemon_form_section_header, parse_pokemon_section_body
    )


# Others


def parse_trainer_list(csv_output, version) -> list[TrainerV15]:
    def _parse_trainer_pokemon(pokemon_attributes) -> TrainerPokemonV15:
        attr_names = TrainerPokemonV15.get_attr_names()
        moves = pokemon_attributes[3:7]
        pokemon_attributes = pokemon_attributes[:3] + pokemon_attributes[7:]
        attr_names.remove("move_list")
        kwargs = parse_one_line_coma(attr_names, pokemon_attributes)
        kwargs["move_list"] = moves

        return TrainerPokemonV15(**kwargs)

    def parse_one_trainer(lines):
        coma_line = []
        coma_line.append(lines[0][0])
        coma_line.append(lines[1][0])
        coma_line.append(lines[1][1] if len(lines[1]) > 1 else "")
        coma_line.append(lines[2][1:])
        coma_line.append(lines[2][0])
        coma_line.append([_parse_trainer_pokemon(line) for line in lines[3:]])

        kwargs = parse_one_line_coma(TrainerV15.get_attr_names(), coma_line)

        return kwargs

    lines = separate_trainers(csv_output)
    obj_list = []
    for line in lines:
        obj_list.append(TrainerV15(**parse_one_trainer(line)))
    return obj_list


def parse_encounter(lines, version: int) -> list[EncounterV15]:
    if version == 15:
        type = EncounterV15
        lines_separated = separate_encountersv15(lines)
        return parse_all_section(
            lines_separated,
            type,
            parse_encounter_map_section_headerv15,
            parse_encounter_map_section_bodyv15,
        )
    else:
        type = EncounterV19
        lines_separated = separate_encountersv19(lines)
        return parse_all_section(
            lines_separated,
            type,
            parse_encounter_map_section_headerv19,
            parse_encounter_map_section_bodyv19,
        )


# ----- Phone
def parse_phone(csv_output):
    argument_translator = PhoneV15.get_attr_dict()
    kwargs = dict()
    lines_separated = separate_equal(csv_output)
    for line in lines_separated:
        section_name = parse_bracket_header(line[0][0])
        section_name = section_name.removesuffix(">")
        section_name = section_name.removeprefix("<")
        line_content = []
        for rest_of_the_line in line[1:]:
            line_content.append(rest_of_the_line[0])
        kwargs[argument_translator[section_name]] = line_content
    phone = PhoneV15(**kwargs)
    return phone
