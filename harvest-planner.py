# stardew valley crop harvest planner
# notifies based on day what crops need to be harvested
# implement a save feature so farm doesn't have to be reentered every use

import pickle  # for saving farm
import os

savefile_ext = ".sav"

# Crops lists and time to harvest

spring_crops = {
    "Blue Jazz": 7,
    "Cauliflower": 12,
    "Coffee Bean": [10, 2],
    "Garlic": 4,
    "Green Beans": [10, 3],
    "Kale": 6,
    "Parsnip": 4,
    "Potato": 6,
    "Rhubard": 13,
    "Strawberry": [8, 3],
    "Tulip": 6,
    "Unmilled Rice": [6, 8]  # depends if irrigated or not (in that order)
}

summer_crops = {
    "Blueberry": [13, 4],
    "Corn": [14, 4],
    "Hops": [11, 1],
    "Hot Pepper": [5, 3],
    "Melon": 12,
    "Poppy": 7,
    "Radish": 6,
    "Red Cabbage": 9,
    "Starfruit": 13,
    "Summer Spangle": 8,
    "Sunflower": 8,
    "Tomato": [11, 4],
    "Wheat": 4,
}

fall_crops = {
    "Amaranth": 7,
    "Artichoke": 8,
    "Beet": 6,
    "Bok Choy": 4,
    "Corn": [14, 4],
    "Cranberries": [7, 5],
    "Eggplant": [5, 5],
    "Fairy Rose": 12,
    "Grape": [10, 3],
    "Pumpkin": 13,
    "Sunflower": 8,
    "Wheat": 4,
    "Yam": 10,
}

special_crops = {
    "Ancient Fruit": [28, 7],
    "Cactus Fruit": [12, 3],
    "Pineapple": 14,
    "Taro Root": [7, 10],  # depends if irrigated or not (in that order)
    "Sweet Gem Berry": 24,
    "Tea Leaves": [20, 1]
}

'''
crop class

crop name (str)
day planted (int)
days until harvest (int)
irrigated (bool)

'''

class Crop:
    def __init__(self, name, planted, to_harvest, irrigated):
        self.name = name
        self.planted = planted
        self.to_harvest = to_harvest
        self.irrigated = irrigated

currentDay = 1

def advanceDay():
    global currentDay
    currentDay += 1

def main():
    global currentDay
    print(f"The current day is {currentDay}")

if __name__ == "__main__":
    main()