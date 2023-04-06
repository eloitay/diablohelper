import os
from datetime import datetime
from time import sleep

from apscheduler.schedulers.blocking import BlockingScheduler

import diablohelper as dh


def tick():
    print('Tick! The time is: %s' % datetime.now())
    if (dh.inDiablo()):
        revive()
        if (dh.inActionMode()):
            if (dh.estimateHP() < 45):
                dh.heal()
            combatCycle()
            dh.clearSouthRoute()


def revive():
    dh.revive()


def clearLoot():
    dh.clearLoot()


def combatCycle():
    print("In Combat.")


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(tick, 'interval', seconds=1)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
