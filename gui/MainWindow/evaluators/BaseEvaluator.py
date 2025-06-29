from datetime import datetime

class BaseEvaluator:
    def __init__(self, logFunc=None):
        self.logFunc = logFunc if logFunc else print

    def startLog(self):
        """ Function to start a log and display initial information for the execution
        """
        # Pretty Prints
        self.logInfo("")
        self.logInfo("")
        self.logInfo("Separation distance between MV/LV substation and secondary neutral grounding configurations")
        self.logInfo("")
        self.logInfo("")

    def closeLog(self):
        """ Function to close a log and display final information for the execution
        """
        # Pretty Prints
        self.logInfo("")
        self.logInfo("Evaluation has finished")
        self.logInfo("Closing log")
        self.logInfo("")

    def logInfo(self, message):
        """ Wrapper function to print Info logs with appended date timestamps

        Arguments: 
            message (string): Message to be printed
        """
        timestamp = self._getTimestamp()
        self.logFunc(f"<I {timestamp}: {message}")

    def logWarning(self, message):
        """ Wrapper function to print Warning logs with appended date timestamps

        Arguments: 
            message (string): Message to be printed
        """
        timestamp = self._getTimestamp()
        self.logFunc(f"<W {timestamp}: {message}")

    def logError(self, message):
        """ Wrapper function to print Error logs with appended date timestamps

        Arguments: 
            message (string): Message to be printed
        """
        timestamp = self._getTimestamp()
        self.logFunc(f"<E {timestamp}: {message}")

    def _getTimestamp(self):
        """Function to generate a timestamp string with milliseconds precision
        """
        # Get the current datetime
        now = datetime.now()
        # Format the datetime as a string with seconds
        timestamp_str = now.strftime("%Y%b%d %H:%M:%S")
        # Get the milliseconds separately
        millis_str = now.strftime("%f")[:-3]
        # Combine the timestamp and milliseconds strings
        return f"{timestamp_str}.{millis_str}"
