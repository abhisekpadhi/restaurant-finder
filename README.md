# Restaurant Finder
Tiny tool to help you find a restaurant in an instant.
It uses [google geocoding api](https://developers.google.com/maps/documentation/geocoding/start) and [zomato api](https://developers.zomato.com/api)
to fetch the data in real time.

# How to run it
1. Clone the repo
```
git clone git@github.com:abhisekpadhi/restaurant-finder.git
```

2. Setup virtualenv
```
cd restaurant-finder
virtualenv venv
source venv/bin/activate
```

3. Install dependencies & set environment variables
```
pip install -r requirements.txt
export MAPS_API_KEY="<your-google-maps-api-key>"
export ZOMATO_API_KEY="<your-zomato-api-key>"
```

4. Run the tool
```
➜  ppt python restaurant_finder.py
What is your location?
BTM Stage 1
-> You are in Bengaluru
Here are the cuisines in Bengaluru, select your preference:
1035: Afghan
152: African
1: American
2: Andhra
4: Arabian
3: Asian
165: Assamese
131: Australian
292: Awadhi
193: BBQ
5: Bakery
227: Bar Food
132: Belgian
10: Bengali
270: Beverages
1013: Bihari
7: Biryani
1032: Bohri
247: Bubble Tea
168: Burger
22: Burmese
30: Cafe
121: Cantonese
994: Charcoal Chicken
18: Chettinad
25: Chinese
1040: Coffee
35: Continental
1014: Cuisine Varies
100: Desserts
268: Drinks Only
38: European
40: Fast Food
271: Finger Food
45: French
501: Frozen Yogurt
134: German
47: Goan
156: Greek
48: Gujarati
143: Healthy Food
1026: Hot dogs
49: Hyderabadi
233: Ice Cream
114: Indonesian
140: Iranian
55: Italian
60: Japanese
164: Juices
65: Kashmiri
178: Kebab
62: Kerala
63: Konkan
67: Korean
66: Lebanese
157: Lucknowi
102: Maharashtrian
69: Malaysian
71: Malwani
72: Mangalorean
70: Mediterranean
73: Mexican
137: Middle Eastern
1041: Mishti
1015: Mithai
1018: Modern Indian
1051: Momos
74: Mongolian
147: Moroccan
75: Mughlai
166: Naga
117: Nepalese
231: North Eastern
50: North Indian
1057: Odia
1048: Paan
290: Parsi
162: Peruvian
82: Pizza
87: Portuguese
88: Rajasthani
27: Raw Meats
1005: Roast Chicken
1023: Rolls
84: Russian
998: Salad
304: Sandwich
83: Seafood
993: Sindhi
119: Singaporean
972: South American
85: South Indian
89: Spanish
86: Sri Lankan
141: Steak
90: Street Food
177: Sushi
1054: Tamil
163: Tea
150: Tex-Mex
95: Thai
93: Tibetan
142: Turkish
99: Vietnamese
1024: Wraps
What cusines are in you mood for?
83 119             
Here is the best restaurant we found for you:

Name: Sriracha Robata & Contemporary Pan Asian Dining
Find on Zomato: https://www.zomato.com/bangalore/sriracha-robata-contemporary-pan-asian-dining-indiranagar-bangalore?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1
Address: 608, 12th Main Road, HAL, 2nd Stage, Indiranagar, Bangalore
Find on Maps: https://maps.google.com/?q=608+12th+Main+Road+HAL+2nd+Stage+Indiranagar+Bangalore
```

# Topics Covered

- input
- data type
- array
- dictionary
- string manipulation
- functions
- loops
- http calls
