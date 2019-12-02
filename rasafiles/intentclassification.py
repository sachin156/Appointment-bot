from rasa_nlu.training_data  import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter

# from bot.services.appointmentservice import AppService
# from bot.services.slotsservice import SlotService
# from bot.services.docservice import DocService



# ********training the model**********
def train_appointmentbot():
    train_data = load_data('rasafiles/rasa_dataset.json')
    trainer = Trainer(config.load("rasafiles/config_spacy.yaml"))
    trainer.train(train_data)
    trainer.persist('./rasamodels/',fixed_model_name='appointmentbot')
# train_appointmentbot()
# *************************************



interpreter = Interpreter.load('./rasamodels/default/appointmentbot')
# print("hello")

def getintent(text):
    intentname=interpreter.parse(text)
    return intentname



