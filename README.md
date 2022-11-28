# Understanding the Impact of Ideological Bias on NLP Tasks
## Libraries and Installations
 - We have used Python 3 for execution of all our models except for BERT we used Google Collab for pre-installed tenserflow libraries
 - To install other libraries required by the project run the below command in the project directory:-
> pip3 install -r requirements.txt

## Dataset Generation
### Dataset 1 (Twitter News)
 - Execute the below command in 'data_parser' directory
> python3 TwitterNewsDatasetGenerator.py
 - This will generate 3 files in 'data/pre_processed' directory: FoxNews.csv, CNN.csv, and NewsNation.csv.
 - The execution of the file can take approximately 12 hrs to generate 4440 tweets data from 3 news media sources.
 - If you want to increase the dataset size change the parameter on #line 12, to increase per category data.
 
### Dataset 2 (Harvard News)
 - Download the dataset zip file from this url [link](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/5XRZLH)
 - Unzip the HarvardNewsTweets and HarvardNewsTweets/dataverse_files and move to 'data' folder.
 - Execute the below command in 'data_parser' directory
> python3 HarvardNewsDataParser.py
 - This will generate 3 files in 'data/pre_processed' directory: FoxNewsHarvard.csv, CNNHarvard.csv, and WSJHarvard.csv.
 
### Train Test Split
 - To process to train test file split execute the below command in 'data_parser' directory
> python3 TrainTestDataProcessor.py
 - This will generate 12 files in 'data/train_test_split' directory: Left_Train.csv, Left_Train.csv, Right_Train.csv, Right_Test.csv, Neutral_Train.csv, Neutral_Test.csv, Left_Harvard_Train.csv, Left_Harvard_Train.csv, Right_Harvard_Train.csv, Right_Harvard_Test.csv, Neutral_Harvard_Train.csv, and Neutral_Harvard_Test.csv. 
 
## Model Executions
### Naive Bayes
### SVM
### KNN
 - Comment out or Uncomment the lines #12-17 based on the data set.
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
