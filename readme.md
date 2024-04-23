## eddn Plot

A simple example program to show how to use the eddn API (the MQ endpoint)
to receive messages about what is happening in the galaxy.

First we load a picture of the galaxy from a PPM file, and set the coordinates
to roughly what the incoming messages use: Sol centered at (0, 0), east/west
borders at +- 45000, north/south borders at 70000/-20000.

Then we receive messages, unpack them, and if they contain a location we plot
a yellow dot at that location.

Note that the events are not necessarily hyperjumps, as many more message types
contain a star position. But sometimes you can see people using the neutron
highway for example :)

Just let the program run for a while and watch the dots pop up...

More info about eddn (and the E:D addons that send to it) [here](https://edcodex.info/?m=tools&entry=24).

More info about the status of the eddn network [here](https://eddn.edcd.io/).
