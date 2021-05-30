from Parser import *
import FileLoader





if __name__ == '__main__':

    csvTrainer = FileLoader.FileCsvTolist('PBS/trainers.txt')
    csvTrainerType = FileLoader.FileCsvTolist('PBS/trainertypes.txt')
    csvMove = FileLoader.FileCsvTolist('PBS/moves.txt')
    csvItem = FileLoader.FileCsvTolist('PBS/items.txt')
    equalPokemonSpecies = FileLoader.FileEqualToList('PBS/pokemon.txt')

    trainerTypeList = parseTrainerTypes(csvTrainerType)
    speciesList = parsePokemon(equalPokemonSpecies)
    moveList = parserMove(csvMove)
    itemList = parseItem(csvItem)
    trainerList = parseTrainerList(csvTrainer, trainerTypeList, speciesList, moveList, itemList)

    # for s in trainerList:
    #    print(s.toTrainerEntryBulbapedia())
    #for m in moveList:
    #    m.print()

