## CineSense- The Review Sentiment Analysis

🎬 Description

    This project is a Deep Learning web application that classifies movie reviews as Positive or Negative using a Simple RNN (Recurrent Neural Network).



🧠 Model Training 

    The model was developed and trained in RNN. 
    
    Key steps include- Dataset: Used the IMDB dataset containing 50,000 highly polar movie reviews.
    
    Vocabulary Limit- Restricted to the top 10,000 most frequent words to maintain efficiency.
    
    Architecture- 

        Embedding Layer: Maps word indices to dense vectors.
        
        Simple RNN: Captures sequential information from the text.
        
        Dense Layer: A final sigmoid-activated layer for binary 
        
        classification.Optimization: Trained using the adam optimizer and binary_crossentropy loss function.
        
        Export: The final trained model is saved as imdb_simple_RNN_model.keras.
        
        
        
🔍 Prediction Logic (app.py)

    The prediction file handles the real-time inference. Since the model cannot understand raw text, the following pipeline is implemented:
    
        Tokenization: The input review is converted to lowercase and split into individual words.
        
        Indexing: Each word is mapped to its corresponding index from the IMDB word index.
        
        Thresholding: Any word index $> 10,000$ is treated as an 'unknown' token to prevent dimension errors.
        
        Padding: To ensure uniform input size, sequences are padded or truncated to a length of 500.
        
        Inference: The processed array is fed into the model to get a sentiment score between 0 and 1.
        
        
        
🛠️ Tech StackTensorFlow/Keras: 

    For model building and loading.
    
    Streamlit: For the web-based user interface.
    
    NumPy: For array manipulations and preprocessing.
    
    Google Colab: Used as the primary environment for training.
    
    
    
🚀 How to RunMount Drive: 

    Ensure your trained model is accessible in the specified path.

    Install Dependencies: pip install -r requirements.txtLaunch 
    
    App: streamlit run app.py

