#!/usr/bin/env python3

from garth.exc import GarthHTTPError
from garminconnect import (
    Garmin,
    GarminConnectAuthenticationError
)

def get_mfa():
    """Get MFA."""
    return input("MFA one-time code: ")

def init_api(args):
    token_store = args.tokens
    try:
        garmin = Garmin()
        garmin.login(token_store)
        return garmin
    except (FileNotFoundError, GarthHTTPError, GarminConnectAuthenticationError):
        print("OAuth tokens not found, logging in...")
        garmin = Garmin(email=args.username, password=args.password, is_cn=False, prompt_mfa=get_mfa)
        garmin.login()
        garmin.garth.dump(token_store)
        print(f"OAuth tokens stored in '{token_store}' directory for future use")
        return garmin