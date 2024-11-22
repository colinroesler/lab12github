import pytest
from television import *


def test_init():
    """Test that the Television initializes with default values."""
    tv = Television()
    assert tv._Television__status == False
    assert tv._Television__mute == False
    assert tv._Television__channel == Television.MIN_CHANNEL
    assert tv._Television__volume == Television.MIN_VOLUME

def test_power():
    """Test that the power method turns the TV on and off."""
    tv = Television()
    tv.power()  # Turn TV on
    assert tv._Television__status == True
    tv.power()  # Turn TV off
    assert tv._Television__status == False

def test_mute():
    """Test that muting works correctly."""
    tv = Television()
    tv.power()  # Turn TV on to test muting
    tv.mute()  # Mute the TV
    assert tv._Television__mute == True
    tv.mute()  # Unmute the TV
    assert tv._Television__mute == False

def test_channel_up():
    """Test channel_up functionality for both off and on."""
    tv = Television()

    initial_channel = tv._Television__channel
    tv.channel_up()
    assert tv._Television__channel == initial_channel

    tv.power()
    tv.channel_up()
    assert tv._Television__channel == Television.MIN_CHANNEL + 1
    tv._Television__channel = Television.MAX_CHANNEL
    tv.channel_up()
    assert tv._Television__channel == Television.MIN_CHANNEL


def test_channel_down():
    """Test channel_down functionality for both off and on ."""
    tv = Television()

    initial_channel = tv._Television__channel
    tv.channel_down()
    assert tv._Television__channel == initial_channel

    tv.power()
    tv.channel_down()
    assert tv._Television__channel == Television.MAX_CHANNEL
    tv._Television__channel = Television.MAX_CHANNEL
    tv.channel_down()
    assert tv._Television__channel == Television.MAX_CHANNEL - 1


def test_volume_up():
    """Test volume_up functionality for both off and on."""
    tv = Television()

    initial_volume = tv._Television__volume
    tv.volume_up()
    assert tv._Television__volume == initial_volume

    tv.power()
    tv.volume_up()
    assert tv._Television__volume == Television.MIN_VOLUME + 1
    tv._Television__volume = Television.MAX_VOLUME
    tv.volume_up()
    assert tv._Television__volume == Television.MAX_VOLUME


def test_volume_down():
    """Test volume_down functionality for both off and on."""
    tv = Television()


    initial_volume = tv._Television__volume
    tv.volume_down()
    assert tv._Television__volume == initial_volume

    tv.power()
    tv.volume_down()
    assert tv._Television__volume == Television.MIN_VOLUME
    tv._Television__volume = Television.MIN_VOLUME + 1
    tv.volume_down()
    assert tv._Television__volume == Television.MIN_VOLUME

