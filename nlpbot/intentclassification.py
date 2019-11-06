from rasa_nlu.training_data  import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter



# for training the model..
train_data = load_data('rasa_dataset.json')
trainer = Trainer(config.load("config_spacy.yaml"))
trainer.train(train_data)


# To get the intent of sentence..
def getintent(text):
    model_directory = trainer.persist('./projects/')
    interpreter = Interpreter.load(model_directory)
    intentname=interpreter.parse(text)
    print(intentname)
    return intentname['intent']['name']