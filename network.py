from textgenrnn import textgenrnn

file_name = './formatted.txt'

model_cfg = {
	'rnn_size': 76,
	'rnn_layers': 3,
	'rnn_bidirectional': True,
	'max_length': 100,
	'max_words': 10000,
	'dim_embeddings': 100,
	'word_level': False
}

train_cfg = {
	'line_delimited': False,
	'num_epochs': 10,
	'gen_epochs': 2,
	'batch_size': 1024,
	'train_size': 0.8,
	'dropout': 0.0,
	'max_gen_length': 1000,
	'validation': False,
	'is_cvs': False
}

model_name = 'orban'
textgen = textgenrnn(name = model_name)

train_fuction = textgen.train_from_file
train_fuction(
	file_path = file_name,
	new_model = True,
	num_epochs = train_cfg['num_epochs'],
	gen_epochs = train_cfg['gen_epochs'],
	batch_size = train_cfg['batch_size'],
	train_size = train_cfg['train_size'],
	dropout  = train_cfg['dropout'],
	max_gen_length = train_cfg['max_gen_length'],
	validation = train_cfg['validation'],
	is_cvs = train_cfg['is_cvs'],
	rnn_layers = model_cfg['rnn_layers'],
	rnn_size = model_cfg['rnn_size'],
	rnn_bidirectional = model_cfg['rnn_bidirectional'],
	max_length = model_cfg['max_length'],
	dim_embeddings = model_cfg['dim_embeddings'],
	word_level = model_cfg['word_level'])