# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount
import requests
import json

class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    async def on_message_activity(self, turn_context: TurnContext):
        
        url = "https://bot.honohr.com/pulsebot/honobot/getUnitData/"
        qw = turn_context.activity.text

        payload = json.dumps({
        "state": qw
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload,verify=False)

        print(response.json())
        print(turn_context.activity.text)
        # await turn_context.send_activity(f"aapne bola hai '{ turn_context.activity.text }'")
        await turn_context.send_activity(f"aapne bola hai '{ response.text }'")


    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")
