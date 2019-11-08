from rasa_nlu.training_data  import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter




# def train_appointmentbot():
    # train_data = load_data('rasa_dataset.json')
    # trainer = Trainer(config.load("config_spacy.yaml"))
    # trainer.train(train_data)
    # model_dir=trainer.persist('./models/',fixed_model_name='appointmentbot')
    # interpreter = Interpreter.load(model_dir)
    # return interpreter
# interpreter = Interpreter.load(model_dir)

# To get the intent of sentence..

train_data = load_data('rasa_dataset.json')
trainer = Trainer(config.load("config_spacy.yaml"))
trainer.train(train_data)
model_dir=trainer.persist('./models/',fixed_model_name='appointmentbot')
interpreter = Interpreter.load(model_dir)


def getintent(text):
    # interpreter = Interpreter.load('./models/default/appointmentbot')
    # model_dir='./models/default/appointmentbot'
    intentname=interpreter.parse(text)
    print(intentname)
    return intentname['intent']['name']

# train_appointmentbot()

# print(getintent("Book an appointment with doctor vijay"))