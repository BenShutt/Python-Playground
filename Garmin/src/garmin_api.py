#!/usr/bin/env python3

from getpass import getpass
from garth.exc import GarthHTTPError
from garminconnect import (
    Garmin,
    GarminConnectAuthenticationError
)

def get_mfa():
    """Get MFA"""
    return input("MFA one-time code: ")

def get_credentials():
    """Get user credentials"""
    email = input("Garmin Connect email: ")
    password = getpass("Garmin Connect password: ")
    return email, password

def init_api(args):
    token_store = args.tokens
    try:
        garmin = Garmin()
        garmin.login(token_store)
        return garmin
    except (FileNotFoundError, GarthHTTPError, GarminConnectAuthenticationError):
        print("OAuth tokens not found, please log in")
        email, password = get_credentials()
        garmin = Garmin(email=email, password=password, is_cn=False, prompt_mfa=get_mfa)
        garmin.login()
        garmin.garth.dump(token_store)
        print(f"OAuth tokens stored in the {token_store} directory for future use")
        return garmin