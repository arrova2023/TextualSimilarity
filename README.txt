This project focuses on calculating the textual similarity between two texts: an original text and a suspect text. The textual similarity will be calculated using the Jaccard index, which measures the similarity between two sets through the intersection and union of their elements.
Requirements

To run this project, make sure you have Python 3.11 or higher installed. You will also need the spacy library to perform stemming of the text. You can install it using the following command:

pip install spacy

In addition, the file "stopwords.txt" is required, which contains a list of function words in Spanish. Make sure you have this file in the "resources/stopwords.txt" path.
Use

Place the texts original.txt and suspect.txt in the "corpus/" folder.

Autorun: To run the entire process automatically, simply run the "main.py" file from the command line using the following command:

python main.py

The "main.py" script will perform all tasks in the project, including text preprocessing, corpus generation, comparison matrix creation, similarity and entropy calculation, as well as temperature and energy calculation.

Results: Once the "main.py" script has been executed, the results of each stage will be saved to text files in the "scores/" folder. In particular, similarity results will be stored in "scores/similarity/similarity.res", entropy results in "scores/entropy/entropy.res", and temperature results in "scores/temperature/temperature.res" . Also, the final result of the similarity between the original text and the suspect text will be saved in "scores/discerned/discerned.res".

Additional notes

    If you want to run each stage separately, you can run the corresponding files, such as "lemmatize.py" for preprocessing and lemmatization, "matrix.py" to create the comparison matrix, "entropy.py" to calculate entropy, and " temperature.py" to calculate the temperature.

    If you need to change the stopwords used in the project, you can edit the "stopwords.txt" file in the "resources/" folder.

    If you want to add more detail or functionality to the project, you can explore and modify the corresponding Python files. Comments in the code will guide you on how it works.