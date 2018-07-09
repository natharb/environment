import pkg_resources
import bob.bio.base
from bob.bio.spear.database import AudioBioFile

wav_directory = "database_todos/"

database = bob.bio.base.database.FileListBioDatabase('protocolos/closedset_ynogutti/', 'protocolos',
                                                     bio_file_class=AudioBioFile,
                                                     protocol='fold_10',
                                                     original_directory=wav_directory,
                                                     original_extension=".wav")

database.objects()