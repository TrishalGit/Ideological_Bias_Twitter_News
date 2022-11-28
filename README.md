# Understanding the Impact of Ideological Bias on NLP Tasks
## Note
 - All the datasets are processed and stored in 'data' folder.
 - The classification models use dataset files from 'data' folder.
 - Follow Dataset Generation steps to regenerate/modify existing dataset.

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
### Naive Bayes
### SVM
### KNN
 - Comment out or Uncomment the lines #12-17 based on the data set in 'models/KNN.py'.
 - Execute the command in 'models' directory
> python3 KNN.py
### Random Forest
 - Comment out or Uncomment the lines #12-17 based on the data set.
 - Execute the command in 'models' directory
> python3 RandomForest.py
### Decision Tree
 - Comment out or Uncomment the lines #12-17 based on the data set.
 - Execute the command in 'models' directory
> python3 DecisionTree.py
### FastText
 - Comment out or Uncomment the lines #7-12 based on the data set.
 - Execute the command in 'models' directory
> python3 FastText.py
### BERT
