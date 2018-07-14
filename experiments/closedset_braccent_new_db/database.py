import bob.db.braccent
wav_directory = "[PATH_UNTIL_BasedeDados]" # PATH UNTIL BasedeDados

database = bob.db.braccent.BraccentBioDatabase(original_directory=wav_directory,
                                               original_extension='.wav')


