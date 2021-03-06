import pytest
from config import load_parameters


def test_load_params():
    params = load_parameters()
    assert isinstance(params, dict)


def test_params_exist():
    params = load_parameters()
    assert 'DATASET_NAME' in params.keys()
    assert 'SRC_LAN' in params.keys()
    assert 'TRG_LAN' in params.keys()
    assert 'DATA_ROOT_PATH' in params.keys()
    assert 'TEXT_FILES' in params.keys()
    assert 'INPUTS_IDS_DATASET' in params.keys()
    assert 'OUTPUTS_IDS_DATASET' in params.keys()
    assert 'INPUTS_IDS_MODEL' in params.keys()
    assert 'OUTPUTS_IDS_MODEL' in params.keys()
    assert 'METRICS' in params.keys()
    assert 'EVAL_ON_SETS' in params.keys()
    assert 'EVAL_ON_SETS_KERAS' in params.keys()
    assert 'START_EVAL_ON_EPOCH' in params.keys()
    assert 'EVAL_EACH_EPOCHS' in params.keys()
    assert 'EVAL_EACH' in params.keys()
    assert 'SAMPLING' in params.keys()
    assert 'TEMPERATURE' in params.keys()
    assert 'BEAM_SEARCH' in params.keys()
    assert 'BEAM_SIZE' in params.keys()
    assert 'OPTIMIZED_SEARCH' in params.keys()
    assert 'LENGTH_PENALTY' in params.keys()
    assert 'LENGTH_NORM_FACTOR' in params.keys()
    assert 'COVERAGE_PENALTY' in params.keys()
    assert 'COVERAGE_NORM_FACTOR' in params.keys()
    assert 'NORMALIZE_SAMPLING' in params.keys()
    assert 'ALPHA_FACTOR' in params.keys()
    assert 'SAMPLE_ON_SETS' in params.keys()
    assert 'N_SAMPLES' in params.keys()
    assert 'START_SAMPLING_ON_EPOCH' in params.keys()
    assert 'SAMPLE_EACH_UPDATES' in params.keys()
    assert 'POS_UNK' in params.keys()
    assert 'HEURISTIC' in params.keys()
    assert 'ALIGN_FROM_RAW' in params.keys()
    assert 'MAPPING' in params.keys()
    assert 'TOKENIZATION_METHOD' in params.keys()
    assert 'DETOKENIZATION_METHOD' in params.keys()
    assert 'APPLY_DETOKENIZATION' in params.keys()
    assert 'TOKENIZE_HYPOTHESES' in params.keys()
    assert 'TOKENIZE_REFERENCES' in params.keys()
    assert 'DATA_AUGMENTATION' in params.keys()
    assert 'FILL' in params.keys()
    assert 'PAD_ON_BATCH' in params.keys()
    assert 'INPUT_VOCABULARY_SIZE' in params.keys()
    assert 'MIN_OCCURRENCES_INPUT_VOCAB' in params.keys()
    assert 'MAX_INPUT_TEXT_LEN' in params.keys()
    assert 'OUTPUT_VOCABULARY_SIZE' in params.keys()
    assert 'MIN_OCCURRENCES_OUTPUT_VOCAB' in params.keys()
    assert 'MAX_OUTPUT_TEXT_LEN' in params.keys()
    assert 'MAX_OUTPUT_TEXT_LEN_TEST' in params.keys()
    assert 'LOSS' in params.keys()
    assert 'CLASSIFIER_ACTIVATION' in params.keys()
    assert 'OPTIMIZER' in params.keys()
    assert 'LR' in params.keys()
    assert 'CLIP_C' in params.keys()
    assert 'CLIP_V' in params.keys()
    assert 'SAMPLE_WEIGHTS' in params.keys()
    assert 'LR_DECAY' in params.keys()
    assert 'LR_GAMMA' in params.keys()
    assert 'MAX_EPOCH' in params.keys()
    assert 'BATCH_SIZE' in params.keys()
    assert 'HOMOGENEOUS_BATCHES' in params.keys()
    assert 'JOINT_BATCHES' in params.keys()
    assert 'PARALLEL_LOADERS' in params.keys()
    assert 'EPOCHS_FOR_SAVE' in params.keys()
    assert 'WRITE_VALID_SAMPLES' in params.keys()
    assert 'SAVE_EACH_EVALUATION' in params.keys()
    assert 'EARLY_STOP' in params.keys()
    assert 'PATIENCE' in params.keys()
    assert 'STOP_METRIC' in params.keys()
    assert 'MODEL_TYPE' in params.keys()
    assert 'ENCODER_RNN_TYPE' in params.keys()
    assert 'DECODER_RNN_TYPE' in params.keys()
    assert 'INIT_FUNCTION' in params.keys()
    assert 'SOURCE_TEXT_EMBEDDING_SIZE' in params.keys()
    assert 'SRC_PRETRAINED_VECTORS' in params.keys()
    assert 'SRC_PRETRAINED_VECTORS_TRAINABLE' in params.keys()
    assert 'TARGET_TEXT_EMBEDDING_SIZE' in params.keys()
    assert 'TRG_PRETRAINED_VECTORS' in params.keys()
    assert 'TRG_PRETRAINED_VECTORS_TRAINABLE' in params.keys()
    assert 'ENCODER_HIDDEN_SIZE' in params.keys()
    assert 'BIDIRECTIONAL_ENCODER' in params.keys()
    assert 'N_LAYERS_ENCODER' in params.keys()
    assert 'BIDIRECTIONAL_DEEP_ENCODER' in params.keys()
    assert 'DECODER_HIDDEN_SIZE' in params.keys()
    assert 'N_LAYERS_DECODER' in params.keys()
    assert 'ADDITIONAL_OUTPUT_MERGE_MODE' in params.keys()
    assert 'ATTENTION_SIZE' in params.keys()
    assert 'SKIP_VECTORS_HIDDEN_SIZE' in params.keys()
    assert 'INIT_LAYERS' in params.keys()
    assert 'DEEP_OUTPUT_LAYERS' in params.keys()
    assert 'WEIGHT_DECAY' in params.keys()
    assert 'RECURRENT_WEIGHT_DECAY' in params.keys()
    assert 'DROPOUT_P' in params.keys()
    assert 'RECURRENT_INPUT_DROPOUT_P' in params.keys()
    assert 'RECURRENT_DROPOUT_P' in params.keys()
    assert 'USE_NOISE' in params.keys()
    assert 'NOISE_AMOUNT' in params.keys()
    assert 'USE_BATCH_NORMALIZATION' in params.keys()
    assert 'BATCH_NORMALIZATION_MODE' in params.keys()
    assert 'USE_PRELU' in params.keys()
    assert 'USE_L2' in params.keys()
    assert 'EXTRA_NAME' in params.keys()
    assert 'MODEL_NAME' in params.keys()
    assert 'STORE_PATH' in params.keys()
    assert 'DATASET_STORE_PATH' in params.keys()
    assert 'SAMPLING_SAVE_MODE' in params.keys()
    assert 'VERBOSE' in params.keys()
    assert 'RELOAD' in params.keys()
    assert 'RELOAD_EPOCH' in params.keys()
    assert 'REBUILD_DATASET' in params.keys()
    assert 'MODE' in params.keys()
    assert 'TRAIN_ON_TRAINVAL' in params.keys()
    assert 'FORCE_RELOAD_VOCABULARY' in params.keys()


def test_params_type():
    params = load_parameters()
    assert isinstance(params['DATASET_NAME'], str)
    assert isinstance(params['SRC_LAN'], str)
    assert isinstance(params['TRG_LAN'], str)
    assert isinstance(params['DATA_ROOT_PATH'], str)
    assert isinstance(params['TEXT_FILES'], dict)
    assert isinstance(params['INPUTS_IDS_DATASET'], list)
    assert isinstance(params['OUTPUTS_IDS_DATASET'], list)
    assert isinstance(params['INPUTS_IDS_MODEL'], list)
    assert isinstance(params['OUTPUTS_IDS_MODEL'], list)
    assert isinstance(params['METRICS'], list)
    assert isinstance(params['EVAL_ON_SETS'], list)
    assert isinstance(params['EVAL_ON_SETS_KERAS'], list)
    assert isinstance(params['START_EVAL_ON_EPOCH'], int)
    assert isinstance(params['EVAL_EACH_EPOCHS'], bool)
    assert isinstance(params['EVAL_EACH'], int)
    assert isinstance(params['SAMPLING'], str)
    assert isinstance(params['TEMPERATURE'], int)
    assert isinstance(params['BEAM_SEARCH'], bool)
    assert isinstance(params['BEAM_SIZE'], int)
    assert isinstance(params['OPTIMIZED_SEARCH'], bool)
    assert isinstance(params['LENGTH_PENALTY'], bool)
    assert isinstance(params['LENGTH_NORM_FACTOR'], float)
    assert isinstance(params['COVERAGE_PENALTY'], bool)
    assert isinstance(params['COVERAGE_NORM_FACTOR'], float)
    assert isinstance(params['NORMALIZE_SAMPLING'], bool)
    assert isinstance(params['ALPHA_FACTOR'], float)
    assert isinstance(params['SAMPLE_ON_SETS'], list)
    assert isinstance(params['N_SAMPLES'], int)
    assert isinstance(params['START_SAMPLING_ON_EPOCH'], int)
    assert isinstance(params['SAMPLE_EACH_UPDATES'], int)
    assert isinstance(params['POS_UNK'], bool)
    assert isinstance(params['HEURISTIC'], int)
    assert isinstance(params['ALIGN_FROM_RAW'], bool)
    assert isinstance(params['MAPPING'], str)
    assert isinstance(params['TOKENIZATION_METHOD'], str)
    assert isinstance(params['DETOKENIZATION_METHOD'], str)
    assert isinstance(params['APPLY_DETOKENIZATION'], bool)
    assert isinstance(params['TOKENIZE_HYPOTHESES'], bool)
    assert isinstance(params['TOKENIZE_REFERENCES'], bool)
    assert isinstance(params['DATA_AUGMENTATION'], bool)
    assert isinstance(params['FILL'], str)
    assert isinstance(params['PAD_ON_BATCH'], bool)
    assert isinstance(params['INPUT_VOCABULARY_SIZE'], int)
    assert isinstance(params['MIN_OCCURRENCES_INPUT_VOCAB'], int)
    assert isinstance(params['MAX_INPUT_TEXT_LEN'], int)
    assert isinstance(params['OUTPUT_VOCABULARY_SIZE'], int)
    assert isinstance(params['MIN_OCCURRENCES_OUTPUT_VOCAB'], int)
    assert isinstance(params['MAX_OUTPUT_TEXT_LEN'], int)
    assert isinstance(params['MAX_OUTPUT_TEXT_LEN_TEST'], int)
    assert isinstance(params['LOSS'], str)
    assert isinstance(params['CLASSIFIER_ACTIVATION'], str)
    assert isinstance(params['OPTIMIZER'], str)
    assert isinstance(params['LR'], float)
    assert isinstance(params['CLIP_C'], float)
    assert isinstance(params['CLIP_V'], float)
    assert isinstance(params['SAMPLE_WEIGHTS'], bool)
    assert params['LR_DECAY'] is None
    assert isinstance(params['LR_GAMMA'], float)
    assert isinstance(params['MAX_EPOCH'], int)
    assert isinstance(params['BATCH_SIZE'], int)
    assert isinstance(params['HOMOGENEOUS_BATCHES'], bool)
    assert isinstance(params['JOINT_BATCHES'], int)
    assert isinstance(params['PARALLEL_LOADERS'], int)
    assert isinstance(params['EPOCHS_FOR_SAVE'], int)
    assert isinstance(params['WRITE_VALID_SAMPLES'], bool)
    assert isinstance(params['SAVE_EACH_EVALUATION'], bool)
    assert isinstance(params['EARLY_STOP'], bool)
    assert isinstance(params['PATIENCE'], int)
    assert isinstance(params['STOP_METRIC'], str)
    assert isinstance(params['MODEL_TYPE'], str)
    assert isinstance(params['ENCODER_RNN_TYPE'], str)
    assert isinstance(params['DECODER_RNN_TYPE'], str)
    assert isinstance(params['INIT_FUNCTION'], str)
    assert isinstance(params['SOURCE_TEXT_EMBEDDING_SIZE'], int)
    assert params['SRC_PRETRAINED_VECTORS'] is None
    assert isinstance(params['SRC_PRETRAINED_VECTORS_TRAINABLE'], bool)
    assert isinstance(params['TARGET_TEXT_EMBEDDING_SIZE'], int)
    assert params['TRG_PRETRAINED_VECTORS'] is None
    assert isinstance(params['ENCODER_HIDDEN_SIZE'], int)
    assert isinstance(params['BIDIRECTIONAL_ENCODER'], bool)
    assert isinstance(params['N_LAYERS_ENCODER'], int)
    assert isinstance(params['BIDIRECTIONAL_DEEP_ENCODER'], bool)
    assert isinstance(params['DECODER_HIDDEN_SIZE'], int)
    assert isinstance(params['N_LAYERS_DECODER'], int)
    assert isinstance(params['ATTENTION_SIZE'], int)
    assert isinstance(params['ADDITIONAL_OUTPUT_MERGE_MODE'], str)
    assert isinstance(params['SKIP_VECTORS_HIDDEN_SIZE'], int)
    assert isinstance(params['INIT_LAYERS'], list)
    assert isinstance(params['DEEP_OUTPUT_LAYERS'], list)
    assert isinstance(params['WEIGHT_DECAY'], float)
    assert isinstance(params['RECURRENT_WEIGHT_DECAY'], float)
    assert isinstance(params['DROPOUT_P'], float)
    assert isinstance(params['RECURRENT_INPUT_DROPOUT_P'], float)
    assert isinstance(params['RECURRENT_DROPOUT_P'], float)
    assert isinstance(params['USE_NOISE'], bool)
    assert isinstance(params['NOISE_AMOUNT'], float)
    assert isinstance(params['USE_BATCH_NORMALIZATION'], bool)
    assert isinstance(params['BATCH_NORMALIZATION_MODE'], int)
    assert isinstance(params['USE_PRELU'], bool)
    assert isinstance(params['USE_L2'], bool)
    assert isinstance(params['EXTRA_NAME'], str)
    assert isinstance(params['MODEL_NAME'], str)
    assert isinstance(params['STORE_PATH'], str)
    assert isinstance(params['DATASET_STORE_PATH'], str)
    assert isinstance(params['SAMPLING_SAVE_MODE'], str)
    assert isinstance(params['VERBOSE'], int)
    assert isinstance(params['RELOAD'], int)
    assert isinstance(params['RELOAD_EPOCH'], bool)
    assert isinstance(params['REBUILD_DATASET'], bool)
    assert isinstance(params['MODE'], str)
    assert isinstance(params['TRAIN_ON_TRAINVAL'], bool)
    assert isinstance(params['FORCE_RELOAD_VOCABULARY'], bool)


if __name__ == '__main__':
    pytest.main([__file__])
