import pkg_resources
import bob.bio.base
from bob.bio.spear.database import AudioBioFile

wav_directory = "database_todos/"

database = bob.bio.base.database.FileListBioDatabase('protocolos/crossdataset_ynogutti_braccent/', 'protocolos',
                                                     bio_file_class=AudioBioFile,
                                                     protocol='crossdataset',
                                                     original_directory=wav_directory,
                                                     original_extension=".wav")

database.objects()
