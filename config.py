#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "a70e1e42-bc74-4186-842d-477e4781c29c")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "B108Q~11fiZCfptTKIoQ_tpnOfwy_33eyqPVXc79")
