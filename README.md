# Understanding the Impact of Ideological Bias on NLP Tasks
## Directory Structure
 - data (contains all the processed data files)
 - data_parser (contains code files for dataset generation)
 - models (contains model code files)

## Note
 - All the datasets are processed and stored in 'data' folder.
 - The classification models use dataset files from 'data' folder.
 - Follow Dataset Generation steps to regenerate/modify existing dataset.
 - File paths are currently hardcoded in the files. Will try to add some automation in future.

## Libraries and Installations
 - We have used Python 3 for execution of all our models except for BERT we used Google Collab for pre-installed tenserflow libraries
 - To install other libraries required by the project run the below command in the project directory:-
> pip3 install -r requirements.txt
 - For FastText install through below commands
```
$ git clone https://github.com/facebookresearch/fastText.git
$ cd fastText
$ pip install .
```

## Dataset Generation
### Dataset 1 (Twitter News)
 - Execute the below command in 'data_parser' directory
> python3 TwitterNewsDatasetGenerator.py
 - This will generate 3 files in 'data/pre_processed' directory: FoxNews.csv, CNN.csv, and NewsNation.csv.
 - The execution of the file can take approximately 12 hrs to generate 4440 tweets data from 3 news media sources.
 - If you want to increase the dataset size change the parameter on #line 12, to increase per category data.
 
### Dataset 1 (Harvard News)
 - Download the dataset zip file from this url [link](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/5XRZLH)
 - Unzip the HarvardNewsTweets and HarvardNewsTweets/dataverse_files and move to 'data' folder.
 - Execute the below command in 'data_parser' directory
> python3 HarvardNewsDataParser.py
 - This will generate 3 files in 'data/pre_processed' directory: FoxNewsHarvard.csv, CNNHarvard.csv, and WSJHarvard.csv.
 
### Train Test Split
 - To process to train test file split execute the below command in 'data_parser' directory
> python3 TrainTestDataProcessor.py
 - This will generate 12 files in 'data/train_test_split' directory: Left_Train.csv, Left_Test.csv, Right_Train.csv, Right_Test.csv, Neutral_Train.csv, Neutral_Test.csv, Left_Harvard_Train.csv, Left_Harvard_Test.csv, Right_Harvard_Train.csv, Right_Harvard_Test.csv, Neutral_Harvard_Train.csv, and Neutral_Harvard_Test.csv.

### FastText Data
 - Fasttext accepts data in different format with '__label__' + original_label followed by the text string.
 - Comment out or Uncomment the lines #6-11 based on the data set in 'data_parser/FastTextDatasetGenerator.py'.
 - Execute the command in 'data_parser' directory
> python3 FastTextDatasetGenerator.py
 - This will generate 12 files (6 on each execution based on dataset) in 'data/fasttext' directory: Left_Train.train, Left_Test.test, Right_Train.train, Right_Test.test, Neutral_Train.train, Neutral_Test.test, Left_Harvard_Train.train, Left_Harvard_Test.test, Right_Harvard_Train.train, Right_Harvard_Test.test, Neutral_Harvard_Train.train, and Neutral_Harvard_Test.test.
 
## Model Executions
### Naive Bayes & SVM
 - Comment out or Uncomment the lines {15-16, 26-27, 37-40, 112-113, 167-168} based on the data set in 'models/NaiveBayesandSVM.py'.
 - Execute the command in 'models' directory
> python3 NaiveBayesandSVM.py
### KNN
 - Comment out or Uncomment the lines #12-17 based on the data set in 'models/KNN.py'.
 - Execute the command in 'models' directory
> python3 KNN.py
### Random Forest
 - Comment out or Uncomment the lines #12-17 based on the data set in 'models/RandomForest.py'.
 - Execute the command in 'models' directory
> python3 RandomForest.py
### Decision Tree
 - Comment out or Uncomment the lines #12-17 based on the data set in 'models/DecisionTree.py'.
 - Execute the command in 'models' directory
> python3 DecisionTree.py
### FastText
 - Comment out or Uncomment the lines #7-12 based on the data set in 'models/FastText.py'.
 - Execute the command in 'models' directory
> python3 FastText.py
### BERT
 - The BERT model code is split into 3 files inside 'models/BERT' as bert_left.py (train on left data), bert_right.py (train on right data) and bert_neutral.py (train on neutral data)
 - To execute the file need to run on Google Collab for convenience and pre-existing libraries + GPU support.
 - Copy 'train_test_split' folder in 'data' to your google drive. The code can pull the dataset from drive.
 - Open new collab notebook and copy-paste the python code inside the '.py' file one at a time.
 - Comment out or Uncomment the lines based on the data set to use.
 - Click 'Runtime' -> 'Run all' to execute the code.
 - After first time execution the collab will install necessary libraries and tries to mount to Google Drive which the user has to allow for dataset access.
 - The code executions might take 40min to 1hr 30min.
#### Issues
 - During first execution you might get this error (No module named 'tensorflow_text') 
 ![TensorFlowError](https://user-images.githubusercontent.com/96170761/204177888-c1972984-82fd-487b-9410-3ffd63a3c4ef.png)
 - Please end the current execution and Re-run the code. 
 - If the issue still persists contact the authors @GayamTrishal or @HirthikMathavan

