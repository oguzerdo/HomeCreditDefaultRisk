import gc
import time
from contextlib import contextmanager
import warnings


from scripts.helper_functions import get_namespace, i_love_ds, label_encoder

label_encoder

from scripts.pre_processing import application_train_test, bureau_and_balance, previous_applications, pos_cash, \
    installments_payments, credit_card_balance

from scripts.train import kfold_lightgbm

warnings.simplefilter(action='ignore', category=FutureWarning)