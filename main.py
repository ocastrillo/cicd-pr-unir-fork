"""
License: Apache
Organization: UNIR
"""

import os
import sys
import logging

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False
logging.basicConfig(filename="removing_duplicates.log", level=logging.INFO)


def sort_list(items, ascending=True):
    """Sort a list of items in ascending or descending order."""
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")
    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    """Remove duplicates from a list."""
    return list(set(items))


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
    else:
        logging.info("Se debe indicar el fichero como primer argumento")
        logging.info("El segundo argumento indica si se quieren eliminar duplicados")
        sys.exit(1)

    logging.info(f"Se leerán las palabras del fichero {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        logging.info(f"El fichero {filename} no existe")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]


    logging.info('Lista original: ')
    logging.info(word_list)

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)
        logging.info('Lista ordenada luego de eliminar duplicados: ')
        logging.info(sort_list(word_list))
    else:
        logging.info('Lista ordenanda sin eliminar duplicados: ')
        logging.info(sort_list(word_list))
