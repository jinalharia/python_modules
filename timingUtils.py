import cProfile
import pstats
import io
import time

class TimingUtil(object):

    def __init__(self, logger, cProf=True, verbose=False, sortby="cumtime", top=10):
        self.logger = logger
        self.cProf = cProf
        self.verbose = verbose
        self.sortby = sortby
        self.top = top
        self.aggregate_logs = ""

        if cProf:
            self.pr = cProfile.Profile()
            self.pr.enable()
        else:
            self.time0 = time.time()
            self.summary_time0 = self.time0

    def print(self, msg, summary=False):
        if self.cProf:
            self.pr.disable()
            s = io.StringIO()
            ps = pstats.Stats(self.pr, stream=s).sort_stats(self.sortby)
            self.logger.info(msg)
            ps.print_stats(self.top)
            self.logger.info(s.getvalue())
            self.pr.enable()

        else:
            log_msg = msg + " - Time Elapsed = " + str(round(time.time() - (self.summary_time0 if summary else self.time0), 3)) + "s"
            self.aggregate_logs += log_msg + "\n"
            self.logger.info(log_msg)
            self.time0 = time.time()

    def get_msgs(self):
        return self.aggregate_logs