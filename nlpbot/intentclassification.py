from rasa_nlu.training_data  import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter


# ********training the model**********
def train_appointmentbot():
    train_data = load_data('rsafiles/rasa_dataset.json')
    trainer = Trainer(config.load("rsafiles/config_spacy.yaml"))
    trainer.train(train_data)
    model_dir=trainer.persist('./rsamodels/',fixed_model_name='appointmentbot')
# train_appointmentbot()
# *************************************



interpreter = Interpreter.load('./rsamodels/default/appointmentbot')
# print("hello")

def getintent(text):
    intentname=interpreter.parse(text)
    return intentname



