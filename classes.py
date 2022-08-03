class Television:
    """
    A class representing details for a television object.
    """
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        Contstructor to create initial state for television object.
        Creates private variables for channel, volume, and power state.
        Channel and volume variables are initialized at the minimum value, power is set to be off (0).
        """
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__on = 0

    def power(self) -> None:
        """
        Method to toggle the power state of the television object.
        Sets the power to on (1) if off (0), and off if on.
        """
        if self.__on == 1:
            self.__on = 0
        else:
            self.__on = 1

    def channel_up(self) -> None:
        """
        Method to increase the channel value of the television object by 1.
        Increasing the value while at the max value will cycle the channel back to the min value.
        """
        if self.__on == 1:
            if self.__channel + 1 > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Method to decrease the channel value of the television object by 1.
        Decreasing the value while at the min value will cycle the channel back to the max value.
        """
        if self.__on == 1:
            if self.__channel - 1 < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Method to increase the volume value of the television object by 1.
        Increasing the value while at the max value will cause no change.
        """
        if self.__on == 1:
            if self.__volume + 1 <= Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to decrease the volume value of the television object by 1.
        Decreasing the value while at the min value will cause no change.
        """
        if self.__on == 1:
            if self.__volume - 1 >= Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to retrieve the power, channel, and volume status of the television object.
        :return: Power state (True/False), channel number, and volume number.
        """
        power_status = ''
        if self.__on:
            power_status = 'True'
        else:
            power_status = 'False'
        status = 'TV status: Is on = {}, Channel = {}, Volume = {}'
        return status.format(power_status, self.__channel, self.__volume)
