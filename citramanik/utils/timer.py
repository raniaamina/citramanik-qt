import time

class CitramanikTimer:

    """ Timer class utility for time elapsed information. """

    def start(self):
        """ Start the timer. """
        self.timer_start = time.monotonic()
    
    def get_elapsed_time(self):
        """ Get elapsed time in second format (ex: 12.2s). """
        timer_stop = time.monotonic() - self.timer_start
        return "%.2fs" % timer_stop
