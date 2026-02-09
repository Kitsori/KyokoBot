import os
from pymongo import MongoClient

import discord
from discord.ext import commands

import logging
from dotenv import load_dotenv

import random
import asyncio



XP_LEVELS = {
    1: 10,
    2: 15, # +5
    3: 20, # +5
    4: 25, # +5
    5: 30, # +5
    6: 40, # +10
    7: 50, # +10
    8: 60, # +10
    9: 70, # +10
    10: 85, # +15
    11: 100, # +15
    12: 115, # +15
    13: 130, # +15
    14: 150, # +20
    15: 170, # +20
    16: 190, # +20
    17: 210, # +20
    18: 235, # +25
    19: 260, # +25
    20: 285, # +25
    21: 310, # +25
    22: 340, # +30
    23: 370, # +30
    24: 400, # +30
    25: 430, # +30
}


def xp_to_level(level):
    return XP_LEVELS.get(level, None)


def level_up(player_data):
    leveledUp = False
    reward = 0

    while True:
        required = xp_to_level(player_data['level'])
        currentLevel = player_data['level']

        if required is None:
            break

        if player_data["xp"] >= required:
            player_data["xp"] -= required
            player_data["level"] += 1

            if currentLevel == 1:
                reward = 5
            elif currentLevel == 2:
                reward = 8
            elif currentLevel == 3:
                reward = 10
            elif currentLevel == 4:
                reward = 15
            elif currentLevel == 5:
                reward = 20
            elif currentLevel == 6:
                reward = 30
            elif currentLevel == 7:
                reward = 40
            elif currentLevel == 8:
                reward = 50
            elif currentLevel == 9:
                reward = 65
            elif currentLevel == 10:
                reward = 80



            leveledUp = True
        else:
            break
    return leveledUp, player_data, reward