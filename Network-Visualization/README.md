# Network Visualization with D3.js

This project demonstrates how to visualize networks and interconnections using the D3.js (Data-Driven Documents) visualization library. The code is written in Python and SQLite for data preparation and management, and the resulting data is used to generate interactive network visualizations using D3.js.

## Project Overview
Network visualization is a powerful way to represent and understand complex relationships and connections between various entities. In this project, we use a combination of Python and SQLite for data processing and management, and D3.js for creating interactive and visually appealing network visualizations.
This collection of programs replicates several functions of a search engine. They utilize an SQLITE3 database named 'spider.sqlite' to store their data. You have the flexibility to delete this file at any time to initiate the process anew. The primary function of this program is to crawl a specified website and gather a sequence of web pages, while also recording the connections between these pages.

## Features
- Data collection and storage in an SQLite database.
- PageRank algorithm implementation to calculate page ranks for nodes in the network.
- Exporting data to JSON for use in D3.js visualizations.
- Interactive network visualization using D3.js.

## Prerequisites
Before you can use this project, make sure you have the following prerequisites installed:

- Python 3.x
- SQLite
- D3.js 

## Getting Started
Should you decide to restart the program and request it to crawl additional pages, it will refrain from re-crawling any pages that are already present in the database. Upon restart, it selects a random, unvisited page as its starting point. Therefore, each successive run of spider.py builds upon the previous one. It's worth noting that you can maintain multiple starting points within the same database, which are referred to as "webs" within the program. The spider makes random selections from all unvisited links across all the webs.

## Result - Example
<img width="834" alt="web2" src="https://github.com/aleksandrajk/Python-Projects/assets/55165756/0d541c7d-64eb-41fb-a1c2-d54626554d4c">

<img width="734" alt="web1" src="https://github.com/aleksandrajk/Python-Projects/assets/55165756/10da12db-08e3-42f9-a96b-ea3f53eac469">


## Acknowledgments
- [D3.js](http://d3js.org/) - The D3.js library for creating interactive data visualizations.
- [SQLite](https://www.sqlite.org/) - A self-contained, serverless, and zero-configuration SQL database engine.
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - The BeautifulSoup library for web scraping and HTML parsing.
- "Python for Informatics" Book by Dr. Charles Severance - This project is inspired by the concepts and teachings from the "Python for Informatics" book by Dr. Charles Severance.


