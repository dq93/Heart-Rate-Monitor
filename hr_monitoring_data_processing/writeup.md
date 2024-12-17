## Question 1

Take a look at the file labeled `data/data2.txt`. Why might we have missing values or values that state "NO SIGNAL" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?

Those values might still show some information, such as no signal appearing at specific times everyday could indicate something happening at that time.

## Question 2

While the "averages.png" and "maximums.png" graphs visualize typical values in our time-series data of heart rates and subsequently describe similar trends, the "stdevs.png" graph visualizes the standard deviations, which results in a graph with less apparent trends. In the context of heart rate, what does the standard deviation describe?

It could be that the person being studied was exercising or doing other activities that would show a different heart rate than normal.

## Question 3

Run your `main.py` module and look at the graph labeled "averages.png." Roughly speaking, where do you see the time series experience a significant difference in values along the x-axis? Point out all x-values where you notice a drastic difference in future values.

From 10 to 20 there is a huge spike, then from 25 to 30 a few spikes and dips to drop dramatically when it gets to 40. Around 45 it spikes up and then drops again.

## Question 4

Do you also notice a corresponding difference in values in the "stdevs.png" graph? If so, do these differences align with the "averages.png" graph? 

Yes it does align because in the stdevs you also see huge spikes at 10 and 35 being the most dramatic, while seeing lots of fluctuating between 10 - 30 and then from 40 - 45.
