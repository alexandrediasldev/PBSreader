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
    trainerTypeList: List[TrainerType] = None
    speciesList: List[Species] = None
    moveList: List[Move] = None
    itemList: List[Item] = None
    trainerList: List[Trainer] = None
    encounterList: List[Encounter] = None
    abilityList: List[Ability] = None

    def __init__(self):
        pass
    def loadAbilityList(self,csvAbility):
        self.abilityList = pr.parseAbility(csvAbility)

    def loadTrainerTypeList(self, csvTrainerType):
        self.trainerTypeList = pr.parseTrainerTypes(csvTrainerType)

    def loadSpeciesList(self, equalPokemonSpecies):
        self.speciesList = pr.parsePokemon(equalPokemonSpecies)

    def loadMoveList(self, csvMove):
        self.moveList = pr.parserMove(csvMove)

    def loadItemList(self, csvItem):
        self.itemList = pr.parseItem(csvItem)

    def loadEncounterList(self, csvEncounter,
                          encounterMethodList=getDefaultEncounterMethodList()):
        if (self.speciesList):
            self.encounterList = pr.parseEncounter(csvEncounter, encounterMethodList, self)
        else:
            raise ex.EnvironmentLoadingException("Need to load species list before encounter list")

    def loadTrainerList(self, csvTrainer):
        if (not self.trainerTypeList):
            raise ex.EnvironmentLoadingException("Need to load trainer type list before trainer list")
        elif (not self.speciesList):
            raise ex.EnvironmentLoadingException("Need to load species list before trainer list")
        elif (not self.moveList):
            raise ex.EnvironmentLoadingException("Need to load move list before trainer list")
        elif (not self.itemList):
            raise ex.EnvironmentLoadingException("Need to load item list before trainer list")
        else:
            self.trainerList = pr.parseTrainerList(csvTrainer, self)

    def loadEnvironment(self, csvTrainerType, equalPokemonSpecies, csvMove, csvItem, csvTrainer, csvEncounter,
                        csvAbility,
                        encounterMethodList=getDefaultEncounterMethodList()):
        self.loadAbilityList(csvAbility)
        self.loadTrainerTypeList(csvTrainerType)
        self.loadSpeciesList(equalPokemonSpecies)
        self.loadMoveList(csvMove)
        self.loadItemList(csvItem)
        self.loadTrainerList(csvTrainer)
        self.loadEncounterList(csvEncounter, encounterMethodList)
