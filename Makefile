##### FETCHING THE DATA #####
stage_books:
	python fetch_data/stage_books.py

process_books:
	python fetch_data/process_books.py



##### CLEANING THE DATA #####
preprocess_gru:
	python -c 'from package.interface.main import preprocess_gru; preprocess_gru()'

# preprocess_bert:


##### COMPILE THE MODELS #####
compile_gru:
	python -c 'from package.interface.main import compile_gru; compile_gru()'

# compile_bert:


##### TRAIN THE MODELS #####
train_gru:
	python -c 'from package.interface.main import train_gru; train_gru()'

# train_bert:


##### PREDICT RESULTS #####



##### RUN PREPROCESSING + COMPILING + TRAINING
run_all: preprocess_gru compile_gru train_gru


##### RUN THE API #####
run_api:
	uvicorn package.api.fast:app --port 8002 --reload

#################### PACKAGE ACTIONS ###################
reinstall_package:
	 @pip uninstall -y package || :
	 @pip install -e .
