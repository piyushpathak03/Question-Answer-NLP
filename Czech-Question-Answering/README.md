# Czech-Question-Answering
**TL;DR:** We have used SQuAD datasets and BERT and RoBERTa models designed for English question answering task. We have retrained them to obtain models solving question answering for the Czech language using cross-lingual transfer.

**Longer description:** Question answering is concerned with natural language processing and information rtetrieval. The main goal is to build a model that can automatically find an answer to a questions posed by humans in given text. There exists several models and datasets for this task in English but there are none for Czech which is more challenging because of its more complicated grammar and richer vocabulary.

This project focuses on building question answerting systems for Czech without requiring any manually annotated Czech training data. It is based on existing datasets and models developed for Eglish question answering task. We automatically translated SQuAD 1.1 and SQuAD 2.0 [datasets](https://arxiv.org/abs/1606.05250) to Czech to create train and test data, which we release at [this URL](https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-3249). We then trained and evaluated [BERT](https://arxiv.org/abs/1810.04805) and [XLM-RoBERTa](https://arxiv.org/abs/1907.11692) models based on Tranformer language model architecture. For such training, we used [this](https://github.com/huggingface/transformers) interface.

This repository contains other necessary scripts for dataset and model preprocessing. You can read more about this project and its results in [our article](https://arxiv.org/abs/2007.01667).
