This is the folder regarding HMM Generation made in the course of the MSc Individual Project.

--------------------------------
In order to make work this you need to have installed the following dependencies:
	- Cython
	- Scipy
	- Numpy
	- Pandas
	- Setup tools
	- Sklearn
	- Statsmodels
	
The versions of those dependencies can create issues so make sure to install adequate ones.


Then in a command line after being in the synsys folder make the setup of pomegranate with:
python3 setup.py build_ext --inplace install –user

Finally you can now execute the algorithm with:
python runSynSys.py /path/to/originalsmarthomedata.csv <integer number of HMM states for activity HMM> <integer number of HMM states for sensor event HMM’s> <integer time interval in hours for timestamp reset> <integer to indicated type of model for timestamp generation> <most frequent activity in your dataset>

--------------------------------
Your orginal smart home data must contains an ordered sequence of sensor events in the following format: 
<date> <time> <sensor name> <sensor state or reading> <activity label>

This is the type of format that the pipeline Jupyter notebook gives
