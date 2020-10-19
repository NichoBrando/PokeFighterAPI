# PokeFighter API

## How to create database?

Database: https://www.kaggle.com/terminus7/pokemon-challenge
On command line, run these commands:

- `mongoimport -d PokeFighter -c pokemons --type csv --file pokemons.csv --headerline`
- `mongoimport -d PokeFighter -c combats --type csv --file combats.csv --headerline`
- `mongoimport -d PokeFighter -c tests --type csv --file tests.csv --headerline`

To Do:

- Add GET Pokemon and GET Pokemons routes;
- Add POST battle route;
- Add tests;
- Add Team Builder.
