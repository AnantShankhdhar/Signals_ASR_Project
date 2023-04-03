# Signals_ASR_Project


## Project Overview ##
* We plan on building a Machine Learning Based Voice Analytics tool. The toolkit Designed for multiple forms of analysis from audio data intended to help understand the speaker and their behaviour for optimizing business functions etc.

* We will design the toolkit to be able to perform various forms of analysis on both live audio recorded as well as a stream of audio files stored in a folder, this can be easily used in a web application.

* The application will consist of two main modules:-
  * Extracting text from audio using automatic speech recognition(ASR)
  * Performing different kinds of analysis on the extracted text using natural language processing

## Automatic Speech Recognition ##
* We plan on using DL models for speech recognition
 * DeepSpeech -  It is a multi layer BiLSTM model which utilizes the CTC loss. We will train the model on Common Voice Dataset made available by the   Mozilla Foundation.
 * Wav2Vec2 - It is the state of the art transformer based model released by Facebook. Pretrained model is available which can also be used

* Datasets - 
 * The Common Voice dataset consists of a unique MP3 and corresponding text file. 
 The dataset is available for 96 languages but we will use the English split.


