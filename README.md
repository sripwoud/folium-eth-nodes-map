# Python Folium Ethereum Nodes Map

## Getting Started

```
gh repo clone r1oga/folium-eth-nodes-map
conda env create --file=environments.yml
python map.py
```

## Data

### Node list: [etherscan.io](https://etherscan.io/exportData?type=nodelist)

Latest 5000 records starting from 1st January 2021 as of 3rd January 2021.

```
"Node Id","Last Seen","Host","Port","Country","Client","Type","OS"
6ff20d36a96d7f4a48601c209527f23bd887f407e501a47bede9513be4e668b0f2492b5ec159fcba73d0cf4e6563c81005943de59f7cab8f029b8c9f24630bcc,Jan-01-2021 12:06:43 AM +UTC,47.242.151.65,0,United States, Geth, go1.15.3, Linux-amd64
c80fe0aa21095256b55902dfb5a27e9a346518f6ef6082408b1e0db7d3a053a3c031fb120fbf32be936c6fb81a8670104b07e78f1894b26887146ed0c602ecdb,Jan-01-2021 12:07:56 AM +UTC,168.119.0.139,30304,Germany,,,
eaabac0fe2e1bc79bfd624b57ba791f279d4e38c5b93a19ae8e369d555af1178bc9dbb5bfde848d568965aba2579740feb167a48540d9ec7ab93c41aca067c60,Jan-01-2021 12:09:26 AM +UTC,106.83.118.63,20182,China,,,
05fa1613cdd4f89d9236f3b4752a44d7edb6599fa3cc29b56694d563bfbdfdb1c7ea14a04e0846f0fbc602799126f66b1d51ac573c8042c31e1ed9e9f13eec1c,Jan-01-2021 12:11:58 AM +UTC,47.16.84.77,0,United States, Geth, go1.15.5, Linux-amd64
```

### IP locations: [ipwhois.io](https://ipwhois.io/)

GET Endpoint : `https://ipwhois.io/json/:ip`

```
{
  "ip": "47.242.151.65",
  "success": true,
  "type": "IPv4",
  "continent": "North America",
  "continent_code": "NA",
  "country": "United States",
  "country_code": "US",
  "country_flag": "https://cdn.ipwhois.io/flags/us.svg",
  "country_capital": "Washington",
  "country_phone": "+1",
  "country_neighbours": "CA,MX,CU",
  "region": "California",
  "city": "San Mateo",
  "latitude": "37.5629917",
  "longitude": "-122.3255254",
  "asn": "AS45102",
  "org": "Alibaba (Us) Technology Co. Ltd.",
  "isp": "Alibaba (China) Technology Co., Ltd.",
  "timezone": "America/Los_Angeles",
  "timezone_name": "Pacific Standard Time",
  "timezone_dstOffset": "0",
  "timezone_gmtOffset": "-28800",
  "timezone_gmt": "GMT -8:00",
  "currency": "US Dollar",
  "currency_code": "USD",
  "currency_symbol": "$",
  "currency_rates": "1",
  "currency_plural": "US dollars",
  "completed_requests": 5001
}
```

## Visualization: [folium](https://python-visualization.github.io/folium/) (python implementation of [leaflet.js](https://leafletjs.com/))
