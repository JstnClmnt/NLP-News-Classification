# Topic Identification of Filipino and English News using Bidirectional Long-Short Term Memory with Attention Mechanisms

Topic Identification of News using BiLSTMs with Attention Mechanisms. Our data for the English News came from BBC News

## Getting Started

Download the dataset from http://mlg.ucd.ie/files/datasets/bbc-fulltext.zip and extract it in a folder named ``` /data ``` in the local directory.

### Prerequisites

What things you need to install the software and how to install them

* [Keras](https://keras.io/) - with Tensorflow Backend
* [Tensorflow 1.12](https://www.tensorflow.org/install/pip)
* [Pandas](https://pandas.pydata.org/)
* [Matplotlib](https://matplotlib.org/)
* [Numpy](https://www.numpy.org/)
* [NLTK](https://www.nltk.org/)


### Installing

* Create a folder named ```/Graph_LSTM``` and ```/Graph``` in the local directory so tensorboard will save the files there for the Ordinary LSTMs and LSTMs with Attention.

* Download  the GloVe Word Embeddings [here](https://nlp.stanford.edu/data/glove.6B.zip) and extract the file named ```glove.6B.300d.txt``` in the local directory


## Code

Just run the ```.ipynb``` file in your Jupyter Notebook and you're good to go.


## Authors

* **Christian Justine Clemente** - *Initial work* - [JstnClmnt](https://github.com/JstnClmnt)

See also the list of [contributors](https://github.com/JstnClmnt/NLP-News-Classification/contributors) who participated in this project.

## References

[[1]](https://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf) Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., ... & Polosukhin, I. (2017). Attention is all you need. In Advances in neural information processing systems (pp. 5998-6008).
<br>[[2]](https://github.com/philipperemy/keras-attention-mechanism) Keras implementation of Attention Mechanisms
<br>[[3]](https://github.com/tris-rivers/nlp-with-python/tree/master/StopWords%20Removal) Stop Words Function Removal for the Filipino Language
<br>[[4]](https://www.aclweb.org/anthology/D14-1162) Pennington, J., Socher, R., & Manning, C. (2014). Glove: Global vectors for word representation. In Proceedings of the 2014 conference on empirical methods in natural language processing (EMNLP) (pp. 1532-1543).
