EXP_NAME = "ImageNet100"

IMAGE_SIZE = 168
NUM_FEATURES = 3 * IMAGE_SIZE * IMAGE_SIZE
NUM_CLASSES = 100
NUM_TRAIN_DATA = 126100
NUM_TEST_DATA = 5000

NUM_CLIENTS = 10
NUM_LOCAL_UPDATES = 5
CLIENT_BATCH_SIZE = 20
INIT_LR = 0.05
MOMENTUM = 0
WEIGHT_DECAY = 0

EVAL_DISP_INTERVAL = 10
ADJ_INTERVAL = 50
SAVE_INTERVAL = 50

IP_MAX_ROUNDS = 1000
IP_ADJ_INTERVAL = ADJ_INTERVAL
IP_DATA_BATCH = 25
IP_THR = 0.1

DENSE_TIME = 25.3356386726
SPARSE_ALL_TIME = 27.966371
SPARSE1_TIME = 14.560097051459854
COEFFICIENTS_SINGLE = [0.0, 2.340521716080689e-06, 1.0023681746470196e-05, 1.056062089141079e-05, 4.237937059382076e-06,
                       5.6712687899939165e-06, 2.1231460738533592e-06, 2.3287953360690104e-06, 6.735456426708777e-07,
                       6.624979740735464e-06, 5.137498356286562e-07, 1.9743886037025985e-07, 3.703237561077147e-08,
                       9.910993133200227e-07, 1.4966532573161931e-06, 7.477319510700925e-07, 8.722523120339614e-07,
                       6.128180224224039e-06]

SPARSE_TIME = SPARSE1_TIME - sum(COEFFICIENTS_SINGLE)

COMP_COEFFICIENTS = [c * NUM_LOCAL_UPDATES for c in COEFFICIENTS_SINGLE]
# 1MBps = 4e-6 * 2
COMM_COEFFICIENT = 5.561621025626998e-06
TIME_CONSTANT = SPARSE_TIME * NUM_LOCAL_UPDATES

ADJ_THR_FACTOR = 1.5
ADJ_THR_ACC = ADJ_THR_FACTOR / NUM_CLASSES

# Variables
MAX_INC_DIFF = None
MAX_DEC_DIFF = 0.3

LR_HALF_LIFE = 10000
STEP_SIZE = 1000
ADJ_HALF_LIFE = 10000

MAX_ROUND = 20001

# Iterative pruning config
NUM_ITERATIVE_PRUNING = 20

# Online algorithm config
MAX_NUM_UPLOAD = 5
