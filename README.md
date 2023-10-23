

<!-- Find and Replace All [repo_name] -->
<!-- Replace [product-screenshot] [product-url] -->
<!-- Other Badgets https://naereen.github.io/badges/ -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn1][linkedin-shield1]][linkedin-url1]
[![LinkedIn2][linkedin-shield2]][linkedin-url2]
<!-- [![License][license-shield]][license-url] -->


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Link To Live Streamlit App</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <ul>
        <li><a href="#mvp">M.V.P.</a></li>
        <li><a href="#stretch-goals">Stretch Goals</a></li>
      </ul>
    <li><a href="#contributing">Contributing</a></li>
	<!-- <li><a href="#license">License</a></li> -->
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This project was created by: Nick Danialy and Jose Tollinchi and its live on Streamlit.  See the link in the Usage section

This is an application that fetches historical data on 1 index, 4 stocks, and 2 crypto currencies and performs analytical calculations to assist in conducting a relative analysis between the index and the crypto currencies to determine if a relationship exists and the type of relationship for the purpose of conducting portfolio analysis and Monte Carlo Simulation for forecasting potential future returns.

The user can experiment with many different variations of choices for portfolio analysis based on preferences and risk tolerance.

### Built With

<!-- This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples. -->

* [Postman](https://www.postman.com/downloads/)
* [Python](https://www.python.org/)
* [Python CSV Reading/Writing](https://docs.python.org/3/library/csv.html)
* [Python pandas](https://pandas.pydata.org/)
* [Python Streamlit](https://streamlit.io/)
* [Python hvplot.pandas](https://hvplot.holoviz.org/index.html)
* [Python conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
* [Python JupyterLab](https://jupyter.org/)

<!-- GETTING STARTED -->
## Getting Started

<!-- This is an example of how you may give instructions on setting up your project locally. To get a local copy up and running follow these simple example steps. -->
You don't need Python directly on your system. You can install Anaconda for a virtual environment and JupyterLab normally just like any other application on your computer. Follow the instructions for Anaconda, ensure that its working, then install JupyterLab.

You will need Anaconda Navigator as the preferred tool to install the Streamlit environment.  Go to the Streamlit docs to follow the installation.

We used Postman and Jupyter Lab to test the APIs, look at the object returned, and look at the dataframe to develop the ETL code/process (extraction, transformation, and loading) of the data.

I have placed Comments throughout the code so that you can follow the code and be able to replicate the app on your own. Also, so that you're able to contribute in the future :-)

### Prerequisites

<!-- This is an example of how to list things you need to use the software and how to install them. -->
A text editor such as [VS Code](https://code.visualstudio.com/) or [Sublime Text](https://www.sublimetext.com/)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/AnaIitico/grayscale_analysis.git
   ```

2. You don't need to install pip - Conda comes with pip and you can also use the command
    conda install 'package name'
   
3. Install Conda according to the instructions based on your operating system.
    For windows users you MUST use the Administrator PowerShell. Users with AMD Processors MUST use the Administrator PowerShell 7 (X64) version
  
    Once installed Conda has an Admin PowerShell version shortcut - look on your Start menu for it.
    This shortcut will prove very useful at times when you need to install other apps or make adjustments to your installation

    Once installed and you have finished all Conda instructions, you will see (base) on your terminal.  Make sure that you finish the Conda full installation or this will not work!!
   
4. Activate Conda Dev environment
   ```sh
   conda activate dev
   ```
    You should now see (dev) on your terminal (if not go back to step 3)

5. Install JupyterLabs
   ```sh
   pip install jupyterlab
   ```

6. Run JupyterLab as needed
   ```sh
   jupyter lab
   ```
    A browser window should open on localhost:8888/lab

7. Rename the .ignoreSample to .ignore to keep those folders out of you repo, and keep your keys secret.  Add any folders or filenames that you want to exclude from your repo into this file.

8. Install Streamlit from the Anaconda Navigator

9. Install yfinance Api
   ```sh
   pip install yfinance
   ```
10. Install other dependencies with conda.
    - Search google for the correct conda intall command
    - See the acknowledgements sections for other dependencies 

<!-- USAGE EXAMPLES -->
## Usage

https://share.streamlit.io/anaiitico/grayscale_analysis/main/app.py


<!-- ROADMAP -->
## Roadmap

### M.V.P.
### Provide the following:
 - User input for data parameters
 - Error catching logic for user input
 - Price correlations between assets
 - Asset Beta compared to Index
 - Correlation Heatmap
 - Sharpe Ratios
 - Hypothetical past portfolio performance

### Stretch Goals
### Provide the following:
 - Hypothetical future portfolio performance based on weighted assets
 - Monte Carlo Simulation based on user input

<!-- This is an example of how to list things you need to use the software and how to install them. -->
A text editor such as [VS Code](https://code.visualstudio.com/) or [Sublime Text](https://www.sublimetext.com/)

### Here are some screenshots and code snippets of the working app

#### App User Interface
![App User Interface][app-screenshot]

#### Beta & Normalized Portfolio 
![Beta & Normalized Portfolio][beta-screenshot]

#### Heatmap 
![Heatmap][heatmap-screenshot]

#### Historical Portfolio 
![Historical Portfolio][historical-screenshot]

#### Monte Carlo Simulation Results 
![Monte Carlo Simulation Results][montecarlo-screenshot]


<!-- #### Description
#### you can see the full code (with outputs) in the [risk_return_analysis.ipynb](https://github.com/AnaIitico/grayscale_analysis/blob/main/risk_return_analysis.ipynb) file
  *This code has been summarized into one block for convenience*
  *and there's an analysis at the end*
```sh
  some cool code goes here
 ```

See the [open issues](https://github.com/AnaIitico/grayscale_analysis/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
<!-- ## License

Distributed under the MIT License. See `LICENSE` for more information.
 -->

<!-- CONTACT -->
## Contact

Jose Tollinchi - [@josetollinchi][linkedin-url1] - jtollinchi1971@gmail.com

Nick Danialy - [@nicklaus-danialy][linkedin-url2] - nickdanialy@gmail.com

Project Link: [https://github.com/AnaIitico/grayscale_analysis](https://github.com/AnaIitico/grayscale_analysis)

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

Other Dependencies used to build the project.
##### Search google for the correct conda install command

* pandas
* python-dotenv

Other Acknowledgements
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* Yahoo!, Y!Finance, and Yahoo! finance are registered trademarks of Yahoo, Inc.
yfinance is not affiliated, endorsed, or vetted by Yahoo, Inc. It's an open-source tool that uses Yahoo's publicly available APIs, and is intended for research and educational purposes. You should refer to Yahoo!'s terms of use ([here](https://legal.yahoo.com/us/en/yahoo/terms/otos/index.html) [here](https://policies.yahoo.com/us/en/yahoo/terms/product-atos/apiforydn/index.htm) [here](https://policies.yahoo.com/us/en/yahoo/terms/index.htm)) for details on your rights to use the actual data downloaded. Remember - the Yahoo! finance API is intended for personal use only.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/AnaIitico/grayscale_analysis.svg?style=for-the-badge
[contributors-url]: https://github.com/AnaIitico/grayscale_analysis/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/AnaIitico/grayscale_analysis.svg?style=for-the-badge
[forks-url]: https://github.com/AnaIitico/grayscale_analysis/network/members
[stars-shield]: https://img.shields.io/github/stars/AnaIitico/grayscale_analysis.svg?style=for-the-badge
[stars-url]: https://github.com/AnaIitico/grayscale_analysis/stargazers
[issues-shield]: https://img.shields.io/github/issues/AnaIitico/grayscale_analysis/network/members?style=for-the-badge
[issues-url]: https://github.com/AnaIitico/grayscale_analysis/issues
<!-- [license-shield]: 
[license-url]:  -->
[linkedin-shield1]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-shield2]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url1]: https://www.linkedin.com/in/josetollinchi/
[linkedin-url2]: https://www.linkedin.com/in/nicklaus-danialy/
[app-screenshot]: /images/website.PNG
[beta-screenshot]: /images/beta_normalized_portfolio.PNG
[heatmap-screenshot]: /images/heatmap_correlation.PNG
[historical-screenshot]: /images/historical_portfolio.PNG
[montecarlo-screenshot]: /images/monte_carlo_output.PNG
