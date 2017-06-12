Market-Cart Demo
================
Install
-------
Clone this repository  
`git clone https://github.com/jdgranberry/market-cart.git`  
`cd market-cart`

Build the container image:  
`docker build -t market-cart:latest .`

Run the container (this is for Linux, may not be the same on OSX/Windows):  
`docker run -d --network=host -p 5000:5000 --name market-cart market-cart`

Usage
-----
You can add a list of items to a cart and retrieve the total like so:  
`curl http://localhost:5000/cart?new=CH1,AP1,CF1,MK1`  

which results in  
`$20.34`

Testing
------
Test cases are included. With the Python tox module, simply run  
`tox`