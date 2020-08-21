import pynmea2

# file with nmea output
GPS_FILENAME = "out/nmea.txt"


def write_to_file(filename, data):
    try:
        with open(filename, "a") as f:
            f.write(str(data))
    except Exception as ex:
        print("Error writing data to file " + filename, ex)


def read_nmea(source):
    try:
        if source is not None:
            nmea_msg = pynmea2.parse(str(source))

            if nmea_msg.sentence_type == 'GGA':  # if message is a GPGGA, write it to the file
                print(nmea_msg)
                write_to_file(GPS_FILENAME,
                              str(nmea_msg.timestamp) + ";" + str(nmea_msg.lat) + ";"
                              + str(nmea_msg.latitude) + ";" + str(nmea_msg.lon) + ";"
                              + str(nmea_msg.longitude) + ";" + str(nmea_msg.num_sats) + ";" +
                              str(nmea_msg.horizontal_dil) + ";" + str(nmea_msg.altitude) + "\n")
            return ["coordinates", nmea_msg.timestamp, nmea_msg.latitude, nmea_msg.longitude]

    except Exception as ex:
        print("error in parse line: ", ex)
