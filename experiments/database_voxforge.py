#!/usr/bin/env python

from bob.db.voxforge import Database

voxforge_wav_directory = "./voxforge"

database = Database(original_directory = voxforge_wav_directory, original_extension = ".wav")
