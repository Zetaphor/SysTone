# SysTone: Make busy computers noisy again

![systone_logo](https://github.com/Zetaphor/SysTone/assets/3112763/bbbc4f67-e7a6-463e-9d32-26d8bd8f8869)

_Logo by DALL-E, edited by Zetaphor. Application and README written in collaboration with GPT-4_

## Overview
SysTone is a software project that creates an auditory representation of your computer's performance. It plays oscillating tones where the frequency and modulation are influenced by the CPU's current load, reminiscent of the sounds made by older, mechanically noisier computers.

## Demo

https://github.com/Zetaphor/SysTone/assets/3112763/9ffae60a-cbb0-450b-bc33-c20de2a89e82


## Installation
To run SysTone, you need to have Python installed on your system. Additionally, you must install the necessary dependencies listed in `requirements.txt`.

1. Clone this repository or download the source code.
2. Install the required Python packages:

```shell
pip install -r requirements.txt
```

## Usage
To start SysTone, run the main Python script:

```shell
python SysTone.py
```

The script will start playing an oscillating tone, modulated based on your CPU load. You can terminate the program by pressing `Ctrl+C`.

## Requirements
- Python 3.x
- Numpy
- PyAudio
- Psutil

## License
MIT License
