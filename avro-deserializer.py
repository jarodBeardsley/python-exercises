import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
import sys

# The schema is embedded in the data file
reader = DataFileReader(open(sys.argv[0], "rb"), DatumReader())
reader.close()
