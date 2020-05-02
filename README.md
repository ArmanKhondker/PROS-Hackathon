![build-passing](https://img.shields.io/badge/build-passing-brightgreen) ![test-passing](https://img.shields.io/badge/test-passing-brightgreen)

# PROS Hackathon 2018 Project

Our assignment was to **“Develop a B2B pricing solution that can leverage competitor prices based upon pricing data repositories, screen-scraping tools, indexes, or other data sources in dynamic and sustainable manner.”** Our solution was two-pronged, consisting of a machine learning based estimator and a sentiment analyzer. Our estimator estimated the market valuation of a product based on technical features of the product. Our sentiment analyzer parsed YouTube review video comments to determine public sentiment of a brand. This assigns a measurable value to the online research process that consumers (especially millenials) carry out before making a purchase. We connected this backend to a React frontend, via a Flask REST API.

## Getting Started

To run the application you need only run two files:
* **server.py** will run the backend server locally and connect everything together
* Calling **npm run start** in the **webapp* folder will run the React frontend

### Prerequisites

* Running Python 2.7 and having the scikit-learn/matplotlib packages installed should be enough to run the estimator.
* Making a Google Cloud account and getting the proper token to run everything will be needed to run the sentiment analysis.
* The Flask REST API shouldn't take anything other than installing Flask.
* The React frontend will take the most installation. Details for that can be found in the README file in the **webapp** folder


## Built With

* [Scikit-Learn](http://www.dropwizard.io/1.0.2/docs/) - Machine learning model
* [Google Cloud Youtube Data API](https://console.cloud.google.com/launcher/details/google/youtube.googleapis.com?pli=1) - Sentiment analysis
* [React.js](https://reactjs.org) - Frontend
* [Flask](http://flask.pocoo.org) - REST API to connect Python backend to React frontend


## Authors

* **Matthew Mutammara** - *Estimator and REST API* - Rice University
* **Arman Khondker** - *Sentiment Analysis* - University of Texas at Austin
* **Katherine Jewett** - *Frontend development* - University of Houston
* **Brianna Frausto** - *Business pitch and competition presentation* - University of Houston

## Acknowledgments

Thanks to [PROS inc.](https://www.pros.com) for putting on this event!
