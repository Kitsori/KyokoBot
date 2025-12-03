import os
from pymongo import MongoClient

import discord
from discord.ext import commands

import logging
from dotenv import load_dotenv

import random
import asyncio

XP_LEVELS = {
    1: 10, #10
    2: 25, #15
    3: 45, #20
    4: 70, #25
    5: 100, #30
    6: 140, #40
    7: 190, #50
    8: 255, #65
    9: 335, #80
    10: 435, #100
}


def xp_to_level(level):
    return XP_LEVELS.get(level, None)


def level_up(player_data):
    leveledUp = False

    while True:
        required = xp_to_level(player_data['level'])

        if required is None:
            break

        if player_data["xp"] >= required:
            player_data["xp"] -= required
            player_data["level"] += 1
            leveledUp = True
        else:
            break
    return leveledUp, player_data