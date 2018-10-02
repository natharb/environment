#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#Nathália Alves Rocha Batista (nathbapt@decom.fee.unicamp.br)

import pkg_resources
import bob.bio.base
from bob.bio.spear.database import AudioBioFile

wav_directory = "../baseDeDados/"

database = bob.bio.base.database.FileListBioDatabase('protocolos/all_dataset/', 'protocolos',
                                                     bio_file_class=AudioBioFile,
                                                     protocol='fold_7',
                                                     original_directory=wav_directory,
                                                     original_extension=".wav")

database.objects()
