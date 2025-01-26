# eggs.cheap

[eggs.cheap](http://eggs.cheap) is a dumb website to track the price of eggs during the Trump presidency compared the final value of the Biden presidency. and display it as a webpage.

## Requirements

- Graph updated daily from [https://tradingeconomics.com/commodity/eggs-us](https://tradingeconomics.com/commodity/eggs-us)
- Simple yes/no displayed when price changes to be above or below
- ko-fi donation button

## Stretch Goals

- Daily post to Bluesky with link to page
- Auto link to relevant news articles
- Actually look like a decent website
- Find way for donation button to auto-suggest a starting price equal to a dozen eggs

## To-Dos

- [x] Set up basic webpage template
- [x] Scrape data from [https://tradingeconomics.com/commodity/eggs-us](https://tradingeconomics.com/commodity/eggs-us) daily
    - [x] Add day's value to database
    - [ ] Use database for chart rendering
- [x] Render chart on simple webpage
- [x] Add Donation button
