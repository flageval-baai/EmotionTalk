import os

############ For LINUX ##############
DATA_DIR = {
    'mm4':  '/mnt/real_sda/MERTools-master/MERBench/dataset/mm-process',
    'mm7':  '/mnt/real_sda/MERTools-master/MERBench/dataset/mm-process',
}
PATH_TO_RAW_AUDIO = {
    'mm4': os.path.join(DATA_DIR['mm4'], 'subaudio'),
    'mm7': os.path.join(DATA_DIR['mm4'], 'subaudio'),
}
PATH_TO_RAW_VIDEO = {
    'mm4': os.path.join(DATA_DIR['mm4'], 'subvideo-tgt'),
    'mm7': os.path.join(DATA_DIR['mm4'], 'subvideo-tgt'),
}
PATH_TO_RAW_FACE = {

    'mm4': os.path.join(DATA_DIR['mm4'], 'openface_face'),
    'mm7': os.path.join(DATA_DIR['mm4'], 'openface_face'),
}
PATH_TO_TRANSCRIPTIONS = {
    'mm4': os.path.join(DATA_DIR['mm4'], 'transcription.csv'),
    'mm7': os.path.join(DATA_DIR['mm4'], 'transcription.csv'),
}
PATH_TO_FEATURES = {
    'mm4': os.path.join(DATA_DIR['mm4'], 'features'),
    'mm7': os.path.join(DATA_DIR['mm4'], 'features'),
    'MM': os.path.join(DATA_DIR['mm4'], 'features'), 
}
PATH_TO_LABEL = {	
    'mm4': os.path.join(DATA_DIR['mm4'], 'mm_label4.npz'),
    'mm7': os.path.join(DATA_DIR['mm7'], 'mm_label.npz'),
    'MM': os.path.join(DATA_DIR['mm7'], 'mm_label.npz'),
}

# pre-trained models, including supervised and unsupervised
# PATH_TO_PRETRAINED_MODELS = '/mnt/real_sda/wangxuechen_space/code/MERBench/models/'
PATH_TO_PRETRAINED_MODELS = '/mnt/real_sda/MERTools-master/MERBench/feature_extraction/checkpoint'
PATH_TO_OPENSMILE = './tools/opensmile-2.3.0/'
PATH_TO_FFMPEG = '/mnt/real_sda/ffmpeg-4.4.1-i686-static/ffmpeg'

# dir
SAVED_ROOT = os.path.join('./saved')
MODEL_DIR = os.path.join(SAVED_ROOT, 'model')
LOG_DIR = os.path.join(SAVED_ROOT, 'log')
PREDICTION_DIR = os.path.join(SAVED_ROOT, 'prediction')
FUSION_DIR = os.path.join(SAVED_ROOT, 'fusion')
SUBMISSION_DIR = os.path.join(SAVED_ROOT, 'submission')


############ For Windows [OpenFace to extract face] ##############
DATA_DIR_Win = {
    'mm4': '/mnt/real_sda/MERTools-master/MERBench/dataset/mm4-process',
    'mm7': '/mnt/real_sda/MERTools-master/MERBench/dataset/mm4-process',
    'MM': '/mnt/real_sda/MERTools-master/MERBench/dataset/mm4-process',
}

PATH_TO_RAW_FACE_Win = {
	'mm4':   os.path.join(DATA_DIR_Win['mm4'],   'video'),
	'mm7':   os.path.join(DATA_DIR_Win['mm4'],   'video'),
}

PATH_TO_FEATURES_Win = {
	'mm4':   os.path.join(DATA_DIR_Win['mm4'],   'features'),
	'mm7':   os.path.join(DATA_DIR_Win['mm4'],   'features'),
	'MM':   os.path.join(DATA_DIR_Win['MM'],   'features'),
}

PATH_TO_OPENFACE_Win = "H:\\desktop\\Multimedia-Transformer\\MERBench-master\\tools\\openface_win_x64"
