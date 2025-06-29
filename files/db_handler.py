from app.config.logger_config import detection_logger   

def refresh_characterization_database(row):  # metodo que actualiza una fila de la base de hechos
    characterization_database = open("files/characterization_database.txt", "r+")
    lines = characterization_database.readlines()
    for index, l in enumerate(lines):
        if l[:-2] == row[:-1] and l[-2] != row[-1]:
            l = l[:-2]
            l += row[-1] + "\n"
            lines[index] = l
            characterization_database.seek(0)
            characterization_database.writelines(lines)
            detection_logger.info("Updated row to database")
            characterization_database.close()
            return True
        elif l[:-2] == row[:-1] and l[-2] == row[-1]:
            detection_logger.info("Data already exist")
            return True
    characterization_database.close()
    return False


def add_row(row):  # metodo que anade una fila a la base de hechos
    characterization_database = open("files/characterization_database.txt", "a")
    characterization_database.write(row + "\n")
    characterization_database.close()


def save_data_characterization(metrics_characterization):  # metodo para salvar la caracterizacion del cojunto de datos en la base de hechos
    row = ""
    for i in metrics_characterization:
        row += str(i) + ","
    row = row[:-1]
    detection_logger.info(row)
    try:
        if not refresh_characterization_database(row):
            add_row(row)
            detection_logger.info("Added row to database")
    except:
        detection_logger.info("Data base is created")
        add_row(row)
        detection_logger.info("Added row to database")