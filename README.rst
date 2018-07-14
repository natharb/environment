==============
Manola project
==============


After everything installed do::

 $ git clone git@github.com:natharb/environment
 $ cd environment
 $ conda env create -f environment.yml
 $ source activate bob.accent  # activate the environment
 $ buildout

Hey, so far I've created only the closedset_braccent_foldN protocols.
It's straght forward to extend this to other datasets, since you organized the files in a very nice way (really now it's super clean).
Follow the new set of instructions to run the verify.py ::

 $ cd environment
 $ git pull origin master
 $ # your database will be cloned in ./src/bob.db.braccent
 $ ./bin/bob_dbmanage.py braccent create --files-dir [PATH_TO]/BasedeDados/ -r -vv 
 $ # This is suppose to work
 $ ./bin/nosetests -sv bob.db.braccent
 $ # This is the most important step. TEST UNITS. Look at ./src/bob.db.braccent/bob/db/braccent/test.py I take this very seriouslly
 $ # Check ./experiments/closedset_braccent_new_db/ to see how you'll trigger the thing.
 
 

.. note::
 
   Since now you are developing `bob.bio.base`, `bob.bio.spear`, etc you should ALWAYS use the `verify.py` from `./bin`, like ::
    
     $ ./bin/verify.py --help

