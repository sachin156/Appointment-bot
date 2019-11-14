from rasa_nlu.training_data  import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter

# from bot.services.appointmentservice import AppService
# from bot.services.slotsservice import SlotService
# from bot.services.docservice import DocService



# ********training the model**********
# train_data = load_data('rasa_dataset.json')
# trainer = Trainer(config.load("config_spacy.yaml"))
# trainer.train(train_data)
# model_dir=trainer.persist('./models/',fixed_model_name='appointmentbot')
# interpreter = Interpreter.load(model_dir)
# train_appointmentbot()
# *************************************



interpreter = Interpreter.load('./models/default/appointmentbot')
# print("hello")

def getintent(text):
    intentname=interpreter.parse(text)
    return intentname['intent']['name']

