# Snowboarding Index - AerisWeather API Challenge

## Snowboarding Index
This program calculates and outputs a snowboarding index (SBI) for a supplied location based on a weighted mix of 5 different data types. It calculates hourly indices and summarizes the next 8 hours, weighting the immediate and near future values higher.

#### Data types used
- Snowfall rate (averaged over previous 3 hours), as a rough proxy for snow depth
- Snowfall rate (at timestamp)
- Temperature
- Wind speed
- 'Feels Like' temperature

## Execution
Once installed, execute by `python -m snowboarding_index`. If no location is provided, IP address geolocation will be used.

#### Examples
`python -m snowboarding_index -l 12345`
`python -m snowboarding_index -l "minneapolis, mn"`

#### Flags
`-l, --location`: supply a location, either as a ZIP code or human readable name (e.g., Minneapolis, MN)
`-j, --json`: export a JSON string matching the AerisWeather Index API format
`-h, --help`: this information presented in the terminal.

## Setup
See [combined installation commands](#commands) for quick copy-paste installation.

#### Manual Installation
1. Download the code from Github manually or with git:
`git clone git@github.com:skydeo/API_Challenge.git`
2. Navigate to the folder
3. (Optional) Create and activate a virutal environment: 
`python -m venv venv/`
`source venv/bin/activate`
4. Install requirements
`pip install -r requirements.txt`
5. Run the package
`python -m snowboarding_index`

#### Combined Installation Commands
```
git clone git@github.com:skydeo/API_Challenge.git
cd API_Challenge
python -m venv venv/
source venv/bin/activate
pip install -r requirements.txt
python -m snowboarding_index
```
