# Box_Office_Success
![header](movie_header.png)
**Linear Regression project predicting box office success using data scraped from Box Office Mojo.**

In this repo you will find the following files:
* My [powerpoint presentation](https://github.com/S-DeFerrari/Box-Office-Success/blob/master/Better%20Movies%20Through%20Data.pdf) on this project going over each step of the process as well as my results. This is the best place to start.
* The jupyter notebook I used for [scraping Box Office Mojo.](https://github.com/S-DeFerrari/Box-Office-Success/blob/master/p2_scraping.ipynb)
* The jupyter notebook I used for [feature engineering.](https://github.com/S-DeFerrari/Box-Office-Success/blob/master/p2_features.ipynb)
* The juptyer notebook I used for [modeling.](https://github.com/S-DeFerrari/Box-Office-Success/blob/master/p2_modeling.ipynb)
* The [CSV file](https://github.com/S-DeFerrari/Box-Office-Success/blob/master/BlackListAll-updated.csv) of all Hollywood Blacklist films from 2008 through 2017

The data is a combination of data I scraped along with a kaggle [dataset](https://www.kaggle.com/ardenthira/hollywood-black-list-20082017) containing all of the films featured on the ["Hollywood Blacklist"](https://blcklst.com/) of promising scripts.


## Deployment with Streamlit App via and AWS EC2 Instance
I successfully deployed this model to the web by creating a python file containing the pickled model results and the code necessary to input variables needed for a prediction via the user-friendly Streamlit library! The code for this deployment can be found in the 'box_office_stream_deploy.py' file.

![](web_app.png)
