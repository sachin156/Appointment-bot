from rasa_nlu.training_data  import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter


train_data = load_data('rasa_dataset.json')
trainer = Trainer(config.load("config_spacy.yaml"))
trainer.train(train_data)
model_directory = trainer.persist('./projects/')
interpreter = Interpreter.load(model_directory)


# To get the intent of sentence..

def getintent(text):
    intentname=interpreter.parse(text)
    print(intentname)
    return intentname['intent']['name']



# from rasa_nlu.training_data  import load_data
# from rasa_nlu.config import RasaNLUModelConfig
# from rasa_nlu.model import Trainer
# from rasa_nlu import config
# from rasa_nlu.model import Metadata, Interpreter
# import sys

# train_data = load_data('rasa_dataset.json')
# trainer = Trainer(config.load("config_spacy.yaml"))
# trainer.train(train_data)
# model_directory = trainer.persist('./projects/')
# interpreter = Interpreter.load(model_directory)



# def getintent(text):
# 	intentname=interpreter.parse(text)
# 	return intentname['intent']['name']
# print(getintent("Book an appointment"))