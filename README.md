
## Table of contents:
- [Introduction](#intro)
- [Technologies](#tech)
- [project Setup](#projo)
- [Illustrations](#illus)
- [Project Information](#info)
- [Contributing](#contri)
- [Acknowledgments](#know)

<INTRODUCTION>

<h1 id="intro">Binance Battle</h1>

![Networth](img/battle.JPG)

**Binance-Supremacy-Battle**

A classical supremacy battle of who is the most fast(volatile) and strongest(momentum) coin/symbol pair  amongst usdt pairs within 24hrs . The battle takes place at the USDT SPOT MARKET (the base quote).The bulls front has been explored for now. Each battle lasts for 24hrs.

The draw  happens in the first 8 hrs starting from UTC +00.00  to select the top 10 strongest(momentum change) symbol pairs  in both fronts.

After the draw takes place, the top 10 symbol pairs are monitored after 24hrs and their vitals captured (High, low, close) .

The vitals are analyzed at the end of the 24hrs for each symbol pair and deductions made to determine if their speed and strength was steady for 24hrs after the draw.

The parameters of analysis are:

1. high (after 24 hrs) - close( after the initial draw)
2. the variation of close and high in percentage
4. If the change was positive or negative,if positive profit was made


**Hypothesis**

- The top 10 symbol pairs can potentially yield a profit-margin of 1-2% after the draw.


<TECHNOLOGIES>

<h1 id="tech">Technologies</h1>

**Builth With**
- Python
- Binance API


<PROJECT-SETUP>

<h1 id="projo">Project Setup</h1>


## Hardware Requirements
- You will need a desktop or a laptop computer.
- RAM: A minimum of 4GB RAM is recommended.
- Disk Space: You should have at least 5GB free of space on your working hard drive.

## Software Requirements

**environment**

The project was developed in (wsl2 ubuntu environment) .

**Prerequisites**

To get this project up and running locally, you must already have the following installed:
- [python plus the necessary packages installed on your computer](https://www.python.org/downloads/)
- [code editor ](https://code.visualstudio.com/)


**simple steps to set up on your local machine**

- git clone ```https://github.com/symonkipkemei/binance-battle.git ```
- set up your api key/secret key as virtual environment variable
- Set up and activate the virtual environment.
- install dependencies ```pip install -r requirements.txt```
- set up the date you would like to inspect the battle main(date, month, year)
- (incase of any installation issues,  screenshot ans share on [issues page](https://github.com/symonkipkemei/binance-battle/issues)


<ILLUSTRATIONS>

<h1 id="illus">Illustrations</h1>

![Search](img/search.JPG)
![Search](img/search2.JPG)

<PROJECT-INFORMATION>

<h1 id="info">Project Information</h1>

**Project Status**
- In progress

**To do**
-  Establish the RSI of each pair..
-  Detrmine coins whose momentum is slowing down within the first draw

**complete**
- Determine the change in momentum  of the top 10 coins after 24 hrs

**features**
- Your suggestions 😊............

<CONTRIBUTING>

<h1 id="contri">🤝 Contributing</h1>

Contributions, issues and feature requests are always welcome!

I love meeting other developers, interacting and sharing.

Feel free to check the [issues page](https://github.com/symonkipkemei/binance-battle/issues).

**How to Contribute**

To get a local copy up and running follow these simple example steps.

```
- Fork the repository
- git clone https://github.com/your_username/binance-battle
- git checkout develop
- git checkout -b branch name
- git remote add upstream https://github.com/symonkipkemei/binance-battle
- git pull upstream develop
- git commit -m "commit message"
- git push -u origin HEAD
```


<ACKNOWLEDGMENTS>

<h1 id="know">Acknowledgements</h1>

## Author

👤 **Symon Kipkemei**

- Github: [symonkipkemei](https://github.com/symonkipkemei)
- Twitter: [@symon_kipkemei](https://twitter.com/symon_kipkemei)
- LinkedIn: [Symon kipkemei](https://www.linkedin.com/in/symon-kipkemei/)


## Show your support


I can't promise to solve all your problems but I promise you won't have 
to face them alone 😊.

Finally, if you've read this far, don't forget to give this repo a ⭐️. 


## Acknowledgments

- [codingnomads](https://codingnomads.co/).



