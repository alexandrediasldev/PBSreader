from PBSclasses.Ability import AbilityV15, AbilityV20
from PBSclasses.Encounter import (
    EncounterV15,
    EncounterPokemonV15,
    EncounterByMethodV15,
    EncounterV19,
)
from PBSclasses.Item import ItemV15, ItemV16, ItemV20
from PBSclasses.MapMetaData import MapMetaDataV20
from PBSclasses.Move import MoveV15, MoveV20
from PBSclasses.PokemonForm import PokemonFormV17, PokemonFormV18, PokemonFormV19, PokemonFormV20
from PBSclasses.PokemonMetric import PokemonMetricV20
from PBSclasses.RegionalDexes import RegionalDexV19
from PBSclasses.Ribbon import RibbonV19, RibbonV20
from PBSclasses.Species import (
    SpeciesV15,
    SpeciesV17,
    SpeciesV16,
    SpeciesV18,
    SpeciesV19,
    SpeciesV20,
)
from PBSclasses.SpeciesEvolution import SpeciesEvolution
from PBSclasses.BerryPlant import BerryPlantV16, BerryPlantV20
from PBSclasses.Connection import ConnectionV15
from PBSclasses.MetaData import (
    MetaDataV15,
    PlayerMetaDataV15,
    HomeMetaData,
    MetaDataV18,
    MetaDataV20,
)
from PBSclasses.Phone import PhoneV15
from PBSclasses.ShadowPokemon import ShadowPokemonV15, ShadowPokemonV20
from PBSclasses.SpeciesStats import SpeciesStats
from PBSclasses.Tm import TmV15

from PBSclasses.TownMap import TownMap, TownPoint
from PBSclasses.TrainerPokemon import TrainerPokemonV15
from PBSclasses.TrainerTypes import TrainerTypeV15, TrainerTypeV16, TrainerTypeV20
from PBSclasses.Trainers import TrainerV15, TrainerV18, TrainerV20
from PBSclasses.Type import TypeV15, TypeV20
from src.Exception import UnsupportedVersionError
from src.parser.parse_utils import parse_bracket_header, parse_one_line_coma, append_value_kwargs
from src.parser.schema import (
    separate_equal,
    separate_trainersv15,
    separate_encountersv15,
    separate_encountersv19,
    separate_trainersv18,
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
    parse_trainer_section_bodyv18,
    parse_trainer_section_headerv18,
    parse_trainer_section_bodyv15,
    parse_trainer_section_headerv15,
    parse_berry_plant_section_bodyv20,
    parse_trainer_section_bodyv20,
)
from src.parser.single_line_files import (
    attr_list_to_object,
    attr_name_and_str_list_to_object,
    get_kwargs_from_line_csv,
    parse_csv,
    parse_csv_after_equal,
)


def check_if_version_is_supported(value, min=15, max=20):
    if value < min or value > max:
        raise UnsupportedVersionError(
            f"{value} is not a supported version, it must be between {min} and {max}"
        )


# ---- CSV


def parse_ability(csv_output, version) -> list[AbilityV15]:
    check_if_version_is_supported(version)
    if version >= 15 and version <= 19:
        type = AbilityV15
        return parse_csv(csv_output, type)
    else:
        type = AbilityV20
        lines_separated = separate_equal(csv_output)
        return parse_all_section(
            lines_separated, type, parse_bracket_section_header, parse_equal_section_body
        )


def parse_move(csv_output, version) -> list[MoveV15]:
    check_if_version_is_supported(version)
    if version >= 15 and version <= 19:
        type = MoveV15
        return parse_csv(csv_output, type)
    else:
        type = MoveV20
        lines_separated = separate_equal(csv_output)
        return parse_all_section(
            lines_separated, type, parse_bracket_section_header, parse_equal_section_body
        )


def parse_berry_plant(csv_output, version) -> list[BerryPlantV16]:
    check_if_version_is_supported(version, min=16)
    if version >= 16 and version <= 19:
        type = BerryPlantV16
        return parse_csv(csv_output, type)
    else:
        type = BerryPlantV20
        lines_separated = separate_equal(csv_output)
        return parse_all_section(
            lines_separated, type, parse_bracket_section_header, parse_berry_plant_section_bodyv20
        )


def parse_connection(csv_output, version) -> list[ConnectionV15]:
    check_if_version_is_supported(version)
    type = ConnectionV15
    return parse_csv(csv_output, type)


def parse_trainer_types(csv_output, version) -> list[TrainerTypeV15]:
    check_if_version_is_supported(version)
    if version == 15:
        type = TrainerTypeV15
        return parse_csv(csv_output, type)
    elif version >= 16 and version <= 19:
        type = TrainerTypeV16
        return parse_csv(csv_output, type)
    else:
        type = TrainerTypeV20
        lines_separated = separate_equal(csv_output)
        return parse_all_section(
            lines_separated, type, parse_bracket_section_header, parse_equal_section_body
        )


def parse_item(csv_output, version) -> list[ItemV15]:
    check_if_version_is_supported(version)
    if version == 15:
        itemType = ItemV15
        return parse_csv(csv_output, itemType)
    elif version >= 16 and version <= 19:
        itemType = ItemV16
        return parse_csv(csv_output, itemType)
    else:
        type = ItemV20
        lines_separated = separate_equal(csv_output)
        return parse_all_section(
            lines_separated, type, parse_bracket_section_header, parse_equal_section_body
        )


def parse_ribbon(csv_output, version) -> list[RibbonV19]:
    check_if_version_is_supported(version, min=19)
    if version == 19:
        type = RibbonV19
        return parse_csv(csv_output, type)
    else:
        type = RibbonV20
        lines_separated = separate_equal(csv_output)
        return parse_all_section(
            lines_separated, type, parse_bracket_section_header, parse_equal_section_body
        )


def parse_shadow_pokemon(csv_output, version) -> list[ShadowPokemonV15]:
    check_if_version_is_supported(version)
    if version >= 15 and version <= 19:
        type = ShadowPokemonV15
        return parse_csv_after_equal(csv_output, type)
    else:
        type = ShadowPokemonV20
        lines_separated = separate_equal(csv_output)
        return parse_all_section(
            lines_separated, type, parse_bracket_section_header, parse_equal_section_body
        )


def parse_tm(lines, version):
    check_if_version_is_supported(version, max=18)
    type = TmV15
    lines_separated = separate_equal(lines)
    return parse_all_section(
        lines_separated, type, parse_bracket_section_header, parse_one_line_coma_section_body
    )


def parse_regional_dex(lines, version):
    check_if_version_is_supported(version, min=19)
    type = RegionalDexV19
    lines_separated = separate_equal(lines)
    return parse_all_section(
        lines_separated, type, parse_bracket_section_header, parse_one_line_coma_section_body
    )


# ------ Equal


def parse_type(lines, version):
    check_if_version_is_supported(version)
    if version >= 15 and version <= 19:
        type = TypeV15
    else:
        type = TypeV20
    lines_separated = separate_equal(lines)
    return parse_all_section(
        lines_separated, type, parse_bracket_section_header, parse_equal_section_body
    )


def parse_townmap(lines, version):
    check_if_version_is_supported(version)
    type = TownMap
    lines_separated = separate_equal(lines)
    return parse_all_section(
        lines_separated, type, parse_bracket_section_header, parse_townmap_section_body
    )


def parse_metadata(lines, version):
    check_if_version_is_supported(version)
    if version >= 15 and version <= 17:
        type = MetaDataV15
    elif version >= 18 and version <= 19:
        type = MetaDataV18
    else:
        type = MetaDataV20
    lines_separated = separate_equal(lines)
    return parse_all_section(
        lines_separated, type, parse_bracket_section_header, parse_metadata_section_body
    )


def parse_map_metadata(lines, version):
    check_if_version_is_supported(version, min=20)
    if version == 20:
        type = MapMetaDataV20
    lines_separated = separate_equal(lines)
    return parse_all_section(
        lines_separated, type, parse_bracket_section_header, parse_metadata_section_body
    )


def parse_pokemon(lines, version):
    check_if_version_is_supported(version)
    if version == 15:
        type = SpeciesV15
    elif version == 16:
        type = SpeciesV16
    elif version == 17:
        type = SpeciesV17
    elif version == 18:
        type = SpeciesV18
    elif version == 19:
        type = SpeciesV19
    else:
        type = SpeciesV20

    lines_separated = separate_equal(lines)
    return parse_all_section(
        lines_separated, type, parse_bracket_section_header, parse_pokemon_section_body
    )


def parse_pokemon_form(lines, version):
    check_if_version_is_supported(version, min=17)
    if version == 17:
        type = PokemonFormV17
    elif version == 18:
        type = PokemonFormV18
    elif version == 19:
        type = PokemonFormV19
    else:
        type = PokemonFormV20

    lines_separated = separate_equal(lines)
    return parse_all_section(
        lines_separated, type, parse_pokemon_form_section_header, parse_pokemon_section_body
    )


def parse_pokemon_metric(lines, version):
    check_if_version_is_supported(version, min=20)
    if version == 20:
        type = PokemonMetricV20

    lines_separated = separate_equal(lines)
    return parse_all_section(
        lines_separated, type, parse_pokemon_form_section_header, parse_equal_section_body
    )


# Others


def parse_trainer_list(csv_output, version) -> list[TrainerV15]:
    check_if_version_is_supported(version)
    if version >= 15 and version <= 17:
        type = TrainerV15
        lines = separate_trainersv15(csv_output)
        return parse_all_section(
            lines, type, parse_trainer_section_headerv15, parse_trainer_section_bodyv15
        )
    elif version >= 18 and version <= 19:
        type = TrainerV18

        lines_separated = separate_trainersv18(csv_output)
        return parse_all_section(
            lines_separated, type, parse_trainer_section_headerv18, parse_trainer_section_bodyv18
        )
    else:
        type = TrainerV20

        lines_separated = separate_trainersv18(csv_output)
        return parse_all_section(
            lines_separated, type, parse_trainer_section_headerv18, parse_trainer_section_bodyv20
        )


def parse_encounter(lines, version: int) -> list[EncounterV15]:
    check_if_version_is_supported(version)
    if version >= 15 and version <= 18:
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
def parse_phone(csv_output, version):
    check_if_version_is_supported(version)
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
