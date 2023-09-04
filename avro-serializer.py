import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
import sys

# Need to know the schema to write. According to 1.8.2 of Apache Avro
avsc = sys.argv[1]
schema = avro.schema.parse(open(avsc, "rb").read())

av = sys.argv[0]
writer = DataFileWriter(open(ac, "wb"), DatumWriter(), schema)
writer.close()
